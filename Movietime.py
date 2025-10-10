import json
import os
from datetime import datetime

FUNCIONES_FILE = "funciones.json"
VENTAS_FILE = "ventas.json"


def cargar_datos(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as f:
            return json.load(f)
    return []

def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w") as f:
        json.dump(datos, f, indent=4)

def registrar_funcion():
    funciones = cargar_datos(FUNCIONES_FILE)
    codigo = input("Ingrese código de la función: ")
    nombre = input("Ingrese nombre de la película: ")
    hora = input("Ingrese hora (HH:MM): ")
    fecha = input("Ingrese fecha (DD/MM/AAAA): ")
    precio = 10000
    funcion = {"codigo": codigo, "nombre": nombre, "hora": hora, "fecha": fecha, "precio": precio}
    funciones.append(funcion)
    guardar_datos(FUNCIONES_FILE, funciones)
    print(" Función registrada correctamente.\n")


def listar_funciones():
    funciones = cargar_datos(FUNCIONES_FILE)
    if not funciones:
        print("No hay funciones registradas.\n")
        return
    print("Funciones disponibles:")
    for f in funciones:
        print(f"Código: {f['codigo']} | Película: {f['nombre']} | Hora: {f['hora']} | Fecha: {f['fecha']} | Precio: {f['precio']}")
    print()

def vender_boletos():
    funciones = cargar_datos(FUNCIONES_FILE)
    ventas = cargar_datos(VENTAS_FILE)
    codigo = input("Ingrese código de la función: ")
    funcion = next((f for f in funciones if f["codigo"] == codigo), None)
    if not funcion:
        print(" Función no encontrada.\n")
        return
    try:
        cantidad = int(input("Ingrese número de boletos: "))
        if cantidad <= 0 or cantidad > 200:
            print(" Número de boletos inválido.\n")
            return
    except ValueError:
        print(" Valor inválido.\n")
        return

    total = funcion["precio"] * cantidad
    print(f"Total a pagar: ${total}\n")
    ventas.append({
        "codigo": codigo,
        "pelicula": funcion["nombre"],
        "cantidad": cantidad,
        "total": total,
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
    })
    guardar_datos(VENTAS_FILE, ventas)
    print(" Venta registrada correctamente.\n")




def resumen_ventas():
    ventas = cargar_datos(VENTAS_FILE)
    if not ventas:
        print("No hay ventas registradas.\n")
        return
    
    total_boletos = sum(v["cantidad"] for v in ventas)
    total_dinero = sum(v["total"] for v in ventas)
    print(f"Boletos vendidos: {total_boletos}")
    print(f"Dinero recaudado: ${total_dinero}\n")



def menu():
    while True:
        print("=== SISTEMA DE VENTA DE BOLETOS ===")
        print("1. Registrar función")
        print("2. Listar funciones")
        print("3. Vender boletos")
        print("4. Resumen de ventas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_funcion()
        elif opcion == "2":
            listar_funciones()
        elif opcion == "3":
            vender_boletos()
        elif opcion == "4":
            resumen_ventas()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print(" Opción inválida.\n")

if __name__ == "__main__":
    menu()
