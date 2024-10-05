import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class TranslatorApp(App):
    def build(self):
        self.translate_from_dictionary()
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.input_box = TextInput(multiline=False, size_hint=(1, 0.4), hint_text='enter a word')


        self.translate_button = Button(text="Translate", size_hint=(1, 0.2))
        self.translate_button.bind(on_press=self.translate)

        self.translation = Label(text='', size_hint=(1, 0.4))
        self.layout.add_widget(self.input_box)
        self.layout.add_widget(self.translate_button)
        self.layout.add_widget(self.translation)
        return self.layout

    def translate(self, instnace):
        word = self.input_box.text
        translated_word = self.dictionary.get(word, "Not found in dictionary")
        self.translation.text = translated_word
    
    def translate_from_dictionary(self):
        with open('project22/english_german.json', 'r') as file:
            self.dictionary = json.load(file)
    
TranslatorApp().run()
