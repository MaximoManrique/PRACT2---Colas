from abc import ABC, abstractmethod
from typing import Any, Optional
import time

class Pedido:
    def __init__(self, cantidad: int, cliente: str):
     
        self._cliente = cliente
        self._cantidad = cantidad

    def imprimir_detalles(self):
     
        print(f"     Cliente: {self.cliente}")
        print(f"     Cantidad: {self.cantidad}")
    @property
    def cantidad(self) -> int:
      
        return self._cantidad

    @property
    def cliente(self) -> str:
      
        return self._cliente

    def __str__(self) -> str:
      
        return f"[Pedido de {self.cliente} por {self.cantidad} unidades]"


class InterfazCola(ABC):
    @abstractmethod
    def tamano(self) -> int: pass
    
    @abstractmethod
    def esta_vacia(self) -> bool: pass
    
    @abstractmethod
    def frente(self) -> Optional[Any]: pass
    
    @abstractmethod
    def encolar(self, info: Any): pass
    
    @abstractmethod
    def desencolar(self) -> Optional[Any]: pass

class Nodo:
    def __init__(self, dato: Any, siguiente_nodo: Optional['Nodo'] = None):
        self.dato = dato
        self.siguiente_nodo = siguiente_nodo


class ColaEnlazada(InterfazCola):
    def __init__(self):
        self._cabeza: Optional[Nodo] = None  
        self._cola: Optional[Nodo] = None    
        self._tamano: int = 0

    def tamano(self) -> int:
        return self._tamano

    def esta_vacia(self) -> bool:
        return self._tamano == 0

    def frente(self) -> Optional[Any]:
      
        if self.esta_vacia():
            return None
        return self._cabeza.dato

    def encolar(self, info: Any):
       
        nuevo_nodo = Nodo(info)
        if self.esta_vacia():
            self._cabeza = nuevo_nodo
            self._cola = nuevo_nodo
        else:
            self._cola.siguiente_nodo = nuevo_nodo
            self._cola = nuevo_nodo
        self._tamano += 1

    def desencolar(self) -> Optional[Any]:
      
        if self.esta_vacia():
            return None
        
        dato_a_retornar = self._cabeza.dato
        self._cabeza = self._cabeza.siguiente_nodo
        
        if self._cabeza is None:
            self._cola = None
            
        self._tamano -= 1
        return dato_a_retornar

    def imprimir_estado_cola(self):
      
        print(f"\n--- ESTADO DE LA COLA (Pedidos pendientes: {self.tamano()}) ---")
        nodo = self._cabeza
        if nodo is None:
            print("   [La cola está vacía]")
        
        index = 1
        while nodo is not None:
            print(f"   {index}. {nodo.dato}")
            nodo = nodo.siguiente_nodo
            index += 1



if __name__ == "__main__":
    
    print("Inicia el sistema de recepción de pedidos.")
    
  
    cola_de_pedidos = ColaEnlazada()
    
    print("\n[Llegan nuevos pedidos...]")
    time.sleep(1)

 
    pedido1 = Pedido(cantidad=50, cliente="Empresa A")
    cola_de_pedidos.encolar(pedido1)
    print(f"  -> Llegó {pedido1}")

    time.sleep(1)


    pedido2 = Pedido(cantidad=120, cliente="Empresa B")
    cola_de_pedidos.encolar(pedido2)
    print(f"   Llegó {pedido2}")
    
 
    cola_de_pedidos.imprimir_estado_cola()
    
    print("\n[Fábrica empieza a procesar pedidos...]")
    time.sleep(2)

   
    pedido_en_proceso = cola_de_pedidos.desencolar()
    if pedido_en_proceso:
        print(f"   Procesando: {pedido_en_proceso}")
        
    cola_de_pedidos.imprimir_estado_cola()

    print("\n[Llega un nuevo pedido...]")
    time.sleep(1)
    
    pedido3 = Pedido(cantidad=30, cliente="Empresa C (Urgente)")
    cola_de_pedidos.encolar(pedido3)
    print(f"   Llegó {pedido3}")
    
    cola_de_pedidos.imprimir_estado_cola()
    
    print("\n[Fábrica termina y busca más pedidos...]")
    time.sleep(2)
    

    pedido_en_proceso = cola_de_pedidos.desencolar()
    if pedido_en_proceso:
        print(f"  <-  Procesando: {pedido_en_proceso}")

    time.sleep(2)

    # Procesamos el último
    pedido_en_proceso = cola_de_pedidos.desencolar()
    if pedido_en_proceso:
        print(f"  <-  Procesando: {pedido_en_proceso}")
    
    cola_de_pedidos.imprimir_estado_cola()
    print("\ Todos los pedidos han sido procesados.")