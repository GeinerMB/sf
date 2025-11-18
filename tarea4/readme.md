# Cafetería — Patrones Decorator y Observer
Repo: https://github.com/GeinerMB/sf

## Cómo ejecutar:

  Desde la raíz del proyecto:
  - python3 /home/neicort/repos/sf/tarea4/cafeterya.py

En la consola: python cafeterya.py

## Resumen
- Código principal: `cafeterya.py`.
- Demuestra dos patrones:
  - Decorator: para añadir ingredientes/extras a productos (bebidas y alimentos) de forma composable.
  - Observer: para notificar a clientes cuando sus pedidos están listos.

## Justificación de diseño
- Decorator:
  - Permite extender dinámicamente la funcionalidad de productos sin modificar las clases base.
  - Cumple el principio Open/Closed: nuevas combinaciones (ej. café con leche y canela) se crean componiendo decoradores en lugar de crear múltiples subclases.
  - Evita la explosión de clases (p. ej. CafeConLecheConCanela) y facilita pruebas unitarias por componente.
- Observer:
  - Facilita notificaciones desacopladas: el Barista (sujeto) notifica a Clientes (observadores) sin conocer su implementación.
  - Escala cuando hay múltiples clientes suscritos y mejora la mantenibilidad del flujo de eventos.

## Buenas prácticas aplicadas
- Separación de responsabilidades (SRP): cada clase tiene responsabilidad única (Producto, IngredienteExtra, Observador, Barista, Cliente).
- Tipos y docstrings (cuando corresponde) para mejorar legibilidad y mantenimiento.
- Código modular: facilita tests unitarios y mantenimiento.
- Evitar duplicación de lógica: los decoradores reutilizan la API del componente envuelto.

