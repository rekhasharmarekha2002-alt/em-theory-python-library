import sys
sys.path.append("C:/Users/sagar/Desktop")  # path to the folder containing EM_Library

from EM_Library.coulomb import coulomb_field

E = coulomb_field(1e-6, 0.5)
print(E)

