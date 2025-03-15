import pickle
from datetime import datetime

# Listas para almacenar los datos
horas_sueno = []
vasos_agua = []
minutos_actividad = []
niveles_estres = []
estados_animo = []
fechas = []

# Opciones de estado de ánimo
opciones_animo = ["Muy triste", "Triste", "Neutral", "Contento", "Muy feliz"]

# Intentar cargar datos guardados previamente
try:
    with open("datos_salud.pkl", "rb") as f:
        fechas, horas_sueno, vasos_agua, minutos_actividad, niveles_estres, estados_animo = pickle.load(f)
except FileNotFoundError:
    pass  # Si el archivo no existe, se usan listas vacías


def guardar_datos():
    """Guarda los datos en un archivo para mantener persistencia."""
    with open("datos_salud.pkl", "wb") as f:
        pickle.dump((fechas, horas_sueno, vasos_agua, minutos_actividad, niveles_estres, estados_animo), f)


def registrar_datos():
    """Solicita al usuario que ingrese datos y los almacena en listas."""
    fecha = input("Ingrese la fecha (DD/MM/AAAA): ")
    
    try:
        datetime.strptime(fecha, "%d/%m/%Y")  # Validar formato de fecha
        if fecha in fechas:
            print("Ya existe un registro con esta fecha.\n")
            return
        
        fechas.append(fecha)

        try:
            horas_sueno.append(int(input("Horas de sueño: ")))
            vasos_agua.append(int(input("Vasos de agua: ")))
            minutos_actividad.append(int(input("Minutos de actividad: ")))
            niveles_estres.append(int(input("Nivel de estrés (1-10): ")))
        except ValueError:
            print("Error: Ingresa valores numéricos válidos.\n")
            fechas.pop()  # Se elimina la fecha añadida si hubo error
            return

        print("\nSeleccione su estado de ánimo:")
        for i, opcion in enumerate(opciones_animo, 1):
            print(f"{i}. {opcion}")

        while True:
            try:
                opcion = int(input("Opción (1-5): "))
                if 1 <= opcion <= 5:
                    estados_animo.append(opciones_animo[opcion - 1])
                    break
                else:
                    print("Opción fuera de rango. Intente de nuevo.")
            except ValueError:
                print("Entrada no válida. Ingrese un número entre 1 y 5.")

        print("Datos guardados correctamente.\n")
        guardar_datos()

    except ValueError:
        print("Fecha no válida. Intente de nuevo.\n")


def ver_historial():
    """Muestra el historial de registros."""
    if not fechas:
        print("No hay registros aún.\n")
        return

    print("\nHistorial de Datos:")
    for i in range(len(fechas)):
        print(f"{fechas[i]} - Sueño: {horas_sueno[i]}h, Agua: {vasos_agua[i]}, "
              f"Actividad: {minutos_actividad[i]}min, Estrés: {niveles_estres[i]}, Estado: {estados_animo[i]}")
    print()


def eliminar_registro():
    """Elimina un registro según la fecha ingresada."""
    fecha = input("Ingrese la fecha a eliminar (DD/MM/AAAA): ")
    if fecha in fechas:
        idx = fechas.index(fecha)
        del fechas[idx], horas_sueno[idx], vasos_agua[idx], minutos_actividad[idx], niveles_estres[idx], estados_animo[idx]
        print("Registro eliminado.\n")
        guardar_datos()
    else:
        print("Fecha no encontrada.\n")


def menu():
    """Muestra el menú principal y gestiona la navegación del usuario."""
    while True:
        print("\nMenú Principal")
        print("1. Registrar datos de hoy")
        print("2. Ver historial de datos")
        print("3. Eliminar un registro")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_datos()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            eliminar_registro()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

menu()
