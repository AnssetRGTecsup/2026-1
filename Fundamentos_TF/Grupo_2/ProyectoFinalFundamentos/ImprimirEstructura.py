from constantes import (
    EST_NOMBRE, EST_CODIGO, EST_CICLO, EST_CURSOS, 
    CUR_CREDITOS, CUR_EVALUACIONES, CUR_HORAS, 
    EVA_NOMBRE, EVA_FECHA, EVA_NOTA, EVA_PESO
)

def ImprimirEstructuraDiccionario(estudiante):
    
    print("\n========================================================")
    print("           DATOS GENERALES DEL ESTUDIANTE               ")
    print("========================================================")
    print(f"• Estudiante : {estudiante[EST_NOMBRE]}")
    print(f"• Código     : {estudiante[EST_CODIGO]}")
    print(f"• Ciclo      : {estudiante[EST_CICLO]}")
    print("--------------------------------------------------------")
    print("               DETALLE DE CURSOS Y NOTAS                ")
    print("--------------------------------------------------------")

    
    cursos = estudiante[EST_CURSOS]
    
    if not cursos:
        print("  (Este estudiante aún no tiene cursos registrados)")
        print("========================================================\n")
        return

    
    for nombre_curso, info_curso in cursos.items():
        
        total_horas = sum(info_curso[CUR_HORAS])
        
        print(f" CURSO: {nombre_curso} ({info_curso[CUR_CREDITOS]} Créditos)")
        print(f"  Tiempo invertido: {total_horas:.1f} horas totales")
        print(f"  Evaluaciones:")

        evaluaciones = info_curso[CUR_EVALUACIONES]
        if not evaluaciones:
            print("     (Aún no se registran exámenes para este curso)")
        else:
            for eva in evaluaciones:
                fecha_str = eva[EVA_FECHA].strftime("%d/%m/%Y")
                peso_porcentaje = int(eva[EVA_PESO] * 100)
                
                # Formato limpio para cada nota
                print(f" {eva[EVA_NOMBRE]}: Nota {eva[EVA_NOTA]} | Peso: {peso_porcentaje}% | Fecha: {fecha_str}")
        
        print(" . . . . . . . . . . . . . . . . . . . . . . . . . . . .")
        
    print("========================================================\n")