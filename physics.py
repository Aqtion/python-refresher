g = 9.81


def calculate_buoyancy(V, density_fluid):
    """Calculate buoyant force.

    V -- volume of fluid |
    density_fluid -- density of fluid
    """
    buoyant_force = density_fluid * V * g
    return buoyant_force


def will_it_float(V, mass):
    """Checks whether object with given mass floating in a fluid of given volume (by Archimedes' principle) will float.
    V -- volume of object |
    mass -- mass of object
    """
    buoyant_force = V * 1000 * g
    weight = mass * g
    return buoyant_force > weight


def calculate_pressure(depth):
    """Calculates pressure at given depth.

    depth -- depth of object in water
    """
    pressure = 1000 * g * depth
    return pressure
