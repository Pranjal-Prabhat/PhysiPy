def gravitational(mass1,distance,mass2):
    """
    Calculates gravitational force based on given parameters.

    Raises:
    ValueError: If no valid values are given to calculate gravitational force.
    """
    return (mass1*mass2*6.67430e-11)/distance**2

def buoyant(density,volume,gravity):
    """
    Calculates buoyant force based on given parameters.

    Raises:
    ValueError: If no valid values are given to calculate buoyant force.
    """
    return density*volume*gravity

def spring(equilibrium_pos,displaced_pos,constant):
    """
    Calculates spring force based on given parameters.

    Raises:
    ValueError: If no valid values are given to calculate spring force.
    """
    return (-equilibrium_pos+displaced_pos)*constant




