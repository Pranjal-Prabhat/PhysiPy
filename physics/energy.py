def kinetic(mass,velocity=None,time_of_fall=None,gravity=None,error=True):
    """
    Calculates kinectic energy under given parameters.
    It can calculate in 2 condidtion/
                                    if time_of_fall and gravity is given
                                    if velocity is given
    mass is compulsary.
    raises:
           ValueError: If no valid conditions are found to calculate kinectic enrgy or error=True.
    """
    if (velocity == None and time_of_fall != None and gravity != None):
        return (0.5*mass*(time_of_fall*gravity)**2)
    
    elif (velocity != None and time_of_fall == None and gravity == None):
        return (0.5*mass*velocity**2)
    
    elif(error == True):
        raise ValueError("Correct or right values were not given to find kinetic energy.")
    
    else:
        pass

def potential(mass,gravity,height=None,time_to_fall_down=None,error=True):
    """
    Calculates potential energy under given parameters.
    It can calculate in 2 condidtion/
                                    if time_of_fall and gravity is given
                                    if height and time_of_fall is given
    mass is compulsary.
    raises:
           ValueError: If no valid conditions are found to calculate potential enrgy or error=True.
    """
    if (height!=None and time_to_fall_down == None):
        return mass*gravity*height
    
    elif (height==None and time_to_fall_down != None):
        return mass*gravity**2*0.5*time_to_fall_down**2
    
    elif(error == True):
        raise ValueError("Correct or right values were not given to find potential energy.")
    
    else:
        pass
        
def nuclear(mass):
    """
    Calculates nuclear energy under given parameters.(takes mass as argument)

    raises:
           ValueError: If no valid conditions are found to calculate potential enrgy or error=True.
    """
    return 8.98755179*10**16*mass