# Tarea 3 — Sistema de Pedidos de Comida (Decisiones de diseño)

Breve explicación de las decisiones de diseño usadas en la implementación de tarea3

1) Patrón Factory
- Objetivo: separar la creación de objetos `Pedido` del resto de la lógica.
- Implementación: se definieron `CreadorHamburguesas` y `CreadorPizzas` que
  exponen el método `crear_pedido(id_)` y devuelven instancias de `Pedido`.
- Ventaja: si en el futuro se agregan más tipos (bebidas, postres), solo se
  añaden nuevas clases creadoras sin tocar la lógica de procesamiento.

1) Concurrencia: hilos y cola
- Uso de `queue.Queue` como estructura segura entre hilos (productores y
  consumidores). Los cocineros (workers) extraen pedidos de la cola y los
  procesan de forma concurrente.
- Cada cocinero es un `threading.Thread` que ejecuta un bucle, toma pedidos,
  los procesa (simulado con `time.sleep`) y marca `task_done()`.
- Terminación limpia: usamos sentinels (`None`) para indicar a cada hilo que
  debe terminar; también empleamos `queue.join()` para esperar a que todos los
  pedidos sean completados.

3) Servicio centralizado
- `ServicioPedidos` centraliza la cola, la creación y el ciclo de vida de los
  hilos (start/stop/join). Esto mantiene el `main` limpio y desacoplado.

1) Mensajes / Observabilidad
- Se usan `print()` para mostrar el estado en consola (inicio de preparación,
  pedido listo, cierre de cocineros). Para producción se recomienda reemplazar
  por `logging` con niveles y timestamps.

1) Extensibilidad y pruebas
- Es fácil añadir nuevos factories y tipos de pedido.
- Para pruebas se puede desacoplar el tiempo de preparación y
  usar mocks para acelerar tests.

Uso rápido
- Ejecutar:

```bash
python3 tarea3/factory.py
```
