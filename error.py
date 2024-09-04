# error.py

class DimensionError(Exception):
    """
    Excepción personalizada que se utiliza para manejar errores relacionados con dimensiones que exceden un límite permitido.
    
    Atributos:
        mensaje (str): El mensaje de error que se mostrará cuando se lance la excepción.
        dimension (int, opcional): La dimensión actual que causó el error. Por defecto es None.
        maximo (int, opcional): El valor máximo permitido para la dimensión. Por defecto es None.
    """
    
    def __init__(self, mensaje, dimension=None, maximo=None):
        """
        Inicializa una nueva instancia de DimensionError.
        
        Args:
            mensaje (str): El mensaje de error.
            dimension (int, opcional): La dimensión actual que causó el error.
            maximo (int, opcional): El valor máximo permitido para la dimensión.
        """
        # Llama al constructor de la clase base Exception para inicializar el mensaje de error
        super().__init__(mensaje)
        # Almacena la dimensión actual y el valor máximo permitido
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        """
        Devuelve una representación en cadena de la excepción.
        
        Si 'dimension' y 'maximo' no están definidos, devuelve solo el mensaje de error. 
        De lo contrario, devuelve el mensaje de error junto con los detalles sobre la dimensión y el máximo permitido.
        """
        if self.dimension is None and self.maximo is None:
            # Si no se especificaron dimension y maximo, devuelve solo el mensaje de error
            return super().__str__()

        # Devuelve el mensaje de error junto con la dimensión y el máximo permitido
        return f"{self.args[0]} - Dimension: {self.dimension}, Máximo permitido: {self.maximo}"
