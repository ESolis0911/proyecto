# Inicialización de listas para almacenar los datos
fechas = []
horas_sueno = []
vasos_agua = []
minutos_actividad = []
niveles_estres = []
estados_animo = []

# Lista de opciones predefinidas para el estado de ánimo
opciones_animo = ["Feliz", "Triste", "Ansioso", "Relajado", "Enojado"]

# Función lambda para mostrar el menú principal
mostrar_menu = lambda: print("\nMenú Principal:\n1. Registrar datos de hoy\n2. Ver historial de datos\n3. Análisis de bienestar\n4. Recomendaciones personalizadas\n5. Eliminar un registro\n6. Salir")

# Inicio del bucle principal del programa
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-6): ")

    # Opción 1: Registrar datos de hoy
    if opcion == "1":
        # Solicitar la fecha al usuario
        fecha = input("Ingrese la fecha (DD/MM/AAAA): ")
        if fecha in fechas:
            print("Ya existe un registro para esta fecha.")
            continue

        # Función lambda para validar entradas numéricas
        validar_entrada = lambda mensaje, tipo, minimo, maximo: (
            lambda entrada: tipo(entrada) if entrada.isdigit() and minimo <= tipo(entrada) <= maximo else None
        )(input(mensaje))

        # Solicitar y validar horas de sueño
        while True:
            horas = validar_entrada("Horas de sueño (0-24): ", float, 0, 24)
            if horas is not None:
                break
            print("Entrada inválida. Por favor, ingrese un número entre 0 y 24.")

        # Solicitar y validar vasos de agua consumidos
        while True:
            agua = validar_entrada("Vasos de agua consumidos (número entero positivo): ", int, 0, 100)
            if agua is not None:
                break
            print("Entrada inválida. Por favor, ingrese un número entero positivo.")

        # Solicitar y validar minutos de actividad física
        while True:
            actividad = validar_entrada("Minutos de actividad física (número entero positivo): ", int, 0, 1440)
            if actividad is not None:
                break
            print("Entrada inválida. Por favor, ingrese un número entero positivo.")

        # Solicitar y validar nivel de estrés
        while True:
            estres = validar_entrada("Nivel de estrés (1-10): ", int, 1, 10)
            if estres is not None:
                break
            print("Entrada inválida. Por favor, ingrese un número entre 1 y 10.")

        # Mostrar opciones de estado de ánimo
        print("Seleccione su estado de ánimo:")
        for i, opcion in enumerate(opciones_animo):
            print(f"{i + 1}. {opcion}")

        # Solicitar y validar estado de ánimo
        while True:
            animo = validar_entrada("Ingrese el número correspondiente: ", int, 1, len(opciones_animo))
            if animo is not None:
                break
            print(f"Entrada inválida. Por favor, ingrese un número entre 1 y {len(opciones_animo)}.")

        # Almacenar los datos en las listas correspondientes
        fechas.append(fecha)
        horas_sueno.append(horas)
        vasos_agua.append(agua)
        minutos_actividad.append(actividad)
        niveles_estres.append(estres)
        estados_animo.append(opciones_animo[animo - 1])

        print("Registro guardado exitosamente.")

    # Opción 2: Ver historial de datos
    elif opcion == "2":
        if not fechas:
            print("No hay datos registrados.")
            continue

        # Mostrar encabezado de la tabla
        print("\nHistorial de Datos:")
        print(f"{'Fecha':<12}{'Sueño(h)':<10}{'Agua':<6}{'Actividad(min)':<15}{'Estrés':<8}{'Ánimo':<10}")
        print("-" * 60)

        # Iterar sobre los índices de las listas para mostrar los registros
        for i in range(len(fechas)):
            print(f"{fechas[i]:<12}{horas_sueno[i]:<10.1f}{vasos_agua[i]:<6}{minutos_actividad[i]:<15}{niveles_estres[i]:<8}{estados_animo[i]:<10}")

    # Opción 3: Análisis de bienestar
    elif opcion == "3":
        if not fechas:
            print("No hay datos registrados para analizar.")
            continue

        total_registros = len(fechas)
        promedio_sueno = sum(horas_sueno) / total_registros
        promedio_agua = sum(vasos_agua) / total_registros
        promedio_actividad = sum(minutos_actividad) / total_registros
        promedio_estres = sum(niveles_estres) / total_registros

        print("\nAnálisis de Bienestar:")
        print(f"Promedio de horas de sueño: {promedio_sueno:.1f}h")
        print(f"Promedio de vasos de agua consumidos: {promedio_agua:.1f}")
        print(f"Promedio de minutos de actividad física: {promedio_actividad:.1f}min")
        print(f"Promedio de nivel de estrés: {promedio_estres:.1f}/10")

        if total_registros >= 3:
            print("\nTendencias (comparando el registro más reciente con el de hace tres registros):")
            tendencias = ["Sueño", "Agua", "Actividad", "Estrés"]
            valores_actuales = [horas_sueno[-1], vasos_agua[-1], minutos_actividad[-1], niveles_estres[-1]]
            valores_pasados = [horas_sueno[-3], vasos_agua[-3], minutos_actividad[-3], niveles_estres[-3]]

            for i in range(4):
                if valores_actuales[i] > valores_pasados[i]:
                    tendencia = "↑"
                elif valores_actuales[i] < valores_pasados[i]:
                    tendencia = "↓"
                else:
                    tendencia = "→"
                print(f"{tendencias[i]}: {tendencia}")

    # Opción 4: Recomendaciones personalizadas
    elif opcion == "4":
        if not fechas:
            print("No hay datos registrados para generar recomendaciones.")
            continue

        print("\nRecomendaciones Personalizadas basadas en el registro más reciente:")
