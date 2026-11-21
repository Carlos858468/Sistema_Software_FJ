from pathlib import Path

def ejecutar_pruebas():
    archivo = Path(__file__).with_name("logs.txt")

    operaciones = []
    exitosas = 0
    errores_controlados = 0
    no_completadas = 0

    print("PRUEBAS DEL SISTEMA SOFTWARE FJ")

    if not archivo.exists():
        print("No existe logs.txt. Primero ejecute main.py.")
        return

    with archivo.open("r", encoding="utf-8") as log:
        for linea in log:
            if "OPERACION_V2|" not in linea:
                continue

            registro = linea.split("OPERACION_V2|", 1)[1].strip()
            partes = registro.split("|", 2)

            if len(partes) < 2:
                continue

            nombre = partes[0].strip()
            estado = partes[1].strip()

            # Solo se cuentan acciones del sistema, no consultas.
            if estado == "EXITOSA":
                exitosas += 1
            elif estado == "ERROR_CONTROLADO":
                errores_controlados += 1
            elif estado == "NO_COMPLETADA":
                no_completadas += 1
            else:
                continue

            operaciones.append((nombre, estado))

    print("OPERACIONES ENCONTRADAS:")
    if not operaciones:
        print("Todavía no hay operaciones nuevas registradas.")

    for numero, (nombre, estado) in enumerate(operaciones, 1):
        print(f"{numero}. {nombre} - {estado}")

    total = exitosas + errores_controlados

    print("RESULTADOS")
    print("Operaciones completadas o con error:", total)
    print("Operaciones exitosas:", exitosas)
    print("Errores controlados:", errores_controlados)
    print("Acciones no completadas:", no_completadas)

    if total >= 10 and exitosas > 0 and errores_controlados > 0:
        print("PRUEBAS APROBADAS.")
        print("Hay al menos 10 acciones registradas, con éxitos y errores controlados.")
    else:
        print("PRUEBAS INCOMPLETAS.")
        print("Se requieren al menos 10 acciones completadas o fallidas,")
        print("incluyendo por lo menos una exitosa y un error controlado.")

    print("Las consultas no se cuentan como operaciones.")
    print("Los registros antiguos se ignoran; solo se cuentan los nuevos registros V2.")

if __name__ == "__main__":
    ejecutar_pruebas()
