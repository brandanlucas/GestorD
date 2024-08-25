from cliente import Cliente
from producto import Producto

# Crear una instancia de Cliente
cliente1 = Cliente("Juan", "Perez", "reparacion", "123456789", "juan@example.com", "Calle Falsa 123", "Ciudad", "12345", "Provincia")

# Crear una instancia de Producto
producto1 = Producto("Filtro de agua", 50.0, 100.0, 95.0, 90.0)

# Agregar una compra al cliente
cliente1.agregar_compra(producto1.nombre, 2, producto1.precio_efectivo * 2, "2024-08-25")

# Mostrar el historial de compras del cliente
print(cliente1.obtener_historial_compras())
