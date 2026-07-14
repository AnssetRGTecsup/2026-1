from modelos import crear_estudiante_desde_dict


class SistemaAcademico:
    

    def __init__(self):
        self.estudiantes = []
        self.estudiante_activo = None

    def existe_codigo(self, codigo):
       
        return self.buscar_estudiante(codigo) is not None

    def buscar_estudiante(self, codigo):
       
        for estudiante in self.estudiantes:
            if estudiante.codigo == codigo:
                return estudiante
        return None

    def agregar_estudiante(self, estudiante):
       
        if self.existe_codigo(estudiante.codigo):
            return False
        self.estudiantes.append(estudiante)
        self.estudiante_activo = estudiante
        return True

    def eliminar_estudiante(self, estudiante):
       
        if estudiante not in self.estudiantes:
            return False
        self.estudiantes.remove(estudiante)
        if self.estudiante_activo == estudiante:
            self.estudiante_activo = None
        return True

    def to_dict(self):
        
        return {
            "estudiantes": [e.to_dict() for e in self.estudiantes],
            "codigo_activo": (
                self.estudiante_activo.codigo
                if self.estudiante_activo
                else None
            ),
        }


def crear_sistema_desde_dict(datos):
   
    sistema = SistemaAcademico()

    estudiantes = []
    for datos_estudiante in datos.get("estudiantes", []):
        estudiantes.append(crear_estudiante_desde_dict(datos_estudiante))
    sistema.estudiantes = estudiantes

    codigo_activo = datos.get("codigo_activo")
    if codigo_activo:
        sistema.estudiante_activo = sistema.buscar_estudiante(codigo_activo)

    return sistema
