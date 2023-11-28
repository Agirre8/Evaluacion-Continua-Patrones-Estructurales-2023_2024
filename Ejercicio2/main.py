from pizza_builder_gui import *
from pizza_builder_guiMenu import *

def main():
    root = tk.Tk()
    app = PizzaBuilderGUI(root)
    root.mainloop()

    # Una vez se cierra la interfaz previa, continuar con PizzaBuilderGUIMenu
    root2 = tk.Tk()
    app2 = PizzaBuilderGUIMenu(root2)
    app2.mostrar_descripcion_pizza()  # Llama al método para mostrar la descripción de la pizza
    root2.mainloop()

if __name__ == "__main__":
    main()