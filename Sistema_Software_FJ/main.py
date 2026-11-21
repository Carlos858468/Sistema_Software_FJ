import logging
from clientes import Cliente
from servicios import (
    ReservaSalas,
    AlquilerEquipos,
    AsesoriaEspecializada
)
from reservas import Reserva

# Configuración del registro de eventos y errores
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Sistema principal
class SistemaSoftwareFJ:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

sistema = SistemaSoftwareFJ()


# Manejo de operaciones y excepciones
def ejecutar_operacion(nombre, funcion):

    try:
        resultado = funcion()

    except Exception as error:
        print("Error controlado:", error)
        logging.exception(
            "OPERACION_V2|%s|ERROR_CONTROLADO|%s",
            nombre,
            error
        )

    else:
        # Las consultas se registran aparte y no cuentan como operaciones completas.
        if nombre.startswith("Consultar"):
            logging.info("CONSULTA_V2|%s", nombre)

        elif resultado is None:
            # La función terminó, pero no realizó la acción solicitada.
            logging.warning("OPERACION_V2|%s|NO_COMPLETADA", nombre)

        else:
            print(resultado)
            logging.info("OPERACION_V2|%s|EXITOSA", nombre)

    finally:
        print("Operación finalizada.")

# Generar códigos automáticamente
def generar_codigo(prefijo, lista):
    return f"{prefijo}{len(lista) + 1:03d}"

# Solicitar números
def pedir_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero <= 0:
                print("Ingrese un número mayor que cero.")
                continue

            return numero

        except ValueError:
            print("Debe ingresar un número válido.")

# Registrar cliente
def registrar_cliente():

    print("REGISTRAR CLIENTE")

    nombre = input("Nombre completo: ")
    correo = input("Correo electrónico: ")
    telefono = input("Teléfono: ")

    codigo = generar_codigo("C", sistema.clientes)

    cliente = Cliente(codigo, nombre, correo, telefono)

    sistema.clientes.append((codigo, cliente))

    return f"Cliente registrado correctamente. Código: {codigo}"

# Consultar clientes
def consultar_clientes():

    print("CLIENTES REGISTRADOS")

    if not sistema.clientes:
        print("No hay clientes registrados.")
        return

    for codigo, cliente in sistema.clientes:
        print(codigo, "-", cliente)

# Crear servicio
def crear_servicio():

    print("CREAR SERVICIO")
    print("1. Reserva de salas")
    print("2. Alquiler de equipos")
    print("3. Asesoría especializada")

    opcion = pedir_numero("Seleccione el tipo de servicio: ")

    if opcion not in (1, 2, 3):
        print("Opción no válida.")
        return

    nombre = input("Nombre del servicio: ")

    try:
        tarifa = float(input("Tarifa en pesos:"))
    except ValueError as error:
        raise ValueError("La tarifa debe ser numérica.") from error

    codigo = generar_codigo("S", sistema.servicios)

    if opcion == 1:
        servicio = ReservaSalas(codigo, nombre, tarifa)

    elif opcion == 2:
        servicio = AlquilerEquipos(codigo, nombre, tarifa)

    else:
        servicio = AsesoriaEspecializada(codigo, nombre, tarifa)

    sistema.servicios.append((codigo, servicio))

    return f"Servicio creado correctamente. Código: {codigo}"

# Consultar servicios
def consultar_servicios():

    print("SERVICIOS DISPONIBLES")

    if not sistema.servicios:
        print("No hay servicios registrados.")
        return

    for codigo, servicio in sistema.servicios:
        print(codigo, "-", servicio.describir())

# Buscar cliente
def buscar_cliente():

    consultar_clientes()

    if not sistema.clientes:
        return None

    codigo = input("Ingrese el código del cliente: ").upper()

    for identificador, cliente in sistema.clientes:
        if identificador == codigo:
            return cliente

    print("Cliente no encontrado.")
    return None

# Buscar servicio
def buscar_servicio():

    consultar_servicios()

    if not sistema.servicios:
        return None

    codigo = input("Ingrese el código del servicio: ").upper()

    for identificador, servicio in sistema.servicios:
        if identificador == codigo:
            return servicio

    print("Servicio no encontrado.")
    return None

# Crear reserva
def crear_reserva():

    print("CREAR RESERVA")

    cliente = buscar_cliente()

    if cliente is None:
        return

    servicio = buscar_servicio()

    if servicio is None:
        return

    cantidad = pedir_numero("Ingrese la cantidad de horas o unidades: ")

    codigo = generar_codigo("R", sistema.reservas)

    reserva = Reserva(
        codigo,
        cliente,
        servicio,
        cantidad
    )

    sistema.reservas.append((codigo, reserva))

    return f"Reserva creada correctamente. Código: {codigo}"

# Consultar reservas
def consultar_reservas():

    print("RESERVAS REGISTRADAS")

    if not sistema.reservas:
        print("No hay reservas registradas.")
        return

    for codigo, reserva in sistema.reservas:
        print(codigo, "-", reserva)

# Buscar reserva
def buscar_reserva():

    consultar_reservas()

    if not sistema.reservas:
        return None

    codigo = input("Ingrese el código de la reserva: ").upper()

    for identificador, reserva in sistema.reservas:
        if identificador == codigo:
            return reserva

    print("Reserva no encontrada.")
    return None

# Confirmar reserva
def confirmar_reserva():

    reserva = buscar_reserva()

    if reserva is not None:
        return reserva.confirmar()

# Procesar reserva
def procesar_reserva():

    reserva = buscar_reserva()

    if reserva is not None:
        resultado = reserva.procesar()

        if resultado is not None:
            return f"Costo total: ${resultado:,.0f}"

# Cancelar reserva
def cancelar_reserva():

    reserva = buscar_reserva()

    if reserva is not None:
        return reserva.cancelar()

# Menú principal
def mostrar_menu():

    print("SISTEMA SOFTWARE FJ")
    print("1. Registrar cliente")
    print("2. Consultar clientes")
    print("3. Crear servicio")
    print("4. Consultar servicios")
    print("5. Crear reserva")
    print("6. Confirmar reserva")
    print("7. Procesar reserva")
    print("8. Cancelar reserva")
    print("9. Consultar reservas")
    print("0. Salir")
   
# Ejecutar el sistema
def menu_principal():

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        acciones = {
            "1": ("Registrar cliente", registrar_cliente),
            "2": ("Consultar clientes", consultar_clientes),
            "3": ("Crear servicio", crear_servicio),
            "4": ("Consultar servicios", consultar_servicios),
            "5": ("Crear reserva", crear_reserva),
            "6": ("Confirmar reserva", confirmar_reserva),
            "7": ("Procesar reserva", procesar_reserva),
            "8": ("Cancelar reserva", cancelar_reserva),
            "9": ("Consultar reservas", consultar_reservas)
        }

        if opcion == "0":
            print("Gracias por utilizar Software FJ.")
            logging.info("Sistema cerrado.")
            break

        elif opcion in acciones:
            nombre, funcion = acciones[opcion]

            ejecutar_operacion(nombre, funcion)

        else:
            print("Opción incorrecta. Intente nuevamente.")

# Inicio del programa
if __name__ == "__main__":

    try:
        menu_principal()

    except KeyboardInterrupt:
        print("Programa interrumpido.")

    except Exception:
        logging.exception("Error inesperado.")
        print("Ocurrió un error. Consulte logs.txt.")

    finally:
        logging.info("Fin de la ejecución.")
