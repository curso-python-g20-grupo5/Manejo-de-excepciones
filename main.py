from foto import Foto
from error import DimensionError

def solicitar_valor(mensaje):
    """
    Solicita al usuario ingresar un valor entero y valida que el input sea un número.

    Args:
        mensaje (str): El mensaje que se mostrará al solicitar el valor.

    Returns:
        int: El valor entero ingresado por el usuario.

    Raises:
        ValueError: Si el usuario no ingresa un número entero válido, se vuelve a solicitar el valor.
    """
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

def main():
    """
    Función principal que ejecuta el menú interactivo de la aplicación de galería de fotos.
    
    El usuario puede crear una nueva foto, modificar sus dimensiones, ver las dimensiones actuales,
    o salir del programa. Los errores relacionados con dimensiones inválidas se capturan y se muestran
    al usuario.
    
    Las opciones incluyen:
    1. Crear una nueva foto.
    2. Modificar el ancho de la foto.
    3. Modificar el alto de la foto.
    4. Ver las dimensiones actuales de la foto.
    5. Salir del programa.
    
    Si el usuario intenta realizar acciones sin haber creado una foto, se le notifica.
    """
    foto = None  # No se ha creado una foto todavía

    while True:
        opcion = input(
            "\n--- Menú ---\n"
            "1. Crear una nueva foto\n"
            "2. Modificar el ancho\n"
            "3. Modificar el alto\n"
            "4. Ver dimensiones actuales\n"
            "5. Salir\n"
            "Selecciona una opción: "
        )

        if opcion == '1':
            try:
                foto = Foto(solicitar_valor("Ancho: "), solicitar_valor("Alto: "))
                print(f"Foto creada - Ancho: {foto.ancho}, Alto: {foto.alto}")
            except DimensionError as e:
                print(f"Error: {e}")

        elif opcion == '2' and foto:
            try:
                foto.ancho = solicitar_valor("Nuevo ancho: ")
                print(f"Ancho modificado: {foto.ancho}")
            except DimensionError as e:
                print(f"Error: {e}")

        elif opcion == '3' and foto:
            try:
                foto.alto = solicitar_valor("Nuevo alto: ")
                print(f"Alto modificado: {foto.alto}")
            except DimensionError as e:
                print(f"Error: {e}")

        elif opcion == '4' and foto:
            print(f"Dimensiones actuales - Ancho: {foto.ancho}, Alto: {foto.alto}")

        elif opcion == '5':
            print("Saliendo...")
            break

        else:
            print("Opción no válida o no hay una foto creada.")

if __name__ == "__main__":
    main()
