import functions as fun
import os
from functions import print_smooth
import time
import pygame
from sys import exit
from Inventory import inventory
import Road


car_areas = ["BACK SEAT", "GLOVEBOX", "SEATS", "LEAVE CAR"]

creepy_ambient = (os.path.join('soundeffects', 'creepyambient.wav'))
cell_vibrate = (os.path.join('soundeffects', 'cellvibrate.wav'))
phone_static = (os.path.join('soundeffects', 'phonestatic.wav'))
door_ajar_sound = (os.path.join('soundeffects', 'cardoorajar.wav'))
cell_disconnect = (os.path.join('soundeffects', 'Celldisconnect.wav'))
scary_piano = (os.path.join('soundeffects', 'Scarypiano.wav'))
suffocating_man = (os.path.join('soundeffects', 'SuffocatingMan.wav'))

def find_phone():
    fun.sound_effect(creepy_ambient)
    fun.clear_screen()
    print_smooth("You crouch down and prepare to look in the car for your phone. The interior light miraculously still"
                 " works, but is slowly dying from battery drain.")
    print_smooth("\n\nYou begin to crawl back into the car.")
    fun.sound_effect(door_ajar_sound)
    time.sleep(1)

    print_smooth('\n\nBroken glass and plastic are scattered everywhere in the car. "Damnit", you say to yourself.'
                 ' "It could be anywhere."')

    find_phone_where()


def find_phone_where():
    print_smooth("\n\nWhere should I look?")
    print_smooth(', or '.join(car_areas))
    look_where = raw_input()

    if look_where.lower() in ["back seat", "backseat"] and "BACK SEAT" in car_areas:
        backseat()

    elif look_where.lower() in ["back seat", "backseat"] and "BACK SEAT" not in car_areas:
            print_smooth("You've already searched the BACK SEAT!")
            find_phone_where()

    elif look_where.lower() in ["glove box", "glovebox", "glove"] and "GLOVEBOX" in car_areas:
        glovebox()

    elif look_where.lower() in ["glove box", "glovebox"] and "GLOVEBOX" not in car_areas:
            print_smooth("You've already searched the GLOVEBOX!")
            find_phone_where()

    elif look_where.lower() in ["seats", "seat"] and "SEATS" in car_areas:
        seats()

    elif look_where.lower() in ["seats", "seat"] and "SEATS" not in car_areas:
            print_smooth("You've already searched the front SEATS!")
            find_phone_where()

    elif look_where.lower() in ["leave", "leave car", "leavecar", "leave the car"] and "LEAVE CAR" in car_areas:
        found_phone()

    else:
        fun.print_smooth("\n\nI'm not sure where that is.")
        find_phone_where()


def backseat():
    fun.print_smooth("\n\nYou crawl through to the backseat, avoiding cutting yourself open on the glass.\n\nThe "
                     "noxious smell in the air is still strong, as if something more than just your car is putting off"
                     " toxic fumes.\n\nYou know you don't want to be in here long. There is a FLASHLIGHT, but nothing "
                     "else.")
    car_areas.remove("BACK SEAT")
    take_flashlight = raw_input("\n\nTake FLASHLIGHT? Y or N? ")

    if take_flashlight.lower() in ["y", 'yes']:
        inventory.append("flashlight".upper())
        print_smooth('\n\n"This may come in handy later" you say to yourself. You check to make sure its working. Sure'
                     ' enough it is.\n\n***FLASHLIGHT added to inventory.***')
        find_phone_where()

    elif take_flashlight.lower() in ["n", "no"]:
        print_smooth("\n\nI really don't plan on going on a hike through this forest. I need to find my phone, not "
                     "grab a flashlight")
        find_phone_where()

    else:
        print_smooth("\n\nPlease enter Y or N")
        find_phone_where()


def glovebox():
    print_smooth('\n\nThe contents of the glovebox are scattered everywhere. With how bad the wreck is its possible'
                 ' its buried in all this paperwork.\n\nYou search through it all, but can\'t seem to find it. "GAAAHH'
                 '!!!!" you scream.\n\nThe fumes are starting to take their toll. "I need to find this phone!"' )
    car_areas.remove("GLOVEBOX")
    find_phone_where()


def seats():
    car_areas.remove("SEATS")
    print_smooth('"\n\nI never imagined looking under a seat while a car is upside down" you think to yourself.\n\nYou'
                 ' feel around both seats as best you can.\n\nAfter searching, you only find a strange black card, sim'
                 'ilar to a credit card, but with no numbers. It is simply all black.')
    take_black_card()

