import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import random
import difflib



#define our different screens
class UnitScreen(Screen):
    def unitchoice(self, button):
        vocab_unit = {1:'unit1vocab.txt', 2:'unit2vocab.txt', 3: 'unit3vocab.txt'}
        key = vocab_unit[button]
        global unit
        unit = {}
        file = open(key)
        for line in file:
            (k,v) = line.split('= ')
            unit[str(k)] =v
        return unit



class ChoiceScreen(Screen):
    def reviewword(self):
        length = len(unit)
        #pair is the key, unit[pair] is the value
        global pair
        pair = random.choice(list(unit))
        global word
        global answer
        word = unit[pair]
        self.ids.prompt.text = f'What is the definition for: {pair}'
        self.ids.answer.text = f'{word}'
        return word
        return pair
        del unit[pair]


    def cleartext(self):
        self.ids.write.text= ' '


    def reviewdef(self):
        length = len(unit)
        #pair is the key, unit[pair] is the value
        global pair
        pair = random.choice(list(unit))
        global word
        word = unit[pair]
        self.ids.prompt.text = f'What is the word for: {word}'
        self.ids.answer.text = f'{pair} '
        return pair
        return word
        del unit[pair]
        global thing
        thing == 2
        return thing

    def addpoint(self):
        numbs= int(self.ids.score.text)
        numbs=numbs+1
        numsy =str(numbs)
        self.ids.score.text = numsy



    def reveal(self):
        self.ids.answer.color = (.9,.9,.9,1)

    def hide(self):
        self.ids.answer.color = (.9,.9,.9,0)


    def clear(self):
        self.ids.answer.text = ' '
        self.ids.prompt.text = ' '

        #this function will get the text box input, and store it as a variable,
        #as well as get the text from the answer label, and store it as a variable
        # then globally return those variables:
    def gettexts(self):
        global input1
        global input2
        input1 = self.ids.write.text
        input2 = self.ids.prompt.text
        return input1
        return input2

        #create a function that checks the answer, with the text box
    def check(self,input1, input2):
        result=difflib.SequenceMatcher(None, input1, input2)
        percent =(result.ratio()*100)
        if percent>50:
            numbs= int(self.ids.score.text)
            numbs=numbs+1
            numsy =str(numbs)
            self.ids.score.text = numsy




class WindowManager(ScreenManager):
    pass
#sets app size
Window.size= (500, 700)


kv = Builder.load_file('practice.kv')



class MyApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyApp().run()
