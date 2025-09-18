class Curso:
    def init(self, nombre, codigo, instructor):
        self.nombre = nombre
        self.codigo = codigo
        self.instructor = instructor
        self.estudiantes = []
        self.evaluaciones = []

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)

    def agregar_evaluacion(self, evaluacion):
        self.evaluaciones.append(evaluacion)