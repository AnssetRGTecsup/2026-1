angle = float(input("Ingrese el angulo: "))

angle_type = ""

if angle == 0:
    angle_type = "Nulo"
elif angle < 90:
    angle_type = "Agudo"
elif angle == 90:
    angle_type = "Recto"
elif angle < 180:
    angle_type = "Obtuso"
elif angle == 180:
    angle_type = "Llano"
elif angle < 360:
    angle_type = "Concavo"
else:
    angle_type = "Complejo"

print(angle_type)