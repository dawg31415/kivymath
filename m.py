import kivy
kivy.require('2.0.0')
 
from kivy.app import App

from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout


# Consts 
OPERATORS = {
         '+'    : lambda x,y: x + y,
         '-'    : lambda x,y: x - y,
         '*'    : lambda x,y: x * y,
         '^'    : lambda x,y: x ** y,
         '**'   : lambda x,y: x ** y,
}


# Math
def is_number(string:str) -> bool:
    try:
        float(string)
        return True
    except (ValueError, TypeError):
        return False 

def lexer(input_str: str) -> str:
    numbers = []
    operations = []
    for word in str.split(input_str, " "):
        if is_number(word):
            numbers.append(int(word))
        elif word in OPERATORS.keys():
            operations.append(word)

    if len(numbers) < 2 or len(operations) < 1:
        return "Error: wrong syntaxis"

    result = numbers[0]
    for i in range(1, len(numbers)):
        num = numbers[i]
        operator = operations[i-1]
        result = OPERATORS[operator](result, num)

    return str(result)


# App
class Header_SectionSelector(BoxLayout):
    pass

class Body_Math(BoxLayout):
    # (runs after app is loaded)
    def on_kv_post(self, base_widget):
        self.math_input = self.ids.math_input

    # Math
    # (handle button click)
    def do_math(self):
       self.ids.math_output.text=lexer(self.math_input.text)

class Footer_Credentials(AnchorLayout):
    pass

class KivyApp(App):

    # Init
    def build(self):
        WindowLayout = BoxLayout(orientation='vertical')

        WindowLayout.add_widget(Header_SectionSelector())
        WindowLayout.add_widget(Body_Math())
        WindowLayout.add_widget(Footer_Credentials())

        return WindowLayout

    
    # Utility ? idfk
    def leave(self):
        print("leaving app")
        self.stop()

    def on_pause(self):
        print("go fuck yourself")

    def on_resume(self):
        print("hi!")


# Run
def main():
    app = KivyApp()
    app.run()

# Entry point
if __name__ == "__main__":
    main()
