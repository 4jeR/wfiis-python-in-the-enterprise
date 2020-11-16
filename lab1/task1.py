# Write a module that will simulate autonomic car.
# The simulation is event based, an example:
# car1 = Car()
# car1.act(event)
# print(car1.wheel_angle, car1.speed)
# where event can be anything you want, i.e. :
# `('obstacle', 10)` where `10` is a duration (time) of the event.
##The program should:
# - act on the event
# - print out current steering wheel angle, and speed
# - run in infinite loop
# - until user breaks the loop

#The level of realism in simulation is of your choice, but more sophisticated solutions are better.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to github repository. 
#
#Delete these comments before commit!
#Good luck.

import time
from random import randint
import math 


class Engine:
    def __init__(self, acc_rate=5):
        self.rate = acc_rate

class Brakes:
    def __init__(self, dec_rate=5):
        self.rate = dec_rate

class Car:
    def __init__(self, engine, brakes, wheel_angle=0, speed=0):
        self.engine = engine
        self.brakes = brakes
        self.wheel_angle = 0
        self.speed = 0
        
    def __str__(self):
        return f'Car({self.wheel_angle} {self.speed})'

    def accelerate(self):
        print(f'Car is accelerating by {self.engine.rate}')
        if self.speed < 70:
            self.speed += self.engine.rate
            self.wheel_angle += self.speed * 0.01

    def decelerate(self):
        self.speed -= self.brakes.rate
        self.wheel_angle -= self.speed * 0.01
        if self.speed < 0:
            self.speed = 0
        if self.wheel_angle < 0:
            self.wheel_angle = 0



    def act(self, event):
        global total_time
        print(f'Car has slowed, because of {event.name}')
        for i in range(event.duration):
            self.decelerate()
            if self.wheel_angle < 0:
                self.wheel_angle = 0
            total_time += 1


class Event:
    def __init__(self, name='Obstacle', duration=3, odds=10):
        self.name = name
        self.duration = duration
        self.odds = odds

    def __str__(self):
        return f'An event occured: {self.name}, for {self.duration}'
   
   
    def __repr__(self):
        return f'An event occured: {self.name}, for {self.duration}'


 
if __name__=='__main__':
    total_time = 0
    engine = Engine(4)
    brakes = Brakes(15)
    car = Car(engine=engine, brakes=brakes)


    while True:
        total_time += 1
        car.accelerate()

        print(f'Car: {car.speed} km/h, {car.wheel_angle} rate')
        print(f'[TIME {total_time}]')

        event_odds = randint(0, 100)

        if event_odds < 5:
            evt = Event('Obstacle', 3)
            car.act(evt)

        time.sleep(1)
