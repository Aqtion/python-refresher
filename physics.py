g = 9.81


def calculate_buoyancy(V, density_fluid):
    global g
    """
    :param float V: volume of fluid
    :param float density_fluid: density of fluid
    """
    buoyant_force = density_fluid * V * g
    return buoyant_force


def will_it_float(V, mass):
    global constants
    """
    :param float V: volume of fluid
    :param float mass: mass of object
    """
    buoyant_force = V * 1000 * g
    weight = mass * g
    return buoyant_force > weight


def calculate_pressure(depth):
    """
    :param float depth: depth of object in water
    """
    pressure = 1000 * g * depth
    return pressure
