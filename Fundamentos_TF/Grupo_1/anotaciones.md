# Grupo 1

* Aliaga Espinoza Luis Caleb
* Lima Max
* Rivera Jeferson
* Ramirez Adrian

### [Registrar Estudiante](ProyectoLab16/gestion/registro.py)
* Not bucled
* Validate if student already exists

### [Actualizar Datos del Estudiante](ProyectoLab16/gestion/actualizacion.py)
* Displaying an option that may not be viable
* Changing all data in a bunch

### [Registrar Curso](ProyectoLab16/gestion/registro.py)
* Not bucled
* Displaying an unreachable option

### [Actualizar Evaluaciones](ProyectoLab16/gestion/actualizacion.py)
* Not bucled on validation
```py
    nombre_eval = input("Nombre de la evaluación (Ej: PA, EX, PR): ").strip()

    valido_nota, nota = leer_flotante("Nota (0 a 20): ")
    valido_peso, peso = leer_flotante("Peso (Ej: 0.20 para 20%): ")
    valido_fecha, fecha = leer_fecha("Fecha de la evaluación (dd/mm/aaaa): ")

    if not valido_nota or not valido_peso:
        print("Error: la nota y el peso deben ser valores numéricos. Operación cancelada.\n")
        return

    if not valido_fecha:
        print("Error: la fecha debe tener el formato dd/mm/aaaa. Operación cancelada.\n")
        return
```
* Displaying an unreachable option
* Adding only one by one


### [Actualizar Horas de Estudio](ProyectoLab16/gestion/actualizacion.py)
* Not bucled on validation
* Displaying an unreachable option
* Adding only one by one

### [Eliminar Curso(s)](ProyectoLab16/gestion/eliminacion.py): Puede ser solo 1, varios a la vez o todos.
* Review options

### Imprimir Datos de Curso(s): Puede ser solo 1, varios a la vez o todos.
* Review names of methods
* Review options

### Guardar archivos.
* Only save 1 student

### Leer archivos.
* Only read 1 student

### Generar Reporte Gráfico.
* 

### Extras

* In [menu](ProyectoLab16/utilidades/menu.py): datatype
* In [Curso](ProyectoLab16/modelos/entidades.py)
```py
class Curso:
    NOTA_MINIMA_APROBATORIA = 12 #Why in Uppercase
```
* In [Estudiante](ProyectoLab16/modelos/entidades.py)
```py
   def buscar_curso(self, nombre_curso):
        for curso in self.cursos:
            if curso.nombre.lower() == nombre_curso.strip().lower(): #Why using name
                return curso
        return None 
```