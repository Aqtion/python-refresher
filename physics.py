import math

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


def calculate_acceleration(F, mass):
    """
    Calculates acceleration given force and mass.

    F - force applied on object |
    mass - mass of object
    """
    if mass <= 0:
        raise ValueError("Mass must be positive.")
    acceleration = F / mass
    return acceleration


def calculate_angular_acceleration(tau, I):
    """
    Calculates angular acceleration given torque and moment of inertia.

    tau - torque applied on object |
    I - moment of inertia of object
    """
    if I <= 0:
        raise ValueError("Moment of inertia must be positive.")
    angular_acceleration = tau / I
    return angular_acceleration


def calculate_torque(F_magnitude, F_direction, r):
    """
    Calculates torque given magnitude and direction of force and distance from center of mass .

    F_magnitude - magnitude of force applied on object |
    F_direction - direction of force applied on object |
    r - distance of force applied from center of mass
    """
    if F_magnitude < 0 or r < 0:
        raise ValueError(
            "Magnitude of force and distance to center of mass must be positive"
        )
    torque = F_magnitude * math.sin(math.radians(F_direction)) * r
    return torque


def calculate_moment_of_inertia(m, r):
    """
    Calculates moment of inertia given mass and distance from axis of rotation to center of mass.

    m - mass of object |
    r - distance from axis of rotation to center of mass
    """
    if m <= 0 or r < 0:
        raise ValueError(
            "Mass must be positive and distance to center of mass must be nonnegative."
        )
    moment_of_inertia = m * pow(r, 2)
    return moment_of_inertia


def calculate_auv_acceleration(F_magnitude, mass):
    if F_magnitude < 0 or mass <= 0:
        raise ValueError(
            "Magnitude of force must be positive and mass must be positive."
        )
    auv_acceleration = F_magnitude / mass
    return auv_acceleration


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5
):
    if F_magnitude < 0:
        raise ValueError("Magnitude of force must be positive.")
