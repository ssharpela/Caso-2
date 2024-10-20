def conversion_moneda(tipo_cambio_dolar, tipo_cambio_euro, veces):
    for i in range(veces):
        print("\n-------- Conversión", i + 1, "--------")
        print('=' * 45)
        print("Opciones de conversión:")
        print('=' * 45)
        print("1. Dólares a colones")
        print("2. Euros a colones")
        print("3. Colones a dólares")
        print("4. Colones a euros")
        print('*' * 45)

        # Solicitar al usuario que elija una opción de conversión
        opcion = int(input("Seleccione el tipo de conversión (1-4): "))
        print('*' * 45)

        # Dependiendo de la opción, solicitar la cantidad y realizar la conversión
        if opcion == 1:
            dolares = float(input("Ingrese la cantidad en dólares: "))
            print('*' * 45)
            colones = dolares * tipo_cambio_dolar
            print(f"${dolares:,.2f} dólares son ₡{colones:,.2f} colones.")
            print('-' * 45)
        elif opcion == 2:
            euros = float(input("Ingrese la cantidad en euros: "))
            print('*' * 45)
            colones = euros * tipo_cambio_euro
            print(f"€{euros:,.2f} euros son ₡{colones:,.2f} colones.")
            print('-' * 45)
        elif opcion == 3:
            colones = float(input("Ingrese la cantidad en colones: "))
            print('*' * 45)
            dolares = colones / tipo_cambio_dolar
            print(f"₡{colones:,.2f} colones son ${dolares:,.2f} dólares.")
            print('-' * 45)
        elif opcion == 4:
            colones = float(input("Ingrese la cantidad en colones: "))
            print('*' * 45)
            euros = colones / tipo_cambio_euro
            print(f"₡{colones:,.2f} colones son €{euros:,.2f} euros.")
            print('-' * 45)
        else:
            print("Opción no válida. Inténtelo de nuevo.")


def main():

    tipo_cambio_dolar = 540  # Tipo de cambio fijo del dólar
    tipo_cambio_euro = 590  # Tipo de cambio fijo del euro

    # Pedir al usuario cuántas veces desea realizar la conversión
    veces = int(input("¿Cuántas conversiones desea realizar? "))

    # Llamar a la función para realizar las conversiones
    conversion_moneda(tipo_cambio_dolar, tipo_cambio_euro, veces)


# Llamada al programa principal
main()