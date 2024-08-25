class Producto:
    """
    Clase que representa un producto en el sistema.
    """

    def __init__(self, nombre, costo, precio_efectivo, precio_transferencia, precio_mayor):
        """
        Constructor de la clase Producto.
        
        :param nombre: Nombre del producto.
        :param costo: Costo de adquisición del producto.
        :param precio_efectivo: Precio de venta en efectivo.
        :param precio_transferencia: Precio de venta por transferencia.
        :param precio_mayor: Precio de venta al por mayor.
        """
        self.nombre = nombre
        self.costo = costo
        self.precio_efectivo = precio_efectivo
        self.precio_transferencia = precio_transferencia
        self.precio_mayor = precio_mayor
