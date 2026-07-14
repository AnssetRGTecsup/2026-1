# Grupo 2

* Torres Adrian
* Cuya Xiomara
* Lazo Anelhy
* Huamán Vidal
* Medina Fidel

### [Registrar Estudiante](ProyectoFinalFundamentos/RegistrarEstudiante.py)
* 

### [Actualizar Datos del Estudiante](ProyectoFinalFundamentos/ActualizarEstudiante.py)
* 

### [Registrar Curso](ProyectoFinalFundamentos/RegistrarCurso.py)
* Structure
```py
estudiante[EST_CURSOS][nombre_curso] = {
        CUR_CREDITOS: creditos,
        CUR_EVALUACIONES: [],   
        CUR_HORAS: [],           
    }
```

### [Actualizar Evaluaciones](ProyectoFinalFundamentos/ActualizarEvaluaciones.py)
* Not bucled on validation
```py
    curso_llave = None

   
    for curso in estudiante[EST_CURSOS]:
        if curso.lower() == nombre_input.lower():
            curso_llave = curso
            break

    if not curso_llave:
        print(f"El curso '{nombre_input}' no existe.")
        return
```
* Adding only one by one


### [Actualizar Horas de Estudio](ProyectoFinalFundamentos/ActualizarEvaluaciones.py)
* Not bucled on validation
* Adding only one by one

### [Eliminar Curso(s)](ProyectoFinalFundamentos/EliminarCurso.py): Puede ser solo 1, varios a la vez o todos.
* Review options

### Imprimir Datos de Curso(s): Puede ser solo 1, varios a la vez o todos.
* Review names of methods
* Review options

### Guardar archivos.
* Using custom name file instead of code

### Leer archivos.
* Using custom name file instead of code

### Generar Reporte Gráfico.
* 

### Extras

* In [seleccionar_estudiants](ProyectoFinalFundamentos/main.py): why select a student per run
```py
    for i, est in enumerate(estudiantes, 1): # enumerate
        print(f"{i}. {est['nombre']} ({est['codigo']})")
```
* Use of [Constants](ProyectoFinalFundamentos/constantes.py)