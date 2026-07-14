from constantes import EST_NOMBRE, EST_CODIGO, EST_CICLO, EST_CURSOS, CUR_CREDITOS, CUR_EVALUACIONES, CUR_HORAS, EVA_NOMBRE, EVA_FECHA, EVA_NOTA, EVA_PESO
from ConvertirFecha import ConvertirFecha

def GuardarArchivos(lista_estudiantes):
    print("\n--- GUARDAR DATOS EN ARCHIVO ---")
    if not lista_estudiantes:
        print("No hay datos de estudiantes en el sistema para guardar.")
        return

    nombre_archivo = input("Ingrese el nombre del archivo para guardar (ejm: datos.txt): ").strip()
    if not nombre_archivo.endswith(".txt"):
        nombre_archivo = nombre_archivo + ".txt"

    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for estudiante in lista_estudiantes:
                
                archivo.write(f"ESTUDIANTE|{estudiante[EST_CODIGO]}|{estudiante[EST_NOMBRE]}|{estudiante[EST_CICLO]}\n")
                
                
                for nombre_curso, info_curso in estudiante[EST_CURSOS].items():
                    archivo.write(f"CURSO|{nombre_curso}|{info_curso[CUR_CREDITOS]}\n")
                    
                    horas_str = ",".join(str(h) for h in info_curso[CUR_HORAS])
                    archivo.write(f"HORAS|{horas_str}\n")
                    
                    for info_eva in info_curso[CUR_EVALUACIONES]:
                        fecha_str = info_eva[EVA_FECHA].strftime("%d/%m/%Y")
                        archivo.write(f"EVALUACION|{info_eva[EVA_NOMBRE]}|{fecha_str}|{info_eva[EVA_NOTA]}|{info_eva[EVA_PESO]}\n")
                    
        print(f"¡Éxito! Todos los datos se guardaron correctamente en '{nombre_archivo}'.")
    except Exception as e:
        print(f"Ocurrió un error al intentar guardar el archivo: {e}")

def LeerArchivos(lista_estudiantes):
    print("\n--- LEER DATOS DESDE ARCHIVO ---")
    nombre_archivo = input("Ingrese el nombre del archivo a cargar (ejm: datos.txt): ").strip()
    if not nombre_archivo.endswith(".txt"):
        nombre_archivo = nombre_archivo + ".txt"

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            
        if not lineas:
            print("El archivo especificado está vacío.")
            return

        lista_estudiantes.clear()
        estudiante_actual = None
        curso_actual = None

        for linea in lineas:
            partes = linea.strip().split("|")
            if not partes or partes[0] == "":
                continue
                
            tipo = partes[0]

            if tipo == "ESTUDIANTE":
                estudiante_actual = {
                    EST_CODIGO: partes[1],
                    EST_NOMBRE: partes[2],
                    EST_CICLO: int(partes[3]),
                    EST_CURSOS: {}
                }
                lista_estudiantes.append(estudiante_actual)
                curso_actual = None

            elif tipo == "CURSO":
                if estudiante_actual is not None:
                    nombre_cur = partes[1]
                    curso_actual = {
                        CUR_CREDITOS: int(partes[2]),
                        CUR_EVALUACIONES: [],
                        CUR_HORAS: []
                    }
                    estudiante_actual[EST_CURSOS][nombre_cur] = curso_actual

            elif tipo == "HORAS":
                if curso_actual is not None and len(partes) > 1 and partes[1]:
                    curso_actual[CUR_HORAS] = [float(h) for h in partes[1].split(",")]

            elif tipo == "EVALUACION":
                if curso_actual is not None:
                    nombre_eva = partes[1]
                    fecha_obj = ConvertirFecha(partes[2])
                    nota_val = float(partes[3])
                    peso_val = float(partes[4])
                    
                    curso_actual[CUR_EVALUACIONES].append({
                        EVA_NOMBRE: nombre_eva,
                        EVA_FECHA: fecha_obj,
                        EVA_NOTA: nota_val,
                        EVA_PESO: peso_val
                    })

        print(f"¡Éxito! Los datos de los estudiantes se cargaron correctamente.")
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer el archivo: {e}")