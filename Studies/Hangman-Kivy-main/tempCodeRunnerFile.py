def create_buttons(self):
        # Creating buttons for all the alphabets.
        for alphabet in string.ascii_uppercase:
            # Creating button.
            button = Button(
                text=alphabet,
                font_name="fonts/Plaguard.otf",
                font_size=24,
            )

            # Adding button to the layout.
            self.add_widget(button)

            # Adding button to the dictionary.
            self.buttons[alphabet] = button