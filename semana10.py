class Inventario:
    def _init_(self, archivo='inventario.txt'):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario."""
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    id, nombre, cantidad, precio = linea.strip().split(',')
                    self.productos.append(Producto(int(id), nombre, int(cantidad), float(precio)))
        except FileNotFoundError:
            print(f"Archivo '{self.archivo}' no encontrado, se creará uno nuevo al guardar.")
        except PermissionError:
            print(f"Permisos insuficientes para leer el archivo '{self.archivo}'.")

    def guardar_inventario(self):
        """Guarda los productos en el archivo de inventario."""
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    file.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n")
        except PermissionError:
            print(f"Permisos insuficientes para escribir en el archivo '{self.archivo}'.")

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_inventario()

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id != id_producto]
        self.guardar_inventario()

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.guardar_inventario()
                return
        print(f"Producto con ID {id_producto} no encontrado.")

    def mostrar_productos(self):
        for producto in self.productos:
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")