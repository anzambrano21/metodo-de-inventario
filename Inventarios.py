class Producto:
    def __init__(self, nombre, descripcion, precio, status, cantidad_en_stock, fecha_creacion, fecha_actualizacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.status = status
        self.cantidad_en_stock = cantidad_en_stock
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion = fecha_actualizacion

    def actualizar_cantidad_en_stock(self, cantidad_vendida):
        self.cantidad_en_stock -= cantidad_vendida


class ProductoConOpciones(Producto):
    def __init__(self, nombre, descripcion, precio, status, cantidad_en_stock, fecha_creacion, fecha_actualizacion, opciones):
        super().__init__(nombre, descripcion, precio, status, cantidad_en_stock, fecha_creacion, fecha_actualizacion)
        self.opciones = opciones

    def imprimir_opciones(self):
        for opcion in self.opciones:
            print(opcion + ":")
            for valor in self.opciones[opcion]:
                print("  - " + valor)
class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self):
        if len(self.productos) > 0:
            return self.productos.pop()
        else:
            return None

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

class Orden:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def generar_factura(self):
        total = 0
        print("Factura:")
        for producto in self.productos:
            print(f"Producto: {producto.nombre}")
            print(f"Precio: {producto.precio}")
            print(f"Cantidad: {producto.cantidad}")
            print(f"Opciones seleccionadas: {producto.opciones}")
            total += producto.precio * producto.cantidad
        print(f"Total de la compra: {total}")

class Controlador:
    def __init__(self):
        self.productos = []
        self.carrito = []
        self.ordenes = []

    def listar_productos(self):
        for producto in self.productos:
            if producto.status == "activo" and producto.stock > 0:
                print(f"Producto: {producto.nombre}")
                print(f"Opciones: {producto.opciones}")
                print(f"Precio: {producto.precio}")
                print(f"Stock: {producto.stock}")

    def agregar_producto(self, producto):
        self.carrito.append(producto)

    def hacer_compra(self):
        orden = Orden()
        for producto in self.carrito:
            orden.agregar_producto(producto)
        self.ordenes.append(orden)
        self.carrito = []

    def listar_ordenes(self):
        for orden in self.ordenes:
            print(f"Orden: {orden.id}")
            print(f"Productos:")
            for producto in orden.productos:
                print(f"Producto: {producto.nombre}")
                print(f"Precio: {producto.precio}")
                print(f"Cantidad: {producto.cantidad}")
                print(f"Opciones seleccionadas: {producto.opciones}")

    def listar_carrito(self):
        for producto in self.carrito:
            print(f"Producto: {producto.nombre}")
            print(f"Precio: {producto.precio}")
            print(f"Cantidad: {producto.cantidad}")
            print(f"Opciones seleccionadas: {producto.opciones}")
