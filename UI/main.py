from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen


# create a goals card we will style in the kv file

class GoalCard(RectangularRippleBehavior, MDBoxLayout):
    # create property to hold the main color for the card
    card_color = ListProperty([0, 0, 0, 0])
    # create property to hold the score for this card
    score = NumericProperty(0)
    # this property will hold the goal name
    goal_title = StringProperty('')
    # create property to hold the goal items number
    items_num = NumericProperty(1)
    # create property to hold the goal icon
    goal_icon = StringProperty('')


# create GoalsManager widget tobe the root widget of the app
class GoalsManager(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        # create goals list data
        goals_data = [
            # goal_title,card_color,score, items_num,goal_icon
            ['SCAN HERE', '#c8ff59', 1,0, 'qrcode-scan'],
            ['YOUR CART', '#9ed335', 1,0, 'cart'],
            ['YOUR WISHLIST', '#638f0d', 1,0, 'list-box'],
            ['ABOUT US', '#739431', 1, 0,'contacts']
            ,

        ]
        for index, item in enumerate(goals_data):
            from kivy.utils import get_color_from_hex
            card = GoalCard()
            # use get_color_from_hex to get rgba from hex
            card.card_color = get_color_from_hex(item[1])
            card.goal_title = item[0]
            card.score = item[2]
            card.items_num = item[3]
            card.goal_icon = item[4]
            # if index is even add card to the left box if else add it to the right box
            if (index % 2) == 0:
                self.ids.left_box.add_widget(card)
            else:
                self.ids.right_box.add_widget(card)


# creating app instance
class App(MDApp):
    # create build method this will launch when the app is building
    def build(self):
        # here we will specify the app primary color
        self.theme_cls.primary_palette = "Blue"

        # here we will specify the app primary hue
        self.theme_cls.primary_hue = "500"

        # here we will specify the app accent color
        self.theme_cls.accent_palette = "Amber"

        # here we will specify the app accent hue
        self.theme_cls.accent_hue = "500"

        # here we will specify the app theme
        self.theme_cls.theme_style = "Light"

        # load kv file to load the ui using Builder
        Builder.load_file('main.kv')

        # specify the material style version
        self.theme_cls.material_style = "M3"

        # return the root widget of the app
        return GoalsManager()
    



# run the app
if __name__ == '__main__':
    app = App()
    app.run()