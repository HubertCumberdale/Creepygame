import os
import sys
from sys import exit
from sys import stdout
import time
import pygame
from pygame.mixer import Sound
from pygame.mixer import stop as pystop


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_smooth(string):
    punctuation = [".", "!", "?"]

    for letter in string:
        stdout.write(letter)
        time.sleep(.000005)
        stdout.flush()

        if letter in punctuation:
            time.sleep(.5)
        else:
            time.sleep(.035)
    print ("")


def print_slow(string):
    punctuation = [".", "!", "?"]

    for letter in string:
        stdout.write(letter)
        time.sleep(.1)
        stdout.flush()

        if letter in punctuation:
            time.sleep(.5)
        else:
            time.sleep(.035)
    print("")


def way_slow_print(string):
    punctuation = [".", "!", "?"]

    for letter in string:
        stdout.write(letter)
        time.sleep(.7)
        stdout.flush()

        if letter in punctuation:
            time.sleep(.7)
        else:
            time.sleep(.05)
    print ("")


def sound_effect(whataudio, start="y", numberofloops=0):
    pygame.mixer.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    Sound(whataudio)
    current_sound = Sound(whataudio)
    start = start.lower()
    if start == "y":
        current_sound.play(loops=numberofloops)
    elif start == "n":
        current_sound.stop()
    else:
        print "Error: Need to select play music Y or N"


def music(whataudio):
    pygame.mixer.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    pygame.mixer.music.load(whataudio)
    pygame.mixer.music.play()


def soundtest():
    pygame.mixer.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    Sound(os.path.join('soundeffects', 'cellvibrate.wav'))
