import kivy
kivy.require('2.0.0')
 
from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout


# Initialization
class Header_SectionSelector(BoxLayout):
    pass

class Body_Math(GridLayout):
    pass

class Footer_Credentials(AnchorLayout):
    pass
 

# Build
class KivyApp(App):
    def build(self):
        WindowLayout = BoxLayout(orientation='vertical')

        WindowLayout.add_widget(Header_SectionSelector())
        WindowLayout.add_widget(Body_Math())
        WindowLayout.add_widget(Footer_Credentials())

        return WindowLayout

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
