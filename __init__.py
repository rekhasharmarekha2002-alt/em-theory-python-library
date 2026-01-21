from coulomb import coulomb_field
from biot_savart import magnetic_field

E = coulomb_field(1e-6, 0.5)
B = magnetic_field(1.0, 0.2)

print("Electric Field =", E)
print("Magnetic Field =", B)