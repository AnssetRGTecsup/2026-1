import os
import subprocess
import random

CARPETA = "entregas"  # carpeta donde están los .py de alumnos
SCRIPTS = ['Pregunta1.py','Pregunta2.py','Pregunta3.py','Pregunta4.py','Pregunta5.py','Pregunta6.py','Pregunta7.py']

def ejecutar(ruta, entrada):
    try:
        resultado = subprocess.run(
            ["python", ruta],
            input=entrada,
            text=True,
            capture_output=True,
            timeout=5
        )
        return resultado.stdout.strip()
    except Exception as e:
        return f"ERROR: {e}"

def generar_caso():
    n = 5
    nums = [random.randint(1, 20) for _ in range(n)]
    entrada = str(n) + "\n" + "\n".join(map(str, nums)) + "\n"
    esperado = str(sum(nums))
    return entrada, esperado

def evaluar_archivo(ruta):
    entrada, esperado = generar_caso()
    salida = ejecutar(ruta, entrada)

    try:
        return int(salida) == int(esperado)
    except:
        return False
    
def evaluar_

def main():
    resultados = []

    for archivo in os.listdir(CARPETA):
        if archivo.endswith(".py"):
            ruta = os.path.join(CARPETA, archivo)
            ok = evaluar_archivo(ruta)
            resultados.append((archivo, ok))

    print("\nRESULTADOS:")
    for nombre, estado in resultados:
        print(f"{nombre}: {'OK' if estado else 'ERROR'}")

if __name__ == "__main__":
    main()