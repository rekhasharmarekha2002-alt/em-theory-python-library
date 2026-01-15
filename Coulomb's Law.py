"""
This program calculates the electrostatic force between two point charges
using Coulomb's law. Only basic Python is used.
"""

def coulomb_force(q1, q2, r):
    """
    q1 : charge of first particle in coulomb
    q2 : charge of second particle in coulomb
    r  : distance between charges in meter

    The function returns the magnitude of electrostatic force.
    """

    k = 9e9
    force = k * q1 * q2 / (r * r)
    return force


q1 = 2e-6
q2 = 4e-6
r = 0.5

F = coulomb_force(q1, q2, r)
print("Electrostatic force =", F, "N")
