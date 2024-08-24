"""
This module helps to to get some values in projectile motion.
"""
import math

def h_max(theta,initial,gravity = 9.8):
    """
    Finds highest vertical height reached at a specific angle with specific velocity.
    gravity is set by default to 9.8m/s^2
    """
    return (math.sin(math.radians(theta))*initial)**2/(2*gravity)

def time_of_flight(theta,initial,gravity=9.8):
    """
    Finds highest time object will be in air at a specific angle with specific velocity.
    gravity is set by default to 9.8m/s^2
    """
    return 2*(math.sin(math.radians(theta))*initial)/gravity

def time_of_ascent(theta,initial,gravity=9.8):
    """
    Finds highest time object will be in air before reaching its peak at a specific angle and velocity.
    gravity is set by default to 9.8m/s^2
    """
    return time_of_flight(theta,initial,gravity)/2

def time_of_descent(theta,initial,gravity=9.8):
    """
    Finds highest time object will be in air after reaching its peak at a specific angle and velocity.
    gravity is set by default to 9.8m/s^2
    """
    return time_of_flight(theta,initial,gravity)/2\
    
def velocity_vertical(theta,initial,time,gravity=9.8):
    """
    Finds magnitude of vertical velocity at a given time of object an object after thrown.(At a specific initial velocity and angle)

    gravity is set by default to 9.8m/s^2
    """
    return (math.sin(math.radians(theta))*initial)-gravity*time

def distance_covered_vertical(theta,initial,time,gravity=9.8):
    """
    Finds vertical distance covered at a given time of object an object after thrown.(At a specific initial velocity and angle)

    gravity is set by default to 9.8m/s^2
    """
    return time*((math.sin(math.radians(theta))*initial)-1/2*gravity)

def distance_covered_horizontal(theta,initial,time,gravity=9.8):
    """
    Finds horizontal distance covered at a given time of object an object after thrown.(At a specific initial velocity and angle)

    gravity is set by default to 9.8m/s^2
    """
    return time*(math.cos(math.radians(theta))*initial)

def distance_covered_horizontal_max(theta,initial,gravity=9.8):
    """
    Finds maximum horizontal distance covered at a given time of object an object after thrown.(At a specific initial velocity and angle)

    gravity is set by default to 9.8m/s^2
    """
    return time_of_flight(theta,initial,gravity)*(math.cos(math.radians(theta))*initial)




