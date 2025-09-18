class Evaluacion:
    def init(self, tipo, fecha):
        self.tipo = tipo
        self.fecha = fecha
        self.calificaciones = {}

    def registrar_calificacion(self, estudiante, nota):
        self.calificaciones[estudiante.carnet] = nota