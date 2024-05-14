import datetime

class Producto:
    def __init__(self, nombre, descripcion, precio, status, cantidad_en_stock):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.status = status
        self.cantidad_en_stock = cantidad_en_stock
        self.fecha_creacion = datetime.datetime.now()
        self.fecha_actualizacion = datetime.datetime.now()

    def actualizar_cantidad_en_stock(self, cantidad):
        self.cantidad_en_stock -= cantidad
        self.fecha_actualizacion = datetime.datetime.now()

class ProductoConOpciones(Producto):
    def __init__(self, nombre, descripcion, precio, status, cantidad_en_stock, opciones):
        super().__init__(nombre, descripcion, precio, status, cantidad_en_stock)
        self.opciones = opciones

    def imprimir_opciones(self):
        for opcion in self.opciones:
            print(opcion + ": " + ", ".join(self.opciones[opcion]))

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
            print("Nombre: " + producto.nombre)
            print("Precio: " + str(producto.precio))
            print("Cantidad: " + str(producto.cantidad_en_stock))
            if isinstance(producto, ProductoConOpciones):
                print("Opciones:")
                producto.imprimir_opciones()
            total += producto.precio * producto.cantidad_en_stock
            print("")
        print("Total: " + str(total))

productos_disponibles = [
    Producto("iPhone 14", "El último iPhone", 999.99, "activo", 10),
    Producto("Samsung Galaxy S21", "El último Samsung Galaxy", 799.99, "activo", 5),
    Producto("Google Pixel 6", "El último Google Pixel", 699.99, "activo", 3)
]

nuevo_producto = Producto("Sony Xperia 5 III", "El último Sony Xperia", 899.99, "activo", 7)
productos_disponibles.append(nuevo_producto)

iphone_14_opciones = {
    "Tamaño": ["Pequeño", "Mediano", "Grande"],
    "Color": ["Rojo", "Azul", "Verde"]
}
iphone_14_con_opciones = ProductoConOpciones("iPhone 14 con opciones", "", 999.99, "activo", 10, iphone_14_opciones)

carrito_de_compras = Carrito()
carrito_de_compras.agregar_producto(iphone_14_con_opciones)
carrito_de_compras.agregar_producto(nuevo_producto)

orden_de_compra = Orden()
for producto in carrito_de_compras.productos:
    orden_de_compra.agregar_producto(producto)

orden_de_compra.generar_factura()
