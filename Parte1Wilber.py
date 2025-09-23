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
        print("8. Salir")

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
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except Exception as e:
            print(f"Error: {e}")

# Ejecutar menú
if __name__ == "__main__":
    menu()