# https://realpython.com/python3-object-oriented-programming/
# Dog class

class Dog:
    # pass # just a place holder for code.

    # Class Attributes
    # Class attributes are same for all instances
    species = 'mammal'

    # Initializer / Instance Attributes
    # initialize instance attributes
    # self is referring to the object itself, Dog here
    # Must have at-least one argument
    # Instance attributes are different for each instance/object

    # Init gets called automatically when you create a new Dog instance
    # This is like a constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # Instance methods
    # first argument is always self
    def description(self):
        return '{} is {} years old.'.format(self.name, self.age)

    # Instance method
    def speak(self, sound):
        return '{} says {}.'.format(self.name, sound)

    # Instance method
    # To modify age by +1
    def make_older(self):
        self.age += 1

    # Instance method
    # to change is_hungry to False
    def eat(self):
        self.is_hungry = False

    # Instance method
    # each dog walks
    def walk(self):
        return '{} is walking!'.format(self.name)


# Creating a new dog object, since the constructor takes two arguments
# we need to provide two arguments to the constructor.

# We don't need to pass the self or Dog to the constructor.
# Python automatically determines what self is.
a = Dog('Tony', 10)

# Type of a is class of Type Dog
print(type(a))

# you can access the members of a class with . operator
print(a.name)
print(a.age)

# create a new dog with the same attributes
b = Dog('Tony', 10)

# since a and b are two different instances of class
# they are not equal
print(a == b)

# create two instances of dogs with different attributes
philo = Dog('Philo', 5)
mikey = Dog('Mikey', 6)

# another way of printing
print('{} is {} years and {} is {} years.'.format(philo.name, philo.age, mikey.name, mikey.age))

# Check the class attributes
print('{} is {}'.format(philo.name, philo.species))


# ## The Oldest Dog ## #
# take any number of arguments to a function
# return the oldest dog
# you can take multiple arguments with *args
# all the arguments come as a list named args
def oldest_dog(*args):
    oldest = 0
    for dog in args:
        if dog.age > oldest:
            oldest = dog.age
            oldest_name = dog.name
    print('{} is the oldest dog and is {} years old.'.format(oldest_name, oldest))

dog1 = Dog('Tony', 4)
dog2 = Dog('Cherry', 6)
dog3 = Dog('rocky', 5)

oldest_dog(dog1, dog2, dog3)


# Checking instance methods
mikey = Dog('Mikey', 6)

# you call it using an instance of class
# so self knows what object it is.
print(mikey.description())
print(mikey.speak('Gruff Gruff'))

# Modifying attributes
# update the age of Mikey using method make_older
mikey.make_older()
print('{} is now {} years old.'.format(mikey.name, mikey.age))


# Inheritance
# Object class is the parent of all other classes

# child class(inherits from Dog class)
class RussellTerrier(Dog):

    def run(self, speed):
        return '{} runs {}'.format(self.name, speed)

# Child class(inherits from Dog class)
class Bulldog(Dog):

    species = 'Big Dogs'

    def run(self, speed):
        return '{} runs {}'.format(self.name, speed)


# Since Bulldog is inherited from Dog class
# we can create a new Bulldog object using Dog class constructor
jim = Bulldog('Jim', 12)
print(jim.description())

# child class has specific behaviour and attributes
# here we have specific behaviour
print(jim.run('slowly'))

# type of jim is Bulldog which is inherited from Dog
print(type(jim))


# isinstance() method is used to check if an instance is
# also an instance of a certain parent class

# check for instance
# Jim in instance of both Bulldog and Dog class
print(isinstance(jim, Bulldog))
print(isinstance(jim, Dog))

# Jim is not an instance of RussellTerrier
print(isinstance(jim, RussellTerrier))

# Child classes can override attributes and methods of parent class.
# we added the {species = 'Big Dogs'} to Bulldog class
# this modifies the species attribute of the Dog class
print(jim.species)


# ## Dog inheritance ## #
# create a pet class that holds the instance of Dog class

class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    # Instance method
    def walk(self):
        for dog in dogs:
            print(dog.walk())


# list of dog objects
tom = Dog('Tom', 4)
fletcher = Dog('Fletcher', 7)
larry = Dog('Larry', 9)

dogs = [tom, fletcher, larry]

# instance of pet class
pets = Pets(dogs)

print('I have {} dogs.'.format(len(pets.dogs)))
for dog in pets.dogs:
    print('{} is {}.'.format(dog.name, dog.age))
print('And they\'re all {}, of course.'.format(pets.dogs[0].species))


# ## Hungry Dogs ## #
# add an instance attribute {is_hungry = True} to the Dog class
# add a method {eat()} which changes is_hungry to False

# feed the dogs
for dog in pets.dogs:
    dog.eat()

any_hungry = False
for dog in pets.dogs:
    if dog.is_hungry == True:
        any_hungry = True

if any_hungry == False:
    print('My dogs are not hungry')
else:
    print('My dogs are hungry')


# ## Dog Walking ## #
# add a method in both Dog and Pets class
# call walk method for each instance of Dog class
# the above action can be performed inside the walk function of Pets class
pets.walk()