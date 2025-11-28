# Laboratorio #5

Realice este laboratorio de forma individual. Suba las respuestas al enlace de Mediación.

---

## Selección Única (20%)
Marque con X la opción correcta. Cada respuesta vale 2%.

1. Una plataforma de aprendizaje en línea quiere permitir que los estudiantes trabajen en grupos donde cada grupo contiene estudiantes, tareas y subgrupos. ¿Qué patrón usaría para manejar esta estructura jerárquica?  
   - a) Decorator  
   - X) Composite 
   - c) Bridge  
   - d) Mediator

2. Un sistema de mensajería interna debe permitir cambiar la forma de envío de notificaciones (correo, SMS, push) sin modificar el código principal del sistema. ¿Qué patrón aplicaría?  
   - a) Adapter  
   - b) Chain of Responsibility  
   - X) Strategy  
   - d) Proxy

3. En un entorno de trabajo colaborativo, múltiples usuarios editan el mismo documento. El sistema necesita permitir “deshacer” y “rehacer” los cambios. ¿Qué patrón de diseño aplica mejor?  
   - X) Command  
   - b) Memento  
   - c) Observer  
   - d) State

4. En una arquitectura basada en eventos, ¿qué atributo de calidad se mejora al desacoplar emisores y receptores de mensajes?  
   - a) Seguridad  
   - X) Mantenibilidad  
   - c) Disponibilidad  
   - d) Usabilidad

5. El patrón Flyweight mejora principalmente:  
   - a) Usabilidad  
   - b) Escalabilidad horizontal  
   - X) Eficiencia en el uso de memoria  
   - d) Portabilidad del sistema

6. El siguiente código rompe un principio SOLID. ¿Cuál?  
```java
class ReportGenerator {
    public void generateReport(String data) {
        System.out.println("Generando reporte: " + data);
    }
    public void sendEmail(String data) {
        System.out.println("Enviando por correo: " + data);
    }
}
```
   - X) SRP  
   - b) LSP  
   - c) DIP  
   - d) OCP

7. El siguiente código es un ejemplo de mal diseño, ¿por qué?  
```python
class PaymentProcessor:
    def process(self, card_type):
        if card_type == "VISA":
            print("Procesando VISA")
        elif card_type == "MasterCard":
            print("Procesando MasterCard")
        else:
            print("Tipo no soportado")
```
   - X) Rompe el Principio de OCP  
   - b) Rompe el Principio de SRP  
   - c) Afecta la eficiencia del sistema  
   - d) Afecta la seguridad del sistema

8. ¿Qué atributo de calidad se vería afectado negativamente si un sistema tiene muchas dependencias circulares?  
   - X) Mantenibilidad  
   - b) Rendimiento  
   - c) Seguridad  
   - d) Escalabilidad

9.  El siguiente código rompe la Inversión de Dependencias (DIP) porque:
```java
class EmailService {
    public void send(String msg) {
        System.out.println("Email enviado");
    }
}

class Notification {
    private EmailService email = new EmailService();
    public void notify(String msg) { email.send(msg); }
}
```

- a) Notification depende de una abstracción  
- b) EmailService implementa una interfaz  
- X) Notification depende de una clase concreta  
- d) EmailService es un Singleton

10.  ¿Cuál es el principal tradeoff al aumentar la disponibilidad mediante redundancia?  
- a) Reduce la cohesión del sistema  
- b) Aumenta la latencia  
- X) Aumenta costos de mantenimiento  
- d) Reduce la interoperabilidad

---

## Desarrollo (40%)

1. ¿Qué significa que un sistema tenga alta cohesión y bajo acoplamiento? (5%)  
-  Alta cohesión: cada módulo/clase tiene una responsabilidad clara y relacionada
-  Bajo acoplamiento: módulos interactúan mediante interfaces mínimas y bien definidas.
-  
-  

2. ¿La siguiente historia cumple con INVEST? Justifique cada letra de INVEST. (5%)  
Historia: "Como estudiante, quiero acceder a mis notas para poder verificar mi progreso en los cursos."  
- I (Independent):  Parcialmente independiente si no depende de otras historias
- N (Negotiable):  Sí, detalles (formato, filtros) negociables.
- V (Valuable):  Sí, aporta valor directo al usuario.
- E (Estimable):  Sí, si se definen criterios de aceptación.
- S (Small):  Puede ser small, dividir si incluye historial o exportación.
- T (Testable): Sí, se pueden definir casos (login, ver nota, permisos).

