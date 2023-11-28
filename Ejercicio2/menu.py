
class Menu:
    def __init__(self, codigo, elementos):
        self.codigo = codigo
        self.elementos = elementos  # Lista de elementos del menú (entradas, bebidas, pizzas, postres, etc.)
        self.precio_total = self.calcular_precio_total()

    def calcular_precio_total(self):
        precio_total = sum(elemento.precio for elemento in self.elementos)
        # Lógica para aplicar descuentos por promoción, si corresponde
        # ...

        return precio_total

class ElementoMenu:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Ejemplo de uso:

# Definir elementos del menú
entrada = ElementoMenu("Ensalada César", 5.99)
bebida = ElementoMenu("Refresco", 2.49)
pizza_margherita = ElementoMenu("Pizza Margherita", 8.99)
postre = ElementoMenu("Tarta de Chocolate", 4.99)

# Crear menús simples
menu_individual_1 = Menu("M1", [entrada, bebida, pizza_margherita, postre])
menu_individual_2 = Menu("M2", [entrada, bebida, pizza_margherita])

# Crear menú compuesto (Combo Pareja)
combo_pareja = Menu("Combo Pareja", [menu_individual_1, menu_individual_2])

# Obtener el precio total del Combo Pareja
print("Precio del Combo Pareja:", combo_pareja.precio_total)