 def ver_notas(self):
        print(f"\nNotas de {self.nombre}:")
        for curso in self.cursos_inscritos:
            print(f"Curso: {curso.nombre}")
            for evaluacion in curso.evaluaciones:
                nota = evaluacion.calificaciones.get(self.carnet)
                if nota is not None:
                    print(f"  {evaluacion.tipo}: {nota}")
                else:
                    print(f"  {evaluacion.tipo}: Sin calificación")

class Instructor(Usuario):
    def _init_(self, nombre, carnet, correo):
        super()._init_(nombre, carnet, correo)
        self.cursos_impartidos = []