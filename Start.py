import time
import os
import pygame
import functions as fun
from Act_one import act_one

spookyambience = (os.path.join('soundeffects', 'SpookyAmbience.wav'))

def start_game():
    fun.music(spookyambience)
    fun.clear_screen()
    fun.print_smooth("Would you like to view the tutorial?")
    time.sleep(1)
    tutorial_y_n = raw_input("Y or N?--> ")
    if tutorial_y_n.lower() in ["y", "yes"]:
        fun.clear_screen()
        fun.print_smooth("This is a text based game that contains inventory items as well as path choices.\n\n"
                         "You, the player, will be able to select different inventory items and path choices through "
                         "prompts in the game.\n\nPaths and inventory items will always be bolded text.\n\n"
                         "For example, if two choices were 'Do you want to ride a BIKE or drive a CAR' your response"
                         " could be either 'CAR' or 'BIKE'. Your responses do not have to be capitalized however. \n\nThere will also be scenarios in which you will have"
                         " limited time to enter in a valid response or face the consequences. Be prepared and enjoy!")
        raw_input("\n\n\n***Press ENTER when ready***")
        time.sleep(1)
        pygame.mixer.music.fadeout(35000)
        act_one()

    elif tutorial_y_n.lower() in ["n", "no"]:
        pygame.mixer.music.fadeout(35000)
        act_one()
    else:
        fun.print_smooth("\n\nPlease enter Y or N.")
        start_game()

start_game()