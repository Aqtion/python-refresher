import numpy as np

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
    torque = F_magnitude * np.sin(np.radians(F_direction)) * r
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


def calculate_auv_acceleration(
    F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5
):
    """
    Calculates acceleration of AUV given magnitude of force exerted by thruster and mass of AUV.

    F_magnitude - Magnitude of force exerted by thruster |
    F_angle - Angle of force applied by the thruster in degrees
    mass - (optional), mass of the AUV |
    volume - (optional), volume of the AUV |
    thruster_distance - (optional), distance of thruster from center of mass of AUV

    """
    if F_magnitude < 0 or mass <= 0:
        raise ValueError(
            "Magnitude of force must be positive and mass must be positive."
        )
    auv_acceleration = np.array(
        [
            F_magnitude * np.cos(np.radians(F_angle)) / mass,
            F_magnitude * np.sin(np.radians(F_angle)) / mass,
        ],
        dtype=float,
    )
    return auv_acceleration


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    """
    Calculates angular acceleration of AUV given magnitude of force exerted by thruster and angle of force respective to center of mass.

    F_magnitude - Magnitude of force exerted by thruster |
    F_angle - Angle of thruster exerting force on AUV |
    inertia - (optional), moment of inertia of AUV |
    thruster_distance (optional), distance of thruster from center of mass from AUV
    """
    if F_magnitude < 0:
        raise ValueError("Magnitude of force must be positive.")
    torque = F_magnitude * np.sin(np.radians(F_angle)) * thruster_distance
    print(torque)
    auv_angular_acceleration = torque / inertia
    return auv_angular_acceleration


def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    """
    Calculates linear acceleration of AUV given magnitude of force exerted by all 4 thrusters, their angles, and mass of AUV.

    T - Forces exerted by each of the 4 thrusters
    alpha - Angle of each thruster |
    theta - Rotation of AUV |
    mass - Mass of AUV
    """
    cos_angle = np.cos(alpha)
    sin_angle = np.sin(alpha)
    signs_matrix = np.array(
        [
            cos_angle,
            cos_angle,
            -cos_angle,
            -cos_angle,
            sin_angle,
            -sin_angle,
            -sin_angle,
            sin_angle,
        ],
    ).reshape(2, 4)
    forces_matrix = np.dot(signs_matrix, T)
    # print(forces_matrix)
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    rotation_matrix = np.array([cos_theta, -sin_theta, sin_theta, cos_theta]).reshape(
        2, 2
    )

    acceleration_matrix = np.divide(np.dot(rotation_matrix, forces_matrix), mass)

    return acceleration_matrix


def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia=100):
    """
    Calculates angular acceleration of AUV given magnitude of force exerted by thrusters, angle of thrusters, and dimensions of AUV.

    T - Magnitude of force exerted by thruster |
    alpha - angle of thruster with respect to x-axis |
    L - half of the length of the AUV |
    l - half of the width of the AUV |
    inertia - (optional), moment of inertia of AUV
    """
    net_torque = 0
    for i in range(4):
        sin_angle = np.sin(alpha)
        cos_angle = np.cos(alpha)
        if i % 2 == 0:
            net_torque -= T[i] * (sin_angle * L + cos_angle * l)
        else:
            net_torque += T[i] * (sin_angle * L + cos_angle * l)
    angular_acceleration = net_torque / inertia
    return angular_acceleration


print(calculate_auv2_acceleration([2, 4, 8, 6], np.pi / 4, np.pi / 6, 1))
