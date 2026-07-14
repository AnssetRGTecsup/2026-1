import matplotlib.pyplot as plt
import seaborn as sns
from constantes import EST_CURSOS, CUR_CREDITOS, CUR_HORAS, CUR_EVALUACIONES, EVA_NOTA, EVA_PESO

class ReporteAcademico:
    
    def __init__(self, estudiante):
        
        self.estudiante = estudiante
        self.cursos_data = estudiante.get(EST_CURSOS, {})
        self.nombres_cursos = []
        self.horas_totales = []
        self.notas_finales = []
        self._procesar_datos()

    def _procesar_datos(self):
        
        for nombre_curso, info_curso in self.cursos_data.items():
            self.nombres_cursos.append(nombre_curso)
            
            
            total_horas = sum(info_curso.get(CUR_HORAS, []))
            self.horas_totales.append(total_horas)
            
            
            evaluaciones = info_curso.get(CUR_EVALUACIONES, [])
            nota_final = 0.0
            peso_acumulado = 0.0
            
            for eva in evaluaciones:
                nota_final += eva[EVA_NOTA] * eva[EVA_PESO]
                peso_acumulado += eva[EVA_PESO]
            
            
            self.notas_finales.append(round(nota_final, 2))

    def generar_grafico_rendimiento(self):
        
        if not self.nombres_cursos:
            print("El estudiante no tiene cursos para graficar.")
            return

        plt.figure(figsize=(10, 6))
        
        
        barras = plt.bar(self.nombres_cursos, self.notas_finales, color='skyblue', edgecolor='black')
        
        
        plt.axhline(y=12, color='red', linestyle='--', linewidth=2, label='Nota Mínima Aprobatoria (12)')
        
       
        plt.title(f"Rendimiento Final por Curso - {self.estudiante.get('nombre', '')}", fontsize=14, fontweight='bold')
        plt.xlabel("Cursos", fontsize=12)
        plt.ylabel("Nota Final", fontsize=12)
        plt.ylim(0, 20.5) 
        plt.grid(axis='y', linestyle=':', alpha=0.6)
        
        
        for barra in barras:
            yval = barra.get_height()
            plt.text(barra.get_x() + barra.get_width()/2, yval + 0.3, f"{yval}", ha='center', va='bottom', fontsize=10)
            
        plt.legend(loc='upper right')
        plt.tight_layout()
        plt.show()

    def generar_grafico_dispersion(self):
        """Genera un gráfico de dispersión (Seaborn) cruzando Horas de Estudio vs Nota Final."""
        if not self.nombres_cursos:
            print("El estudiante no tiene datos suficientes para analizar la correlación.")
            return

        plt.figure(figsize=(10, 6))
        
        
        sns.scatterplot(x=self.horas_totales, y=self.notas_finales, s=150, color='darkviolet', marker='o', edgecolor='black')
        
        
        for i, curso in enumerate(self.nombres_cursos):
            plt.text(self.horas_totales[i] + 0.5, self.notas_finales[i], curso, fontsize=9, va='center')

        
        plt.title("Análisis de Correlación: Horas Invertidas vs Nota Final", fontsize=14, fontweight='bold')
        plt.xlabel("Total de Horas Invertidas en el Ciclo", fontsize=12)
        plt.ylabel("Nota Final Obtenida", fontsize=12)
        plt.xlim(left=0)
        plt.ylim(0, 20.5)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()

def EjecutarModuloGrafico(estudiante):
    """Función de interfaz para conectar este módulo POO con el menú del archivo main.py"""
    print("\n--- GENERANDO REPORTES GRÁFICOS ---")
    reporte = ReporteAcademico(estudiante)
    
    print("1. Ver Gráfico de Barras: Rendimiento por Curso (Matplotlib)")
    print("2. Ver Gráfico de Dispersión: Horas vs Nota Final (Seaborn)")
    opc = input("Seleccione el reporte gráfico que desea visualizar: ").strip()
    
    if opc == "1":
        reporte.generar_grafico_rendimiento()
    elif opc == "2":
        reporte.generar_grafico_dispersion()
    else:
        print("Opción no válida. Reporte cancelado.")