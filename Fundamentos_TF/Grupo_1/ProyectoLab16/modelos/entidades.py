

class Evaluacion:
    

    def __init__(self, nombre, fecha, nota, peso):
        self.nombre = nombre
        self.fecha = fecha      
        self.nota = nota        
        self.peso = peso        

    def aporte(self):
        
        return self.nota * self.peso

    def fecha_texto(self):
        return self.fecha.strftime("%d/%m/%Y")

    def __str__(self):
        return f"{self.nombre} | Nota: {self.nota} | Peso: {self.peso} | Fecha: {self.fecha_texto()}"


class HabitoEstudio:
    

    def __init__(self, fecha, horas):
        self.fecha = fecha      
        self.horas = horas      

    def fecha_texto(self):
        return self.fecha.strftime("%d/%m/%Y")

    def __str__(self):
        return f"{self.horas} h el {self.fecha_texto()}"


class Curso:
    

    NOTA_MINIMA_APROBATORIA = 12

    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos
        self.evaluaciones = []        
        self.habitos_estudio = []    

    def agregar_evaluacion(self, evaluacion):
        self.evaluaciones.append(evaluacion)

    def agregar_habito_estudio(self, habito):
        self.habitos_estudio.append(habito)

    def calcular_nota_final(self):
        nota_final = 0.0
        for evaluacion in self.evaluaciones:
            nota_final += evaluacion.aporte()
        return round(nota_final, 2)

    def calcular_horas_totales(self):
        total = 0.0
        for habito in self.habitos_estudio:
            total += habito.horas
        return total

    def esta_aprobado(self):
        return self.calcular_nota_final() >= Curso.NOTA_MINIMA_APROBATORIA

    def resumen(self):
        
        return (self.calcular_nota_final(), self.calcular_horas_totales(), self.esta_aprobado())


class Estudiante:
   

    def __init__(self, nombre, codigo, ciclo):
        self.nombre = nombre
        self.codigo = codigo
        self.ciclo = ciclo
        self.cursos = []   

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def eliminar_curso(self, curso):
        if curso in self.cursos:
            self.cursos.remove(curso)

    def buscar_curso(self, nombre_curso):
        for curso in self.cursos:
            if curso.nombre.lower() == nombre_curso.strip().lower():
                return curso
        return None

    def tiene_cursos(self):
        return len(self.cursos) > 0
