# Mejoras Sugeridas en el Proyecto Biblioteca

Este documento resume las recomendaciones de mejora identificadas en el
código fuente, **sin modificar directamente el código**, únicamente
destacando lo indicado en los comentarios.

------------------------------------------------------------------------

## 📌 Archivo: `biblioteca.py`

### Variable poco descriptiva

-   **Situación actual:**

    ``` python
    l = Libro(titulo, autor, genero, paginas, anio)
    ```

-   **Mejora sugerida:**

    ``` python
    libro = Libro(titulo, autor, genero, paginas, anio)  # nombre más descriptivo
    ```

------------------------------------------------------------------------

### Método muy largo (`generar_reporte`)

-   **Situación actual:**

    ``` python
    def generar_reporte(self):
        total = len(self.libros)
        antiguos = 0
        disponibles = 0
        popularidad_total = 0

        for l in self.libros:
            l.imprimir_datos()
            if l.es_antiguo():
                antiguos += 1
            if l.disponible:
                disponibles += 1
            popularidad_total += l.calcular_popularidad()

        print("\n📖 REPORTE BIBLIOTECA 📖")
        print(f"Total libros: {total}")
        print(f"Disponibles: {disponibles}")
        print(f"Antiguos: {antiguos}")
        print(f"Promedio de popularidad: {popularidad_total / total if total > 0 else 0}")
    ```

-   **Mejora sugerida (dividido en métodos auxiliares):**

    ``` python
    def contar_antiguos(self):
        return sum(1 for libro in self.libros if libro.es_antiguo())

    def contar_disponibles(self):
        return sum(1 for libro in self.libros if libro.disponible)

    def calcular_popularidad_promedio(self):
        if not self.libros:
            return 0
        total = sum(libro.calcular_popularidad() for libro in self.libros)
        return total / len(self.libros)

    def generar_reporte(self):
        for libro in self.libros:
            libro.imprimir_datos()

        print("\n📖 REPORTE BIBLIOTECA 📖")
        print(f"Total libros: {len(self.libros)}")
        print(f"Disponibles: {self.contar_disponibles()}")
        print(f"Antiguos: {self.contar_antiguos()}")
        print(f"Promedio de popularidad: {self.calcular_popularidad_promedio()}")
    ```

------------------------------------------------------------------------

## 📌 Archivo: `libro.py`

### Limitación de opciones en `calcular_popularidad`

-   **Situación actual:**

    ``` python
    if self.genero == 'novela':
        base = 50
        extra = self.paginas / 10
    elif self.genero == 'ciencia':
        base = 70
        extra = self.paginas / 5
    elif self.genero == 'historia':
        base = 40
        extra = self.paginas / 8
    else:
        base = 10
        extra = 0
    ```

-   **Mejora sugerida (usando match-case):**

    ``` python
    match self.genero:
        case 'novela':
            base, extra = 50, self.paginas / 10
        case 'ciencia':
            base, extra = 70, self.paginas / 5
        case 'historia':
            base, extra = 40, self.paginas / 8
        case _:
            base, extra = 10, 0
    ```

------------------------------------------------------------------------

### Método `imprimir_datos`

-   **Situación actual:**

    ``` python
    def imprimir_datos(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Género: {self.genero}")
        print(f"Páginas: {self.paginas}")
        print(f"Año: {self.anio_publicacion}")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")
        print(f"Popularidad: {self.calcular_popularidad()}")
        print(f"Es antiguo: {'Sí' if self.es_antiguo() else 'No'}")
        print("------------------------")
    ```

-   **Mejora sugerida (retornar diccionario):**

    ``` python
    def obtener_datos(self):
        return {
            "Título": self.titulo,
            "Autor": self.autor,
            "Género": self.genero,
            "Páginas": self.paginas,
            "Año": self.anio_publicacion,
            "Disponible": self.disponible,
            "Popularidad": self.calcular_popularidad(),
            "Es antiguo": self.es_antiguo()
        }
    ```

------------------------------------------------------------------------

## 📌 Archivo: `main.py`

### Variable poco descriptiva (`b`)

-   **Situación actual:**

    ``` python
    b = Biblioteca()
    ```

-   **Mejora sugerida:**

    ``` python
    biblioteca = Biblioteca()  # nombre más descriptivo
    ```

------------------------------------------------------------------------

### Uso de `if-elif` para menú

-   **Situación actual:**

    ``` python
    if opcion == "1":
        biblioteca.agregar_libro()
    elif opcion == "2":
        biblioteca.generar_reporte()
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")
    ```

-   **Mejora sugerida (usando match-case):**

    ``` python
    match opcion:
        case "1":
            biblioteca.agregar_libro()
        case "2":
            biblioteca.generar_reporte()
        case "3":
            print("Saliendo...")
            break
        case _:
            print("Opción inválida.")
    ```

------------------------------------------------------------------------

## ✅ Conclusión

Las mejoras sugeridas buscan:\
- Hacer el código más **legible** y **descriptivo**.\
- Reducir la longitud de métodos muy cargados.\
- Facilitar la **escalabilidad futura** (ej. migrar de consola a
interfaz gráfica o web).
