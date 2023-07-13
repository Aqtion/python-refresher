g = 9.81
base_atmospheric_pressure = 101325


def calculate_buoyancy(V, density_fluid):
    """Calculate buoyant force.

    V -- volume of fluid |
    density_fluid -- density of fluid
    """
    if V <= 0 or density_fluid <= 0:
        raise ValueError("Volume or density cannot be <= 0.")
    buoyant_force = density_fluid * V * g
    return buoyant_force


def will_it_float(V, mass):
    """Checks whether object with given mass floating in a fluid of given volume (by Archimedes' principle) will float.
    V -- volume of object |
    mass -- mass of object
    """
    if V <= 0 or mass <= 0:
        raise ValueError("Volume or mass cannot be <= 0.")
    buoyant_force = V * 1000 * g
    weight = mass * g
    return buoyant_force > weight


def calculate_pressure(depth):
    """Calculates pressure at given depth.

    depth -- depth of object in water
    """
    if depth <= 0:
        raise ValueError("Depth must be positive value.")
    pressure = 1000 * g * depth + base_atmospheric_pressure
    return pressure
