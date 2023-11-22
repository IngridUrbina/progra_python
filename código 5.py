class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f'Tarea "{tarea.descripcion}" agregada.')

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True
            print(f'Tarea "{self.tareas[indice].descripcion}" marcada como completada.')
        else:
            print("Índice de tarea no válido.")

    def mostrar_tareas_pendientes(self):
        print("\nTareas Pendientes:")
        for i, tarea in enumerate(self.tareas):
            if not tarea.completada:
                print(f"{i + 1}. {tarea.descripcion}")
        print("\n")

def main():
    lista_tareas = ListaTareas()

    while True:
        print("===== Gestor de Tareas =====")
        print("1. Agregar Tarea")
        print("2. Marcar Tarea como Completada")
        print("3. Mostrar Tareas Pendientes")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            descripcion_tarea = input("Ingresa la descripción de la tarea: ")
            nueva_tarea = Tarea(descripcion_tarea)
            lista_tareas.agregar_tarea(nueva_tarea)
        elif opcion == "2":
            indice_tarea = int(input("Ingresa el índice de la tarea a marcar como completada: ")) - 1
            lista_tareas.marcar_completada(indice_tarea)
        elif opcion == "3":
            lista_tareas.mostrar_tareas_pendientes()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