def take_black_card():
    take_card = raw_input("\n\nTake BLACK CARD? Y or N? ")

    if take_card.lower() in ["y", 'yes']:
        inventory.append("Black Card".upper())
        print_smooth('\n\n"What the hell is this thing?" You try to remember, but have no recollection of ever having '
                     'a card like this. Its not important right now, but you want to make sure you keep it so it doesn'
                     '\'t become lost after your car is eventually towed out of here.')
        time.sleep(1)
        raw_input("\n\nPress ENTER to add black card to inventory")
        time.sleep(.5)
        print_smooth("\n\n***BLACK CARD added to inventory***")
        time.sleep(1)
        find_phone_where()

    elif take_card.lower() in ["n", "no"]:
        print_smooth("\n\nI really don't plan on going on a hike through this forest. I need to find my phone, not "
                     "grab a flashlight")
        find_phone_where()

    else:
        print_smooth("\n\nPlease enter Y or N")
        take_black_card()

    find_phone_where()


def found_phone():
    print_smooth('\n\nThere isn\'t a chance in hell I\'m going to find my phone in here.\n\nYou begin to crawl back out'
                 ' of the car.\n\nAs you crawl out, you notice a glowing light about ten feet away.\n\n"Oh thank god!"'
                 ' you say aloud.')
    fun.sound_effect(cell_vibrate)
    print_smooth('\n\nYou can hear the phone vibrating. Someone is calling!')
    raw_input("\n\nPress Enter to answer phone!")
    fun.sound_effect(cell_vibrate, "n")
    fun.sound_effect(phone_static)
    pygame.mixer.fadeout(20000)
    answer_phone()


def answer_phone():
    fun.clear_screen()
    print_smooth('"Hello!" you say.\n\nYou find it odd that even in a time like this, a normalicy such as answe'
                 'ring "Hello" to a phone call is still habit.')
    time.sleep(1)
    print_smooth('\n\nYou hear a comforting voice coming through. "Son, is that you? Is everything alright?"\n\n"Mom!"'
                 ' you scream."Thank god Mom, i\'m so happy you called."')
    time.sleep(1)
    print_smooth('\n\n"Son what is going on? Is everything OK?"\n\nMy mother always had an overprotective personality,'
                 ' worried about everything that could go wrong. I loved her for it.')
    time.sleep(1)

    print_smooth('\n\n"Yeah Mom, I\'m fine. I was in a car accident, but I am ok."\n\n"Oh my boy!" she screamed."Where '
                 'are you, i\'ll call 911! Just tell me where y....re...no...llo?!')

    fun.sound_effect(cell_disconnect)
    pygame.mixer.fadeout(15000)
    time.sleep(2)

    print_smooth('\n\n"Mom!" you scream. "Mom hello!?"')

    fun.sound_effect(scary_piano)
    pygame.mixer.fadeout(50000)

    fun.print_slow('\n\n"I\'m here sTiLl son. I hAVen\'t left yOU. I\'ll cALl foR help." \n\n"Why Don\'T you gO inTo '
                   'the car wHEre itS saFe." \n\n"You KNow what thEy say, if yOu\'re loSt stay whERe you are ANd find '
                   'sheltER."')
    time.sleep(2)
    fun.clear_screen()

    print_smooth('The phone disconnects...')
    time.sleep(2)
    print_smooth('\n\n"What the hell??" you think to yourself. You try calling her back, but '
                 'there is no answer.\n\nYou try calling every number you know now, including 911, with no answer.'
                 '\n\nHer voice sounded so strange... It was my mom\'s voice, but different in an unexplainable way.')
    time.sleep(1)
    print_smooth('\n\nThe fumes should clear out here soon, and waiting for help may not be a bad idea considering I '
                 'could break my neck trying to get to the road.\n\nThe phone shows that its 12:06 AM. Morning'
                 ' is still going to be an unbearable amount of hours away.')
    wait_or_road()


def wait_or_road():
    wait_road = raw_input('\n\nShould I go back in the car and WAIT, or should I hike back up to the ROAD not far '
                          'away? ')

    if wait_road.lower() in ["stay", "wait"]:

        print_smooth('"\n\nYou walk back toward the car. Mother is right. I should wait inside where it is somewhat warmer."'
                     '\n\n"I\'ll have protection from wind there atleast." Everything about going back into the car feels'
                     ' wrong, but you can\'t seem to talk yourself out of it.\n\nYou reluctantly climb back in the car.')
        fun.sound_effect(suffocating_man)
        time.sleep(2)
        print_smooth('\n\nYou can hear your Mother\'s voice again through your phone. Its odd - you didn\'t answer it.')
        time.sleep(1)
        print_smooth('\n\n"Go to sleep boy. Morning will be here soon....."')
        time.sleep(2)
        died()


    elif wait_road.lower() in ["road"]:
        Road.road_path()

    else:
        print_smooth("\n\nPlease enter WAIT or ROAD.")
        wait_or_road()


def died():
    time.sleep(2)
    print('\n\n***YOU HAVE DIED***')
    time.sleep(2.5)
    try_again = raw_input('\n\nWould you like to try again? Y or N ')

    if try_again.lower() in ["yes", "y"]:
        fun.clear_screen()
        wait_or_road()

    elif try_again.lower() in ["no", "n"]:
        exit(0)

    else:
        print_smooth("\n\nPlease enter Y or N")
        died()
