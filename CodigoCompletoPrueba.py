# Clases base
class Usuario:
    def __init__(self, nombre, carnet, correo):
        self.nombre = nombre
        self.carnet = carnet
        self.correo = correo

    def mostrar_info(self):
        return f"{self.nombre} ({self.carnet}) - {self.correo}"


class Estudiante(Usuario):
    def __init__(self, nombre, carnet, correo):
        super().__init__(nombre, carnet, correo)
        self.cursos_inscritos = []
        self.reportes = []

    def inscribir_curso(self, curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)

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

    def ver_reportes(self):
        print(f"\nReportes de bajo rendimiento para {self.nombre}:")
        if not self.reportes:
            print("  No hay reportes registrados.")
        for reporte in self.reportes:
            print(f"  Curso: {reporte.curso.nombre}, Evaluación: {reporte.evaluacion.tipo}, Nota: {reporte.nota}")
            print(f"    Observación: {reporte.observacion}")


class Instructor(Usuario):
    def __init__(self, nombre, carnet, correo):
        super().__init__(nombre, carnet, correo)
        self.cursos_impartidos = []

    def crear_curso(self, nombre, codigo):
        curso = Curso(nombre, codigo, self)
        self.cursos_impartidos.append(curso)
        return curso

    def generar_reporte(self, estudiante, curso, evaluacion, nota, observacion):
        reporte = Reporte(curso, evaluacion, nota, observacion)
        estudiante.reportes.append(reporte)


class Curso:
    def __init__(self, nombre, codigo, instructor):
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


class Evaluacion:
    def __init__(self, tipo, fecha):
        self.tipo = tipo
        self.fecha = fecha
        self.calificaciones = {}

    def registrar_calificacion(self, estudiante, nota):
        self.calificaciones[estudiante.carnet] = nota


class Reporte:
    def __init__(self, curso, evaluacion, nota, observacion):
        self.curso = curso
        self.evaluacion = evaluacion
        self.nota = nota
        self.observacion = observacion


class GestorPlataforma:
    def __init__(self):
        self.usuarios = {}
        self.cursos = {}

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.carnet] = usuario

    def registrar_curso(self, curso):
        self.cursos[curso.codigo] = curso

    def buscar_usuario(self, carnet):
        return self.usuarios.get(carnet)

    def buscar_curso(self, codigo):
        return self.cursos.get(codigo)

# Menú interactivo
def menu():
    gestor = GestorPlataforma()

    while True:
        print("\nMENÚ PRINCIPAL")
        print("1. Registrar estudiante")
        print("2. Registrar instructor")
        print("3. Crear curso")
        print("4. Inscribir estudiante en curso")
        print("5. Crear evaluación")
        print("6. Registrar calificación")
        print("7. Ver notas de estudiante")
        print("8. Registrar reporte de bajo rendimiento")
        print("9. Ver reportes de estudiante")
        print("10. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre del estudiante: ")
                carnet = int(input("Carnet: "))
                correo = input("Correo: ")
                estudiante = Estudiante(nombre, carnet, correo)
                gestor.registrar_usuario(estudiante)
                print("Estudiante registrado.")

            elif opcion == "2":
                nombre = input("Nombre del instructor: ")
                carnet = int(input("Carnet: "))
                correo = input("Correo: ")
                instructor = Instructor(nombre, carnet, correo)
                gestor.registrar_usuario(instructor)
                print("Instructor registrado.")

            elif opcion == "3":
                carnet = int(input("Carnet del instructor: "))
                instructor = gestor.buscar_usuario(carnet)
                if isinstance(instructor, Instructor):
                    nombre = input("Nombre del curso: ")
                    codigo = input("Código del curso: ")
                    curso = instructor.crear_curso(nombre, codigo)
                    gestor.registrar_curso(curso)
                    print("Curso creado.")
                else:
                    print("Instructor no encontrado.")

            elif opcion == "4":
                carnet = int(input("Carnet del estudiante: "))
                estudiante = gestor.buscar_usuario(carnet)
                codigo = input("Código del curso: ")
                curso = gestor.buscar_curso(codigo)
                if isinstance(estudiante, Estudiante) and curso:
                    curso.agregar_estudiante(estudiante)
                    estudiante.inscribir_curso(curso)
                    print("Estudiante inscrito.")
                else:
                    print("Datos inválidos.")

            elif opcion == "5":
                codigo = input("Código del curso: ")
                curso = gestor.buscar_curso(codigo)
                if curso:
                    tipo = input("Tipo de evaluación (Examen/Tarea): ")
                    fecha = input("Fecha: ")
                    evaluacion = Evaluacion(tipo, fecha)
                    curso.agregar_evaluacion(evaluacion)
                    print("Evaluación creada.")
                else:
                    print("Curso no encontrado.")

            elif opcion == "6":
                codigo = input("Código del curso: ")
                curso = gestor.buscar_curso(codigo)
                if curso and curso.evaluaciones:
                    tipo = input("Tipo de evaluación: ")
                    evaluacion = next((ev for ev in curso.evaluaciones if ev.tipo == tipo), None)
                    if evaluacion:
                        carnet = int(input("Carnet del estudiante: "))
                        estudiante = gestor.buscar_usuario(carnet)
                        nota = float(input("Nota: "))
                        evaluacion.registrar_calificacion(estudiante, nota)
                        print("Calificación registrada.")
                    else:
                        print("Evaluación no encontrada.")
                else:
                    print("Curso o evaluaciones no válidas.")

            elif opcion == "7":
                carnet = int(input("Carnet del estudiante: "))
                estudiante = gestor.buscar_usuario(carnet)
                if isinstance(estudiante, Estudiante):
                    estudiante.ver_notas()
                else:
                    print("Estudiante no encontrado.")

            elif opcion == "8":
                carnet_instructor = int(input("Carnet del instructor: "))
                instructor = gestor.buscar_usuario(carnet_instructor)
                if isinstance(instructor, Instructor):
                    carnet_estudiante = int(input("Carnet del estudiante: "))
                    estudiante = gestor.buscar_usuario(carnet_estudiante)
                    codigo = input("Código del curso: ")
                    curso = gestor.buscar_curso(codigo)
                    tipo = input("Tipo de evaluación: ")
                    evaluacion = next((ev for ev in curso.evaluaciones if ev.tipo == tipo), None)
                    if isinstance(estudiante, Estudiante) and curso and evaluacion:
                        nota = evaluacion.calificaciones.get(estudiante.carnet)
                        observacion = input("Observación del instructor: ")
                        instructor.generar_reporte(estudiante, curso, evaluacion, nota, observacion)
                        print("Reporte registrado.")
                    else:
                        print("Datos inválidos.")
                else:
                    print("Instructor no válido.")

            elif opcion == "9":
                carnet = int(input("Carnet del estudiante: "))
                estudiante = gestor.buscar_usuario(carnet)
                if isinstance(estudiante, Estudiante):
                    estudiante.ver_reportes()
                else:
                    print("Estudiante no encontrado.")

            elif opcion == "10":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except Exception as e:
            print(f"Error: {e}")

# Ejecutar menú
if __name__ == "__main__":
    menu()