# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 19:35:59 2021

@author: wajee
"""
import random
import importlib
import turtle
from turtle import Turtle , Screen
importlib.reload(turtle)


def random_color():
    
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    colour=(red,green,blue)
    return(colour)

timmy=Turtle()
timmy.shape("turtle")
screen=Screen()
timmy.speed("fastest")
screen.colormode(255)
angle=5

for i in range(360):
    
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(angle)
    angle+=5


screen.exitonclick()