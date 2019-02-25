#from https://classroom.udacity.com/courses/ud088/lessons/3621198668/concepts/36300689480923l

# how to create a session in terminal to make changes to existing databses
#ctrl shift p in vs code and change python interpreter to the one in c:/python folder (3.4?)
#anything done below, do in vs code bash terminal, while in vagrant folder. 


#to start vagrant VM, open a git terminal in or out of vs code, navigate to Desktop/Projects/fullstack/vagrant
# do 'vagrant up' then vagrant ssh to connect

#do at the start of each session to connect to db in terminal
python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


#CRUD Create, creates a database entry restaurant with the given name. add/commit commits it to the database, 
# query returns all entries in the Restaurant table
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()
session.query(Restaurant).all()
#create a menu item like so below
cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with fresh mozzarella", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)

#CRUD read, reads all menu items, creates a variable first result that's only the first result of the query, then prints the name of it
session.query(MenuItem).all()
firstResult = session.query(Restaurant).first()
firstResult.name


#CRUD Update, uses the id of 8 to assign variable to current entry, updates the price of it, commits,
#the price of it in the table is updated to $2.99
#first for loop updates all veggie burger prices to $2.99 if they aren't already. 
#Second for loop prints out results from table
UrbanVeggieBurger = session.query(MenuItem).filter_by(id = 8).one()
print(UrbanVeggieBurger.price)
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()
veggieBurgers = session.query(MenuItem). filter_by(name = 'Veggie Burger')
for veggieBurger in veggieBurgers:
    if veggieBurger.price != '$2.99'
        veggieBurger.price = '$2.99'
        session.add(veggieBurger)
        session.commit()

for veggieBurger in veggieBurgers:
    print(veggieBurger.id)
    print(veggieBurger.price)
    print(veggieBurger.restaurant.name)
    print("\n")



#CRUD Delete, finds an entry, does a session delete, and commits, query at the end returns no results
spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
print spinach.restaurant.name
session.delete(spinach)
session.commit()
spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()