3. En UML, explique la diferencia entre dependencia y asociación. Dibuje un ejemplo para cada relación. (10%)  
- Dependencia: Relación donde una clase usa a otra.
- Asociación: Relacion de estructura permanente.
- Ejemplos:  
  - Dependencia: A --> B  
  - Asociación: A --- B

---

Lea el siguiente enunciado para las preguntas 4 y 5:

Una empresa de transporte público desea desarrollar un sistema para calcular rutas y tarifas. El sistema debe cumplir con los siguientes requisitos:

- Existen distintos medios de transporte (bus, tren, ferry).  
- Cada medio calcula su tarifa y tiempo estimado de forma diferente.  
- El sistema debe permitir añadir nuevos medios de transporte sin afectar las clases existentes.  
- Los cálculos deben poder cambiarse dinámicamente (por ejemplo, según hora pico o clima).  
- Existen reglas de negocio dinámicas que pueden otorgar distintos tipos de descuentos o tarifas a pagar. Por ejemplo: descuentos por estudiante, tarifas extra por hora pico, por circular cuando la placa cuenta con restricción, descuentos verdes (por transporte eléctrico) y convenios especiales con municipalidades.  
- A futuro, se quiere integrar un algoritmo de optimización de rutas basado en IA que pueda inyectarse sin afectar la arquitectura actual.

Con base en lo anterior, responda:

4. ¿Qué patrón de diseño usaría para representar los diferentes medios de transporte y sus cálculos? (10%)  
 Patrón:  Strategy por los comportamientos y Factory para creación.

    Explicación:      
          
  -  Cada medio implementa una estrategia para tarifa/tiempo
  -  Nuevo medio = nueva implementación de la estrategia, sin tocar código existente
  -  Factory o Registry permite instanciar medios dinámicamente

5. ¿Qué patrón de diseño usaría para permitir la integración de algún servicio de IA posteriormente? (10%)  
 Patrón:   Inyección de dependencias combinada con Adapter.
 Explicación:  
  -  DI permite inyectar un algoritmo de IA sin cambiar clases consumidoras.
  -  Adapter envuelve la IA para ajustarla a la interfaz esperada.
  -  Facilita cambios de servicios a futuro por ejemplo otra IA.

---

## Código (40%)

Esta sección continúa con el enunciado dado en el punto 4 y 5 del Desarrollo.

Realice un POC (proof of concept) en código para explicar cómo implementaría los posibles distintos descuentos y tarifas que cambian dinámicamente.

Un ejemplo sobre cómo puede verse el resultado de su código es:

```
Calculando viaje combinado: Bus + Tren + Bicicleta
Tarifa base total: 2450 colones
Aplicando descuento de estudiante (-15%)
Aplicando descuento verde (-5%)
Tarifa final: 1970 colones
```

Instrucciones para el POC:  
- Implemente un POC simple en el lenguaje de su preferencia que muestre:  
  - Definición de medios de transporte con cálculo de tarifa y tiempo.  
  - Mecanismo para añadir descuentos dinámicos (por ejemplo, Chain of Responsibility, Decorator o Strategy).  
  - Posibilidad de inyectar un servicio de optimización (simulado) sin cambiar las clases existentes.  
- Coloque el código y la salida esperada.  
- Añada comentarios y explicaciones breves.

Desarrollo

```
# POC rápido (ejemplo)
class Transport:
    def fare(self): pass
class Bus(Transport):
    def fare(self): return 1000
class Train(Transport):
    def fare(self): return 1500

# Decorator de descuento
class DiscountDecorator(Transport):
    def __init__(self, transport, pct): self.transport=transport; self.pct=pct
    def fare(self): return int(self.transport.fare() * (1 - self.pct))

# Uso
trip = DiscountDecorator(Bus(), 0.15)           # descuento estudiante -15%
trip2 = DiscountDecorator(Train(), 0.05)        # verde -5%
total = trip.fare() + trip2.fare()
print("Tarifa final:", total)
```
Salida esperada (ejemplo):

Calculando viaje combinado: Bus + Tren

Tarifa base total: 2500

Aplicando descuento de estudiante (-15%)

Aplicando descuento verde (-5%)

Tarifa final: 2047

---

