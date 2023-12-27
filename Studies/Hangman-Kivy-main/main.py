# Importing the required modules.
import random
import string

import kivy
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from words import WORDS

# Minimum kivy requirements.
kivy.require("1.9.0")


class ButtonsLayout(GridLayout):
    INSTANCES = []

    def __init__(self, **kwargs):
        super(ButtonsLayout, self).__init__(**kwargs)

        # Adding self to the list of instances.
        ButtonsLayout.INSTANCES.append(self)

        # Configuring the layout.
        self.rows = 2
        self.cols = 13

        # Creating a dictionary for buttons.
        self.buttons = {}

        # Creating the buttons.
        self.create_buttons()

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


class MyRoot(BoxLayout):
    ERRORS = StringProperty()
    HANGMAN_IMG = StringProperty()
    GAME_MSG = StringProperty()
    WORD_DISPLAY = StringProperty()
    ###ss

    def __init__(self, **kwargs):
        super(MyRoot, self).__init__(**kwargs)

        # RANDOM_WORD for the word to be guessed.
        self.RANDOM_WORD = ""

        # List of all the guessed alphabets.
        self.GUESSES = []

        # The layout of the available alphabets.
        self.buttons_layout = ButtonsLayout.INSTANCES[0]

        # Configuring the buttons.
        self.configure_buttons()

        # Starting the game.
        self.start_game()

    @property
    def won(self):
        return all(alphabet in self.GUESSES for alphabet in self.RANDOM_WORD)

    def update_word_display(self):
        # Updating display of the word.
        WORD_DISPLAY = []
        for alphabet in self.RANDOM_WORD:
            if alphabet in self.GUESSES:
                WORD_DISPLAY.append(alphabet)
            else:
                WORD_DISPLAY.append("_")

        # Adding space between each character.
        self.WORD_DISPLAY = " ".join(WORD_DISPLAY)

    def btn_press(self, widget):
        # Disabling the button.
        widget.disabled = True

        # Adding the alphabet to the list of GUESSES.
        self.GUESSES.append(widget.text)

        if widget.text in self.RANDOM_WORD:
            # Updating the word.
            self.update_word_display()

            if self.won:
                # Disabling all the buttons.
                for button in self.buttons_layout.buttons.values():
                    button.disabled = True

                # Changing the game message.
                self.GAME_MSG = "You Won!!!"
        else:
            # Adding 1 to the ERRORS.
            self.ERRORS = str(int(self.ERRORS) + 1)

            # Changing the hangman image.
            self.HANGMAN_IMG = "images/hangman" + self.ERRORS + ".png"

            # Checking if the game is over.
            if int(self.ERRORS) == 7:
                # Disabling all the buttons.
                for button in self.buttons_layout.buttons.values():
                    button.disabled = True

                # Changing the game message.
                self.GAME_MSG = "GAME OVER!!!"

                # Changing the display of the word.
                self.WORD_DISPLAY = self.RANDOM_WORD

    def configure_buttons(self):
        # Bind all the buttons.
        for button in self.buttons_layout.buttons.values():
            button.on_press = lambda btn=button: self.btn_press(btn)

    def start_game(self):
        # Getting a Random Word.
        self.RANDOM_WORD = random.choice(WORDS)

        # Clearing the Guesses.
        self.GUESSES.clear()

        # Changing the ERRORS to 0.
        self.ERRORS = "0"

        # Changing the Hangman Image.
        self.HANGMAN_IMG = "images/hangman0.png"

        # Changing the GAME_MSG.
        self.GAME_MSG = "Guess the word"

        # Changing the word display.
        self.WORD_DISPLAY = " ".join(["_" for _ in self.RANDOM_WORD])

        # Enabling all the buttons.
        for button in self.buttons_layout.buttons.values():
            button.disabled = False


class Hangman(App):

    def build(self):
        return MyRoot()


hangman = Hangman()
hangman.run()
