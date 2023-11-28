
class PizzaBuilderGUIMenu:


    def mostrar_descripcion_pizza(self):
        # Mostrar la información de la pizza creada
        self.result_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
        self.result_text.insert(tk.END, f"Tipo de masa: {self.pizza.tipo_masa}\n")
        self.result_text.insert(tk.END, f"Tipo de salsa: {self.pizza.tipo_salsa}\n")
        for ingrediente in self.pizza.ingredientes:
            self.result_text.insert(tk.END, ingrediente + "\n")
        self.result_text.config(state=tk.DISABLED)  # Deshabilitar la edición

        # Agregar opciones de bebidas y postres
        self.label_bebida = tk.Label(self.frame, text="Selecciona una bebida:")
        self.label_bebida.pack()

        self.bebidas = {
            "Refresco": 2.49,
            "Agua": 1.99,
            "Jugo": 2.99
        }
        self.bebida_seleccionada = tk.StringVar()
        self.bebida_seleccionada.set("Refresco")  # Valor por defecto: Refresco

        for bebida, precio in self.bebidas.items():
            self.radio_bebida = tk.Radiobutton(self.frame, text=bebida, variable=self.bebida_seleccionada, value=bebida)
            self.radio_bebida.pack()

        self.label_postre = tk.Label(self.frame, text="Selecciona un postre:")
        self.label_postre.pack()

        self.postres = {
            "Tarta de Chocolate": 4.99,
            "Helado": 3.49,
            "Fruta fresca": 2.99
        }
        self.postre_seleccionado = tk.StringVar()
        self.postre_seleccionado.set("Tarta de Chocolate")  # Valor por defecto: Tarta de Chocolate

        for postre, precio in self.postres.items():
            self.radio_postre = tk.Radiobutton(self.frame, text=postre, variable=self.postre_seleccionado, value=postre)
            self.radio_postre.pack()

        self.agregar_al_menu_button = tk.Button(self.frame, text="Agregar al menú", command=self.agregar_al_menu)
        self.agregar_al_menu_button.pack()

    def agregar_al_menu(self):
        # Obtener la bebida y el postre seleccionados
        bebida_elegida = self.bebida_seleccionada.get()
        postre_elegido = self.postre_seleccionado.get()

        # Crear los elementos del menú (bebida y postre)
        bebida = ElementoMenu(bebida_elegida, self.bebidas[bebida_elegida])
        postre = ElementoMenu(postre_elegido, self.postres[postre_elegido])

        # Crear un menú con la pizza, la bebida y el postre
        menu_personalizado = Menu("Menu Personalizado", [self.pizza, bebida, postre])

        # Mostrar el precio total del menú personalizado
        print("Precio del Menú Personalizado:", menu_personalizado.precio_total)
