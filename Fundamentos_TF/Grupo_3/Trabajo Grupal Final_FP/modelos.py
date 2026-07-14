from datetime import date


class Curso:
    """Representa un curso con sus evaluaciones y horas de estudio."""

    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos
        self.evaluaciones = {}
        self.horas_estudio = []

    def agregar_evaluacion(self, nombre_evaluacion, fecha, nota, peso):
        """Registra una nueva evaluación."""
        self.evaluaciones[nombre_evaluacion] = {
            "fecha": fecha,
            "nota": nota,
            "peso": peso,   
        }

    def actualizar_evaluacion(self, nombre_evaluacion, nota, peso):
        """Actualiza la nota y el peso de una evaluación existente."""
        self.evaluaciones[nombre_evaluacion]["nota"] = nota
        self.evaluaciones[nombre_evaluacion]["peso"] = peso

    def peso_registrado(self):
        """Suma de los pesos de las evaluaciones ya registradas."""
        return round(sum(ev["peso"] for ev in self.evaluaciones.values()), 2)

    def promedio(self):
        """Promedio ponderado: suma de nota x peso de cada evaluación."""
        if not self.evaluaciones:
            return 0.0
        total = sum(ev["nota"] * ev["peso"] for ev in self.evaluaciones.values())
        return round(total, 2)

    def nota_necesaria(self, meta=12):
        """Nota que falta en el peso pendiente para alcanzar la meta."""
        peso_pendiente = round(1 - self.peso_registrado(), 2)
        if peso_pendiente <= 0:
            return None
        necesaria = (meta - self.promedio()) / peso_pendiente
        return round(necesaria, 2)

    def evaluaciones_ordenadas(self):
        """
        Devuelve las evaluaciones (nombre, datos) ordenadas por fecha,
        de la más antigua a la más reciente. """
        lista = list(self.evaluaciones.items())
        cantidad = len(lista)

        for i in range(cantidad):
            for j in range(cantidad - i - 1):
                fecha_actual = lista[j][1]["fecha"]
                fecha_siguiente = lista[j + 1][1]["fecha"]
                if fecha_actual > fecha_siguiente:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

        return lista

    def evolucion(self):
        """
        Compara la nota de la primera evaluación (por fecha) """
        if len(self.evaluaciones) < 2:
            return None
        ordenadas = self.evaluaciones_ordenadas()
        primera_nota = ordenadas[0][1]["nota"]
        ultima_nota = ordenadas[-1][1]["nota"]
        return round(ultima_nota - primera_nota, 2)

    def agregar_horas(self, horas, fecha=None):
        """  Agrega un registro de horas de estudio con su fecha."""
        if fecha is None:
            fecha = date.today().isoformat()
        self.horas_estudio.append({"fecha": fecha, "horas": horas})

    def actualizar_horas(self, indice, horas):
        """ Actualiza únicamente el número de horas de un registro por
        posición """
        self.horas_estudio[indice]["horas"] = horas

    def total_horas(self):
        """Suma total de horas de estudio del curso."""
        return round(sum(registro["horas"] for registro in self.horas_estudio), 2)

    def to_dict(self):
        """Convierte el curso en un diccionario serializable."""
        return {
            "nombre": self.nombre,
            "creditos": self.creditos,
            "evaluaciones": self.evaluaciones,
            "horas_estudio": self.horas_estudio,
        }


def crear_curso_desde_dict(datos):
    """ Reconstruye un curso a partir de un diccionario (leído del JSON)."""
    curso = Curso(datos["nombre"], datos["creditos"])
    curso.evaluaciones = datos["evaluaciones"]

    horas_estudio = datos["horas_estudio"]
    formato_viejo = False
    if horas_estudio:
        primer_registro = horas_estudio[0]
        if isinstance(primer_registro, (int, float)):
            formato_viejo = True

    if formato_viejo:
        horas_convertidas = []
        for horas in horas_estudio:
            horas_convertidas.append({"fecha": None, "horas": horas})
        curso.horas_estudio = horas_convertidas
    else:
        curso.horas_estudio = horas_estudio

    return curso


class Estudiante:
    """Representa a un estudiante y los cursos que administra."""

    def __init__(self, nombre, codigo, ciclo):
        self.nombre = nombre
        self.codigo = codigo
        self.ciclo = ciclo
        self.cursos = []
        self.historial = []

    def existe_curso(self, nombre):
        """Verifica si ya existe un curso con ese nombre."""
        return self.buscar_curso(nombre) is not None

    def buscar_curso(self, nombre):
        
        for curso in self.cursos:
            if curso.nombre.lower() == nombre.lower():
                return curso
        return None

    def agregar_curso(self, curso):
        
        if self.existe_curso(curso.nombre):
            return False
        self.cursos.append(curso)
        return True

    def eliminar_curso(self, curso):
        
        if curso in self.cursos:
            self.cursos.remove(curso)
            return True
        return False

    def promedio_general(self):
        
        cursos_con_notas = [c for c in self.cursos if c.evaluaciones]
        if not cursos_con_notas:
            return 0.0
        total = sum(curso.promedio() for curso in cursos_con_notas)
        return round(total / len(cursos_con_notas), 2)

    def total_horas(self):
        
        return round(sum(curso.total_horas() for curso in self.cursos), 2)

    def _mejor_y_peor_curso_actual(self):
        """ Determina el nombre del curso con mayor y menor promedio """
        cursos_con_notas = []
        for curso in self.cursos:
            if curso.evaluaciones:
                cursos_con_notas.append(curso)

        if not cursos_con_notas:
            return None, None

        mejor = cursos_con_notas[0]
        peor = cursos_con_notas[0]

        for curso in cursos_con_notas:
            if curso.promedio() > mejor.promedio():
                mejor = curso
            if curso.promedio() < peor.promedio():
                peor = curso

        return mejor.nombre, peor.nombre

    def registrar_avance_del_dia(self):
    
        hoy = date.today().isoformat()
        mejor_nombre, peor_nombre = self._mejor_y_peor_curso_actual()

        entrada = {
            "fecha": hoy,
            "promedio_general": self.promedio_general(),
            "horas_totales": self.total_horas(),
            "mejor_curso": mejor_nombre,
            "peor_curso": peor_nombre,
        }

        if self.historial and self.historial[-1]["fecha"] == hoy:
            self.historial[-1] = entrada
        else:
            self.historial.append(entrada)

    def to_dict(self):
        """ diccionario serializable."""
        return {
            "nombre": self.nombre,
            "codigo": self.codigo,
            "ciclo": self.ciclo,
            "cursos": [curso.to_dict() for curso in self.cursos],
            "historial": self.historial,
        }


def crear_estudiante_desde_dict(datos):
    """Reconstruye un estudiante a partir de un diccionario (leído del JSON)."""
    estudiante = Estudiante(datos["nombre"], datos["codigo"], datos["ciclo"])

    cursos = []
    for datos_curso in datos["cursos"]:
        cursos.append(crear_curso_desde_dict(datos_curso))
    estudiante.cursos = cursos

    if "historial" in datos:
        estudiante.historial = datos["historial"]
    else:
        estudiante.historial = []

    return estudiante
