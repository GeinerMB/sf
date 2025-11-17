## cafeteria.py

from abc import ABC, abstractmethod


# PATRÓN DECORATOR (Productos y Personalización)

#Componente Abstracto 
class Producto(ABC):
    @abstractmethod
    def obtener_descripcion(self):
        """Retorna la descripción del producto."""
        pass
    
    @abstractmethod
    def obtener_costo(self):
        """Retorna el costo del producto."""
        pass

#Componentes Concretos
class Cafe(Producto):
    def obtener_descripcion(self):
        return "Café"
    
    def obtener_costo(self):
        return 2.0

class Croissant(Producto):
    def obtener_descripcion(self):
        return "Croissant"
    
    def obtener_costo(self):
        return 3.5

class TeVerde(Producto):
    def obtener_descripcion(self):
        return "Té verde"
    
    def obtener_costo(self):
        return 1.5

#Decorador Abstracto
class IngredienteExtra(Producto, ABC):
    def __init__(self, producto_envuelto):
        self._producto_envuelto = producto_envuelto

    def obtener_descripcion(self):
        return self._producto_envuelto.obtener_descripcion()

    def obtener_costo(self):
        return self._producto_envuelto.obtener_costo()

#Decoradores Concretos
class ConLeche(IngredienteExtra):
    def obtener_descripcion(self):
        return f"{self._producto_envuelto.obtener_descripcion()} con leche"
    
    def obtener_costo(self):
        return self._producto_envuelto.obtener_costo() + 0.50

class ConCanela(IngredienteExtra):
    def obtener_descripcion(self):
        return f"{self._producto_envuelto.obtener_descripcion()} y canela"
    
    def obtener_costo(self):
        return self._producto_envuelto.obtener_costo() + 0.25

class ConRellenoChocolate(IngredienteExtra):
    def obtener_descripcion(self):
        return f"{self._producto_envuelto.obtener_descripcion()} con relleno de chocolate"
    
    def obtener_costo(self):
        return self._producto_envuelto.obtener_costo() + 1.00

class ConCrema(IngredienteExtra):
    def obtener_descripcion(self): 
        return f"{self._producto_envuelto.obtener_descripcion()} con crema"
    
    def obtener_costo(self): 
        return self._producto_envuelto.obtener_costo() + 0.75

class ConDobleEspresso(IngredienteExtra):
    def obtener_descripcion(self): 
        return f"{self._producto_envuelto.obtener_descripcion()} doble espresso"
    
    def obtener_costo(self): 
        return self._producto_envuelto.obtener_costo() + 1.50


#PATRÓN OBSERVER (Notificación de Pedidos)


#Interfaz de Observador
class Observador(ABC):
    @abstractmethod
    def actualizar(self, pedido):
        """Recibe la notificación del sujeto."""
        pass

#Observador Concreto (Cliente)
class Cliente(Observador):
    def __init__(self, nombre):
        self.nombre = nombre
        self.pedidos_listos = []

    def actualizar(self, pedido):
        # Verifica si el pedido es para este cliente antes de notificar
        if pedido.get('cliente') == self.nombre:
            print(f"[Sistema]: Se notifican los clientes cuando sus pedidos están listos.")
            print(f"[{self.nombre}]: ¡Mi pedido de {pedido['descripcion']} está listo para recoger!")
            self.pedidos_listos.append(pedido)

#Sujeto Concreto (Barista/Sistema)
class Barista:
    def __init__(self):
        # Lista de observadores (clientes esperando)
        self._observadores = [] 

    def adjuntar(self, observador):
        """Añade un observador a la lista."""
        if observador not in self._observadores:
            self._observadores.append(observador)

    def desvincular(self, observador):
        """Quita un observador de la lista."""
        self._observadores.remove(observador)

    def preparar_y_notificar(self, pedido):
        """Simula la preparación y notifica al cliente correspondiente."""
        
        # Determina si es bebida o alimento (para el output)
        is_bebida = isinstance(pedido['producto'], (Cafe, TeVerde, ConLeche, ConCanela, ConDobleEspresso, ConCrema))
        tipo = "bebida" if is_bebida else "alimento"

        print(f"[Barista]: Preparo {tipo}: {pedido['descripcion']}")
        
        # Simula la notificación a todos los observadores
        for observador in self._observadores:
            observador.actualizar(pedido)


if __name__ == "__main__":
    
    #Inicializar el sistema y clientes
    barista = Barista()
    ana = Cliente("Ana")
    carlos = Cliente("Carlos")

    #Clientes se adjuntan al sistema (Observer: Subscribirse)
    barista.adjuntar(ana)
    barista.adjuntar(carlos)

    #Creación de Pedidos (Decorator en acción)
    
    # Cliente Ana
    cafe_ana = Cafe()
    orden_ana_1 = ConCanela(ConLeche(cafe_ana)) #Café con leche y canela
    
    croissant_ana = Croissant()
    orden_ana_2 = ConRellenoChocolate(croissant_ana) #Croissant con relleno de chocolate

    # Cliente Carlos
    orden_carlos_1 = TeVerde() # Té verde
    
    cafe_carlos = Cafe()
    orden_carlos_2 = ConCrema(ConDobleEspresso(cafe_carlos)) # Café doble espresso con crema

    pedidos = [
        {"cliente": "Ana", "producto": orden_ana_1, "descripcion": orden_ana_1.obtener_descripcion()},
        {"cliente": "Ana", "producto": orden_ana_2, "descripcion": orden_ana_2.obtener_descripcion()},
        {"cliente": "Carlos", "producto": orden_carlos_1, "descripcion": orden_carlos_1.obtener_descripcion()},
        {"cliente": "Carlos", "producto": orden_carlos_2, "descripcion": orden_carlos_2.obtener_descripcion()},
    ]

    # 3. Simulación de la Cafetería
    print("=== Simulación de Cafetería ===")
    
    # Mostrar las órdenes iniciales
    print("\nCliente: Ana")
    print(f"Ordena {pedidos[0]['descripcion']}")
    print(f"Ordena {pedidos[1]['descripcion']}")
    
    print("\nCliente: Carlos")
    print(f"Ordena {pedidos[2]['descripcion']}")
    print(f"Ordena {pedidos[3]['descripcion']}")
    print("-" * 30)

    # Flujo de preparación y notificación (Observer: Notificar)
    for pedido in pedidos:
        barista.preparar_y_notificar(pedido)
    
    print("-" * 30)
    
    # Mostrar costos (Opcional, para verificar Decorator)
    print(f"Total Ana - Pedido 1 ({pedidos[0]['descripcion']}): ${pedidos[0]['producto'].obtener_costo():.2f}")
    print(f"Total Ana - Pedido 2 ({pedidos[1]['descripcion']}): ${pedidos[1]['producto'].obtener_costo():.2f}")
    print(f"Total Carlos - Pedido 1 ({pedidos[2]['descripcion']}): ${pedidos[2]['producto'].obtener_costo():.2f}")
    print(f"Total Carlos - Pedido 2 ({pedidos[3]['descripcion']}): ${pedidos[3]['producto'].obtener_costo():.2f}")