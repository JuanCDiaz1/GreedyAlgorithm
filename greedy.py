import numpy as np

# Costos de transporte desde las ubicaciones potenciales a los clientes
costos = np.array([[10, 20, 25, 12, 18, 22, 17, 15],
                   [15, 18, 20, 10, 14, 20, 12, 18],
                   [12, 22, 10, 15, 25, 15, 20, 22],
                   [20, 15, 18, 15, 12, 20, 10, 14],
                   [18, 12, 22, 20, 15, 10, 25, 20]])

# Función para encontrar la mejor ubicación en cada iteración
def encontrar_mejor_ubicacion(costos, ubicaciones_seleccionadas):
    mejor_ubicacion = None
    mejor_costo_total = float('inf')

    for ubicacion in range(costos.shape[0]):
        if ubicacion not in ubicaciones_seleccionadas:
            costo_total = np.sum(costos[ubicacion])
            if costo_total < mejor_costo_total:
                mejor_ubicacion = ubicacion
                mejor_costo_total = costo_total

    return mejor_ubicacion, mejor_costo_total

# Función para resolver el problema de ubicación de instalaciones utilizando el método Greedy
def resolver_problema_ubicacion_instalaciones(costos, num_ubicaciones):
    ubicaciones_seleccionadas = []
    costo_total = 0

    for _ in range(num_ubicaciones):
        mejor_ubicacion, mejor_costo = encontrar_mejor_ubicacion(costos, ubicaciones_seleccionadas)
        ubicaciones_seleccionadas.append(mejor_ubicacion)
        costo_total += mejor_costo

    return ubicaciones_seleccionadas, costo_total

# Resolución del ejemplo
num_ubicaciones = 3
ubicaciones_optimas, costo_total_optimo = resolver_problema_ubicacion_instalaciones(costos, num_ubicaciones)

# Mostrar las ubicaciones óptimas seleccionadas
print("Ubicaciones óptimas seleccionadas:")
for ubicacion in ubicaciones_optimas:
    print(chr(65 + ubicacion))  # Convertir el índice a letra (A, B, C, ...)

# Mostrar el costo total óptimo
print("Costo Total Óptimo:", costo_total_optimo)
