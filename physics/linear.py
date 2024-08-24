"""
This module helps to to get some values in linear motion.
"""

from sympy import factor,symbols

def distance(time,acceleration=None,initial=None,speed=None):
    """
    Calculates kinectic energy under given parameters.
    It can calculate in 4 condidtion/
                                    if initial velocity and acceleration is given
                                    if initial velocity given and acceleration is not given
                                    if acceleration given and initial velocity is not given
                                    if acceleration and initial velocity not given but speed given
    time is compulsary

    acceleration is compulsary.
    raises:
           ValueError: If no valid conditions are found to calculate kinectic enrgy or error=True.
    """
    
    if (initial != None ):
        if (acceleration != None):
            return (initial*time + (1/2)*acceleration*time**2)
        else:
            return  (initial*time)
        
    else:
        if (acceleration != None):
            return ((1/2)*acceleration*time**2)
        else:
            return (speed*time)

def acceleration( s=None , force =None , mass =1 , initial=None , final=None , time =None ,error = True):
    """
    Calculate acceleration based on given parameters.

    Parameters:
    force (float): The force applied (optional).
    s (float): Displacement (optional).
    initial (float): Initial velocity (optional).
    final (float): Final velocity (optional).
    time (float): Time duration (optional).
    error (bool): Flag to raise an error if no conditions are met (optional).

    Returns:
    float: Calculated acceleration.

    Raises:
    ValueError: If no valid conditions are found to calculate acceleration.
    """
    if (force != None and s ==None and initial==None and final==None and time ==None ):
        return force/mass
    
    elif (force == None and s ==None and initial != None and final != None and time !=None ):
        return (final - initial)/time
    
    elif (force == None and s != None and initial != None and final == None and time !=None ):
        return 2*(s - initial*time)/time**2
    
    elif (force == None and s != None and initial != None and final != None and time ==None ):
        return (final**2 - initial**2)/2*s
    
    elif(error==True):
        raise ValueError("No conditions were found to calulate acceleration by values given as argument.")
    
    else:
        pass


def collision_momentum(initial_of_A=None, initial_of_B=None, final_of_A=None, final_of_B=None, mass_of_A=None, mass_of_B=None):
    """
    Calculate unknown initial or final velocities or masses in a collision scenario.

    1 value that is is not provided will be found.

    Parameters:
    initial_of_A (float): Initial velocity of object A (optional).
    initial_of_B (float): Initial velocity of object B (optional).
    final_of_A (float): Final velocity of object A (optional).
    final_of_B (float): Final velocity of object B (optional).
    mass_of_A (float): Mass of object A (optional).
    mass_of_B (float): Mass of object B (optional).

    Returns:
    float: Calculated value of the unknown parameter.

    Raises:
    ValueError: If less or wrong parameters are provided for calculating mass or velocity in collision.
    """
    if initial_of_A ==None and initial_of_B != None and final_of_A != None and final_of_B != None and mass_of_A != None and mass_of_B != None:
        return ((mass_of_B * (final_of_B - initial_of_B)) / mass_of_A) + final_of_A
    
    elif initial_of_B ==None and initial_of_A != None and final_of_A != None and final_of_B != None and mass_of_A != None and mass_of_B != None:
        return ((mass_of_A * (final_of_A - initial_of_A)) / mass_of_B) + final_of_B
    
    elif final_of_A ==None and initial_of_A != None and initial_of_B != None and final_of_B != None and mass_of_A != None and mass_of_B != None:
        return ((mass_of_A * initial_of_A) + (mass_of_B * initial_of_B) - (mass_of_B * final_of_B)) / mass_of_A
    
    elif final_of_B ==None and initial_of_A != None and initial_of_B != None and final_of_A != None and mass_of_A != None and mass_of_B != None:
        return ((mass_of_A * initial_of_A) + (mass_of_B * initial_of_B) - (mass_of_A * final_of_A)) / mass_of_B
    
    elif mass_of_A ==None and initial_of_A != None and initial_of_B != None and final_of_A != None and final_of_B != None and mass_of_B != None:
        return ((mass_of_B * (final_of_B - initial_of_B)) + (mass_of_B * initial_of_B)) / (final_of_A - initial_of_A)
    
    elif mass_of_B ==None and initial_of_A != None and initial_of_B != None and final_of_A != None and final_of_B != None and mass_of_A != None:
        return ((mass_of_A * (final_of_A - initial_of_A)) + (mass_of_A * initial_of_A)) / (final_of_B - initial_of_B)
    
    else:
        raise ValueError("Less or wrong parameters provided for calculating mass or velocity in collison.")

def time(displacement=None,acceleration=None,initial=None,final=None,error=True):
    """
    Calculates kinectic energy under given parameters.
    It can calculate in 2 condidtion/
                                    if final velocityand  initial velocity is given
                                    if initial velocity and displacement is given
    acceleration is compulsary.
    raises:
           ValueError: If no valid conditions are found to calculate kinectic enrgy or error=True.
    """
    if(displacement==None and acceleration!=None and initial!=None and final!=None):
        return (final-initial)/acceleration
    
    elif(displacement!=None and acceleration!=None and initial!=None and final==None):
        t = symbols('t')
        return factor(0.5*acceleration*t**2+initial*t+displacement)
    
    elif(error == True):
        raise ValueError("Less or wrong parameters provided for calculating time.")
    
    else:
        pass


   
