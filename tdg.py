import namegenerator
import random

#methods for automatic test data generation

def name_generator():
    name=namegenerator.gen()
    return name.replace('-',' ')

def username_generator():
    name=name_generator()
    usarname=name.split(' ')
    number = random.randint(0,1000)
    return(usarname[1]+str(number))

def email_generator():
    user=username_generator()
    return (user+'@gmail.com')

def password_generator():
    return "@Forabolso13"