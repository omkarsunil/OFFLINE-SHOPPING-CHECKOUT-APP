from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivy.metrics import sp
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.zbarcam.zbarcam import ZBarCam
from kivy.uix.button import Button
from kivymd.toast import toast
import datetime
from datetime import date
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivy.properties import ObjectProperty, StringProperty
from userDatabase import User
import sqlite3


conn = sqlite3.connect('userDatabase.db')
cursor = conn.cursor()


'''class UserDetails:
    def checkDetails(self):
        str = "SELECT Username, Email, Password FROM User"
        cursor.execute(str)
        data = cursor.fetchall()
        if self.ids.email.text in data:
            print("Hello")
'''
class MainScreen(MDScreen):
    pass

class LoginScreen(MDScreen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginButton(self):
        if data_base.validate(self.email.text, self.password.text):
            AccountScreen.current = self.email.text
            self.reset()
            self.manager.current = "account"
        else:
            invalid_login()

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class SignupScreen(MDScreen):
    nm = ObjectProperty(None)
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.nm.text != "" and self.username.text != "" and self.email.text != "" and data_base.valide_email(self.email.text) and self.password.text != "":
            data_base.add_user(self.nm.text, self.username.text, self.email.text, self.password.text)
            self.reset()
            toast("Account Created Successfully!")
            self.manager.current = "login"
        else:
            invalid_form()

    def reset(self):
        self.nm.text = ""
        self.username.text = ""
        self.email.text = ""
        self.password.text = ""

class AccountScreen(MDScreen):
    def show(self):
        str = "SELECT * FROM Cart"
        cursor.execute(str)
        conn.commit()
        data = cursor.fetchall()
        for x in data:
            print(x[0])

    def total(self):
        str = "SELECT SUM(Price) FROM Cart"
        cursor.execute(str)
        conn.commit()
        cursor.fetchall()


class QrCodeScreen(MDScreen):
    txt = ObjectProperty(None)
    
    def addToCart(self):
        self.manager.current = "account"
        if self.txt.text == "":
            self.ids.add.disabled = True
        else:
            self.ids.add.disabled = False
            str = "INSERT INTO Cart(Price) VALUES(?)"
            pr = self.txt.text[2:-1]
            cursor.execute(str, (pr, ))
            conn.commit()
            cursor.fetchall()
        #td.display()
        
class InvoiceScreen(MDScreen):
    def show(self):
        str = "SELECT * FROM Cart"
        cursor.execute(str)
        conn.commit()
        data = cursor.fetchall()
        for x in data:
            return x[0]  


# class ToDoCard(MDScreen):
#     date = StringProperty(None)
#     todo_list = ObjectProperty(None)

#     def display(self):
#         today = date.today()
#         wd = date.weekday(today)
#         days = ['Monday', 'Tuesday', 'Wednesday',
#                 'Thursday', 'Friday', 'Saturday', 'Sunday']
#         year = str(datetime.datetime.now().year)
#         month = str(datetime.datetime.now().strftime("%b"))
#         day = str(datetime.datetime.now().strftime("%d"))
#         screen_manager.get_screen(
#             "todo").date.text = f"{days[wd]},{day} {month} {year}"

# td = ToDoCard()

class Content(BoxLayout):
    manager = ObjectProperty(None)
    nav_drawer = ObjectProperty(None)

class WindowManager(ScreenManager):
    pass

def invalid_login():
    toast("Invalid Email or Password!")

def invalid_form():
    toast("Please Enter Valid Information!")

screen_manager = WindowManager()
data_base = User("userDatabase.db")
screens = [MainScreen(name = "main"), LoginScreen(name = "login"), SignupScreen(name = "signup"), AccountScreen(name = "account"), QrCodeScreen(name = "qr"), InvoiceScreen(name = "invoice")]
for i in screens:
    screen_manager.add_widget(i)

screen_manager.current = "main"
          
class Shopping(MDApp):
    def build(self):
        return Builder.load_file("main.kv")
    
    

if __name__  == '__main__':
    Shopping().run()