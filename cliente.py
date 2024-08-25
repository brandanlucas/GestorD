class Cliente:
    """
    Clase que representa a un cliente dentro del sistema de gestión del emprendimiento.
    """

    def __init__(self, nombre, apellido, tipo_cliente, celular, email, direccion, localidad, codigo_postal, provincia):
        """
        Constructor de la clase Cliente.
        
        :param nombre: Nombre del cliente.
        :param apellido: Apellido del cliente.
        :param tipo_cliente: Tipo de cliente ('repuestos' o 'reparacion').
        :param celular: Número de celular del cliente.
        :param email: Email del cliente.
        :param direccion: Dirección física del cliente.
        :param localidad: Localidad donde reside el cliente.
        :param codigo_postal: Código postal del cliente.
        :param provincia: Provincia del cliente.
        """
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_cliente = tipo_cliente  # Puede ser 'repuestos' o 'reparacion'
        self.celular = celular
        self.email = email
        self.direccion = direccion
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.historial_compras = []  # Lista para almacenar el historial de compras
        self.historial_reparaciones = []  # Lista para almacenar el historial de reparaciones

    def agregar_compra(self, producto, cantidad, precio, fecha):
        """
        Agrega una compra al historial del cliente.

        :param producto: Nombre del producto comprado.
        :param cantidad: Cantidad de productos comprados.
        :param precio: Precio total de la compra.
        :param fecha: Fecha de la compra.
        """
        self.historial_compras.append({
            'producto': producto,
            'cantidad': cantidad,
            'precio': precio,
            'fecha': fecha
        })

    def agregar_reparacion(self, equipo, num_serie, detalle, costo, fecha_reparacion, garantia):
        """
        Agrega una reparación al historial del cliente.

        :param equipo: Tipo de equipo reparado (por ejemplo, 'dispenser').
        :param num_serie: Número de serie del equipo.
        :param detalle: Descripción de la reparación realizada.
        :param costo: Costo de la reparación.
        :param fecha_reparacion: Fecha en la que se realizó la reparación.
        :param garantia: Garantía de la reparación.
        """
        self.historial_reparaciones.append({
            'equipo': equipo,
            'num_serie': num_serie,
            'detalle': detalle,
            'costo': costo,
            'fecha_reparacion': fecha_reparacion,
            'garantia': garantia
        })

    def obtener_historial_compras(self):
        """
        Devuelve el historial completo de compras del cliente.
        """
        return self.historial_compras

    def obtener_historial_reparaciones(self):
        """
        Devuelve el historial completo de reparaciones del cliente.
        """
        return self.historial_reparaciones
    