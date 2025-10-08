import threading
import queue
import time


class Pedido:
    def __init__(self, id_, tipo):
        self.id = id_
        self.tipo = tipo
        self.preparado = False

    def __repr__(self):
        return f"Pedido({self.id}, {self.tipo}, preparado={self.preparado})"


class CreadorHamburguesas:
    def crear_pedido(self, id_):
        return Pedido(id_, "Hamburguesa")


class CreadorPizzas:
    def crear_pedido(self, id_):
        return Pedido(id_, "Pizza")


class FabricaPedidos:
    #  Fábrica de creadores de pedidos (hamburguesas, pizzas, etc.)
    #  Uso:
    #    f = FabricaPedidos()
    #    creador = f.obtener_creador('hamburguesa')
    #    pedido = creador.crear_pedido(1)

    def __init__(self):
        self._mapeo = {
            'hamburguesa': CreadorHamburguesas(),
            'pizza': CreadorPizzas(),
        }

    def obtener_creador(self, tipo):
        key = tipo.lower()
        return self._mapeo.get(key)


class ServicioPedidos:
    #  Servicio de pedidos con múltiples cocineros (hilos) y una cola de pedidos.
    #  Uso:
    #    servicio = ServicioPedidos(num_cocineros=2, tiempo_preparacion=0.5)
    #    servicio.start()
    #    servicio.agregar_pedido(pedido)
    #    ...
    #    servicio.stop()  # envía sentinels para terminar
    #    servicio.join()  # espera a que terminen los cocineros

    def __init__(self, num_cocineros=2, tiempo_preparacion=0.5):
        self._cola = queue.Queue()
        self.num_cocineros = num_cocineros
        self.tiempo_preparacion = tiempo_preparacion
        self._threads = []
        self._running = False

    def agregar_pedido(self, pedido: Pedido):
        self._cola.put(pedido)

    def _cocinero(self, idx):
        while True:
            pedido = self._cola.get()
            # sentinel para terminar
            if pedido is None:
                self._cola.task_done()
                break

            print(f"[COCINERO {idx}] Preparando pedido {pedido.id} ({pedido.tipo})")
            # Simular tiempo de preparación
            time.sleep(self.tiempo_preparacion)
            pedido.preparado = True
            # Mensaje similar al del enunciado
            print(f"[COCINERO {idx}] Pedido {pedido.id} listo: {pedido.tipo} {pedido.id} preparada")
            self._cola.task_done()

        print(f"[COCINERO {idx}] Terminando.")

    def start(self):
        # Inicia los hilos de cocineros
        if self._running:
            return
        self._running = True
        for i in range(1, self.num_cocineros + 1):
            t = threading.Thread(target=self._cocinero, args=(i,))
            t.start()
            self._threads.append(t)

    def stop(self):
        # Envía sentinels para indicar a los cocineros que terminen.
        if not self._running:
            return
        # Añadimos un sentinel None por cada cocinero para que terminen
        for _ in range(self.num_cocineros):
            self._cola.put(None)
        self._running = False

    def join(self):
        # Espera a que todos los pedidos sean procesados y los hilos terminen
        self._cola.join()
        for t in self._threads:
            t.join()
        print("[SISTEMA] Todos los pedidos procesados")


if __name__ == "__main__":
    # Demo: servicio con productores (clientes) y cocineros (hilos)
    servicio = ServicioPedidos(num_cocineros=2, tiempo_preparacion=0.3)
    fabrica = FabricaPedidos()

    # Productor que simula clientes creando pedidos mixtos
    def productor(servicio: ServicioPedidos, fabrica: FabricaPedidos, duracion: float = 2.0):
        tipos = ['hamburguesa', 'pizza']
        idx = 0
        start = time.time()
        while time.time() - start < duracion:
            tipo = tipos[idx % len(tipos)]
            creador = fabrica.obtener_creador(tipo)
            pedido = creador.crear_pedido(idx)
            servicio.agregar_pedido(pedido)
            print(f"[CLIENTE] Pedido {pedido.id} de tipo {pedido.tipo} enviado")
            idx += 1
            time.sleep(0.1)  # tiempo entre clientes

    # Iniciar cocineros
    servicio.start()

    # Iniciar productor en hilo
    prod_thread = threading.Thread(target=productor, args=(servicio, fabrica, 3.0))
    prod_thread.start()

    # Esperar que el productor termine
    prod_thread.join()

    # Parar servicio (envía sentinels) y esperar a que terminen los cocineros
    servicio.stop()
    servicio.join()
