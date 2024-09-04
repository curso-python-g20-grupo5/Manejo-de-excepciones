# Galería de Fotos - Manejo de Excepciones

Este repositorio contiene una implementación de una aplicación de galería de fotos que incluye control de excepciones personalizado para manejar errores relacionados con dimensiones inválidas de imágenes. El proyecto sigue los requisitos planteados por el desafío de manejo de excepciones.

## Descripción

Esta aplicación permite crear, modificar y visualizar las dimensiones (ancho y alto) de una foto. Sin embargo, existe un control de errores que evita asignar dimensiones fuera de los límites permitidos. Si se intenta modificar el ancho o el alto de una foto con un valor menor a 1 o mayor al valor máximo permitido (definido por la clase `Foto`), se lanza una excepción personalizada llamada `DimensionError`.

## Archivos Principales

- **`error.py`**: Contiene la definición de la excepción personalizada `DimensionError`. Esta excepción se utiliza para controlar los errores relacionados con dimensiones que exceden los límites establecidos.
- **`foto.py`**: Define la clase `Foto` que permite crear una foto con dimensiones específicas (ancho y alto). Contiene validaciones en los métodos setter para garantizar que las dimensiones estén dentro del rango permitido.
- **`main.py`**: Es el archivo principal que ejecuta la aplicación. Ofrece un menú interactivo para crear fotos, modificar sus dimensiones y visualizar las dimensiones actuales. También captura y maneja las excepciones lanzadas por `DimensionError`.

## Funcionalidades

1. **Crear una nueva foto**: El usuario puede crear una foto especificando el ancho y el alto. Si se introducen valores fuera de los límites permitidos, se lanza una excepción `DimensionError`.
   
2. **Modificar el ancho o el alto**: El usuario puede modificar las dimensiones de la foto. Si los valores ingresados no son válidos (menores a 1 o mayores al máximo permitido), la aplicación captura la excepción y muestra un mensaje de error detallado.

3. **Ver las dimensiones actuales**: El usuario puede consultar las dimensiones actuales de la foto creada.

4. **Salir de la aplicación**: El usuario puede finalizar la ejecución de la aplicación.

## Requisitos del Desafío

El desafío solicita lo siguiente:

1. **Excepción personalizada**:
   - Crear la excepción `DimensionError` en el archivo `error.py`, que debe recibir un mensaje, una dimensión (ancho o alto) y un valor máximo permitido.
   - Sobrecargar el método `__str__` para devolver una cadena detallada con el mensaje de error, la dimensión y el valor máximo permitido, si se proporcionan.

2. **Validación en `foto.py`**:
   - Modificar los métodos setter de la clase `Foto` para lanzar una excepción `DimensionError` cuando el valor de ancho o alto esté fuera de los límites (menor a 1 o mayor al máximo permitido).

## Ejecución

Para ejecutar la aplicación, sigue estos pasos:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/galeria-fotos-excepciones.git
   cd galeria-fotos-excepciones
   ```

2. Ejecuta el archivo principal `main.py`:
   ```bash
   python main.py
   ```

3. Interactúa con el menú de opciones para crear fotos, modificar dimensiones y ver el estado actual.

## Ejemplo de Uso

### Caso: Crear una foto con dimensiones válidas

```
--- Menú ---
1. Crear una nueva foto
2. Modificar el ancho
3. Modificar el alto
4. Ver dimensiones actuales
5. Salir
Selecciona una opción: 1
Ancho: 500
Alto: 300
Foto creada - Ancho: 500, Alto: 300
```

### Caso: Error al modificar el ancho con un valor inválido

```
--- Menú ---
1. Crear una nueva foto
2. Modificar el ancho
3. Modificar el alto
4. Ver dimensiones actuales
5. Salir
Selecciona una opción: 2
Nuevo ancho: 1200
Error: Valor de ancho fuera de los límites - Dimension: ancho, Máximo permitido: 1000
```
## Contribuciones

- [Rosa Rubio](https://github.com/PaulinaRubioP)
- [Valery Maragaño](https://github.com/Valyxp)
- [Marco Alvarado](https://github.com/7pixel-cl)
- [Esteban Hernández](https://github.com/stivhc)
