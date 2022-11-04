# install library termcolor pip install termcolor
#import library termcolor
from termcolor import colored

text = input("plz enter your text")
color = input('''select color --> 
                               * grey
                               * red
                               * green
                               * yellow
                               * blue
                               * magenta
                               * cyan
                               * white
               ---------------> ''')
print (colored (text, color))

