import webbrowser
from os import system

def main_screen():
    _ = system('clear')
    print("\n Choose your Recipe: ")
    print("\n\n A) Engagement Chicken")
    answer = input("\n\n Input the letter of choice > ")
    if answer.lower() == 'a':
        print("The Recipe Will open on your browser")
        webbrowser.open("https://www.dessertfortwo.com/dinner-for-two-engagement-pasta/")
    else:
        main_screen()
main_screen()