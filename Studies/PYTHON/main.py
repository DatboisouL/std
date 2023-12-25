from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class HangmanGame(BoxLayout):
    def __init__(self, **kwargs):
        super(HangmanGame, self).__init__(**kwargs)
        
        self.word_to_guess = "HANGMAN"
        self.guess_word = ["_"] * len(self.word_to_guess)
        self.attempts_left = 6

        self.word_label = Label(text=" ".join(self.guess_word))
        self.add_widget(self.word_label)

        self.attempts_label = Label(text=f"Attempts left: {self.attempts_left}")
        self.add_widget(self.attempts_label)

        self.input_label = Label(text="Enter a letter:")
        self.add_widget(self.input_label)

        self.input_text = TextInput(multiline=False)
        self.add_widget(self.input_text)

        self.guess_button = Button(text="Guess", on_press=self.guess_letter)
        self.add_widget(self.guess_button)

        self.reset_button = Button(text="Reset", on_press=self.reset_game)
        self.add_widget(self.reset_button)

        # Add at least 24 more widgets as needed for your specific Hangman game.

    def guess_letter(self, instance):
        if self.attempts_left > 0:
            letter = self.input_text.text.upper()
            self.input_text.text = ""

            if letter.isalpha() and len(letter) == 1:
                if letter in self.word_to_guess:
                    for i, char in enumerate(self.word_to_guess):
                        if char == letter:
                            self.guess_word[i] = letter

                    self.word_label.text = " ".join(self.guess_word)

                    if "_" not in self.guess_word:
                        self.word_label.text = "Congratulations! You guessed the word."
                        self.disable_input()
                else:
                    self.attempts_left -= 1
                    self.attempts_label.text = f"Attempts left: {self.attempts_left}"

                    if self.attempts_left == 0:
                        self.word_label.text = f"Game over! The word was {self.word_to_guess}."
                        self.disable_input()
            else:
                self.word_label.text = "Invalid input. Please enter a single letter."

    def reset_game(self, instance):
        self.word_to_guess = "HANGMAN"
        self.guess_word = ["_"] * len(self.word_to_guess)
        self.attempts_left = 6

        self.word_label.text = " ".join(self.guess_word)
        self.attempts_label.text = f"Attempts left: {self.attempts_left}"
        self.input_text.text = ""

        self.enable_input()

    def disable_input(self):
        self.input_text.disabled = True
        self.guess_button.disabled = True

    def enable_input(self):
        self.input_text.disabled = False
        self.guess_button.disabled = False

class HangmanApp(App):
    def build(self):
        return HangmanGame()

if __name__ == '__main__':
    HangmanApp().run()
