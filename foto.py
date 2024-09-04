from error import DimensionError

class Foto:
    """
    Clase que representa una foto con dimensiones de ancho y alto.

    Esta clase permite crear instancias de fotos con valores para el ancho y el alto.
    Los valores de ancho y alto se validan mediante los métodos setter para asegurarse
    de que estén dentro de los límites definidos. Si un valor no cumple con las
    restricciones (menor que 1 o mayor que el valor máximo definido por MAX), se lanza
    una excepción personalizada de tipo DimensionError.

    Atributos:
        MAX (int): El valor máximo permitido para las dimensiones (ancho y alto).

    Métodos:
        __init__(ancho, alto): Inicializa una instancia de Foto con los valores dados para
                              ancho y alto.
        ancho: Obtiene el valor del ancho de la foto.
        ancho.setter: Establece un nuevo valor para el ancho de la foto, validando que
                      esté dentro de los límites permitidos.
        alto: Obtiene el valor del alto de la foto.
        alto.setter: Establece un nuevo valor para el alto de la foto, validando que
                     esté dentro de los límites permitidos.
    """
    MAX = 1000  # Ejemplo de valor máximo

    def __init__(self, ancho, alto):
        """
        Inicializa una instancia de la clase Foto.

        Args:
            ancho (int): El valor inicial del ancho de la foto.
            alto (int): El valor inicial del alto de la foto.
        """
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        """
        Obtiene el valor del ancho de la foto.

        Returns:
            int: El valor actual del ancho de la foto.
        """
        return self._ancho

    @ancho.setter
    def ancho(self, value):
        """
        Establece un nuevo valor para el ancho de la foto.

        Si el valor proporcionado está fuera de los límites permitidos (menor que 1
        o mayor que Foto.MAX), se lanza una excepción DimensionError.

        Args:
            value (int): El nuevo valor del ancho.

        Raises:
            DimensionError: Si el valor proporcionado está fuera de los límites permitidos.
        """
        if value < 1 or value > Foto.MAX:
            raise DimensionError("Valor de ancho fuera de los límites", "ancho", Foto.MAX)
        self._ancho = value

    @property
    def alto(self):
        """
        Obtiene el valor del alto de la foto.

        Returns:
            int: El valor actual del alto de la foto.
        """
        return self._alto

    @alto.setter
    def alto(self, value):
        """
        Establece un nuevo valor para el alto de la foto.

        Si el valor proporcionado está fuera de los límites permitidos (menor que 1
        o mayor que Foto.MAX), se lanza una excepción DimensionError.

        Args:
            value (int): El nuevo valor del alto.

        Raises:
            DimensionError: Si el valor proporcionado está fuera de los límites permitidos.
        """
        if value < 1 or value > Foto.MAX:
            raise DimensionError("Valor de alto fuera de los límites", "alto", Foto.MAX)
        self._alto = value
