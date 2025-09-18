class Usuario:
    def _init_(self, nombre, carnet, correo):
        self.nombre = nombre
        self.carnet = carnet
        self.correo = correo

    def mostrar_info(self):
        return f"{self.nombre} ({self.carnet}) - {self.correo}"

class Estudiante(Usuario):
    def _init_(self, nombre, carnet, correo):
        super()._init_(nombre, carnet, correo)
        self.cursos_inscritos = []

    def inscribir_curso(self, curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)