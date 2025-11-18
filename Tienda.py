from collections import Counter, OrderedDict

# ---  Diccionario con los datos  ---
datos_clientes = {
    "compras": [
        "Luis", "Ana", "Luis", "Carlos", "Marta", "Ana",
        "Sofía", "Elena", "Luis", "Carlos"
    ],
    "registrados": [
        "Ana", "Carlos", "Marta", "Elena"
    ]
}

# --- Acceso a las listas dentro del diccionario ---
compras = datos_clientes["compras"]
registrados = datos_clientes["registrados"]

# 1. Filtrar clientes nuevos (no registrados)
compras_set = set(compras)
registrados_set = set(registrados)
nuevos_clientes = compras_set - registrados_set  # Diferencia de conjuntos

# 2. Eliminar duplicados y mantener orden
clientes_unicos = list(OrderedDict.fromkeys(compras))  # Elimina duplicados y mantiene el orden

# 3. Contar cuántas veces se repite cada nombre
contador_compras = Counter(compras)

# 4. Crear un resumen personalizado (solo los que compraron más de 1 vez)
resumen_frecuentes = {
    cliente: f"Ha comprado {cantidad} veces"
    for cliente, cantidad in contador_compras.items() if cantidad > 1
}

# --- 5. Formato final de salida ---
print("=== CLIENTES NUEVOS (no registrados) ===")
for cliente in nuevos_clientes:
    print(f"- {cliente}")

print("\n=== LISTA DE CLIENTES ÚNICOS ===")
for cliente in clientes_unicos:
    print(f"- {cliente}")

print("\n=== CLIENTES FRECUENTES (más de 1 compra) ===")
for cliente, mensaje in resumen_frecuentes.items():
    print(f"- {cliente}: {mensaje}")