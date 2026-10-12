from barrio import Barrio
from habitacion import Habitacion
from vivienda import Vivienda

# 1. Instanciar las habitaciones
hab1 = Habitacion("Cocina", 12.0)
hab2 = Habitacion("Dormitorio Principal", 15.0)
hab3 = Habitacion("Comedor", 20.0)

# 2. Instanciar las viviendas
casa1 = Vivienda("San Martin", 123, "A", 1, 200.0)
casa2 = Vivienda("Belgrano", 456, "A", 2, 150.0)

# 3. Asociar habitaciones a las casas
casa1.habitacion.append(hab1)
casa1.habitacion.append(hab2)
casa2.habitacion.append(hab3)

# 4. Instanciar el Barrio
mi_barrio = Barrio("Los Pinos", "Constructora SA")

# 5. Asociar las casas al barrio
mi_barrio.vivienda.append(casa1)
mi_barrio.vivienda.append(casa2)

# 6. Ejecutar y mostrar
print("--- RESULTADOS DEL BARRIO ---")
print(f"Superficie total de terreno: {mi_barrio.getSuperficieTotalTerreno()}")
print(
    f"Superficie de terreno en Manzana A: {mi_barrio.getSuperficieTotalTerrenoXManzana('A')}"
)
print(f"Superficie total cubierta del barrio: {mi_barrio.getSuperficieTotalCubierta()}")
