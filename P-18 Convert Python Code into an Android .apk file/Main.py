from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class Main_App(MDApp):
    def build(self):
        return MDLabel(text="Welcome to Whoosh-Tech",halign="center")
    
if __name__ == '__main__':
    Main_App().run()
    
#now open Google collab and create a new notebook 
#simple search on your browser and select first collab notebook and create new notebook

"""Then with the help of it we will create our app"""