import random
from datetime import datetime, timedelta
from constantes import (
    EST_CODIGO, EST_NOMBRE, EST_CICLO, EST_CURSOS,
    CUR_CREDITOS, CUR_EVALUACIONES, CUR_HORAS,
    EVA_NOMBRE, EVA_FECHA, EVA_NOTA, EVA_PESO
)

def GenerarDatosAleatorios(lista_estudiantes):
    print("\n--- GENERANDO DATOS ALEATORIOS DE PRUEBA ---")
    
    
    nombres_fijos = [
        "Anelhy Lazo", 
        "Vidal Huaman", 
        "Fidel Medina", 
        "Adrian Torres", 
        "Xiomara Cuya"
    ]
    
    
    cursos_disponibles = [
        "Fundamentos de Programacion", 
        "Diseño de interfaces de programacion", 
        "Ciencias basicas aplicadas", 
        "Tecnicas de expresion oral y escrita", 
        "calculo y estadistica", 
        "Desarrollo Personal"
    ]
    
    evaluaciones_tipos = [
        {"nombre": "PC1", "peso": 0.20},
        {"nombre": "PC2", "peso": 0.20},
        {"nombre": "EA", "peso": 0.30},
        {"nombre": "EB", "peso": 0.30}
    ]

    try:
        cantidad = int(input(f"¿Cuántos estudiantes desea generar? (Máximo {len(nombres_fijos)}): "))
        if cantidad <= 0:
            print("Cantidad no válida. Operación cancelada.")
            return
        if cantidad > len(nombres_fijos):
            print(f"Solo contamos con {len(nombres_fijos)} nombres en el banco. Ajustando cantidad a {len(nombres_fijos)}.")
            cantidad = len(nombres_fijos)
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")
        return

    
    nombres_a_generar = random.sample(nombres_fijos, cantidad)

    for nombre_completo in nombres_a_generar:
        codigo_aleatorio = f"U2026{random.randint(10000, 99999)}A"
        ciclo_aleatorio = random.randint(1, 5)
        
        if any(est[EST_CODIGO] == codigo_aleatorio for est in lista_estudiantes):
            continue

        nuevo_estudiante = {
            EST_CODIGO: codigo_aleatorio,
            EST_NOMBRE: nombre_completo,
            EST_CICLO: ciclo_aleatorio,
            EST_CURSOS: {}
        }

        
        for curso in cursos_disponibles:
            nuevo_estudiante[EST_CURSOS][curso] = {
                CUR_CREDITOS: random.randint(2, 5),
                CUR_EVALUACIONES: [],
                CUR_HORAS: []
            }
            
            
            for _ in range(random.randint(1, 5)):
                horas_sesion = round(random.uniform(0.5, 4.0), 1)
                nuevo_estudiante[EST_CURSOS][curso][CUR_HORAS].append(horas_sesion)
            
            
            for eva_modelo in evaluaciones_tipos:
                dias_atras = random.randint(1, 30)
                fecha_aleatoria = datetime.now() - timedelta(days=dias_atras)
                nota_aleatoria = round(random.uniform(9.0, 20.0), 1) 
                
                nuevo_estudiante[EST_CURSOS][curso][CUR_EVALUACIONES].append({
                    EVA_NOMBRE: eva_modelo["nombre"],
                    EVA_FECHA: fecha_aleatoria,
                    EVA_NOTA: nota_aleatoria,
                    EVA_PESO: eva_modelo["peso"]
                })

        lista_estudiantes.append(nuevo_estudiante)
        
    print(f"\n¡Éxito! Se han generado {cantidad} estudiantes. Cada uno con los 6 cursos inscritos y sus 4 notas completas.")