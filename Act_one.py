import time
import os
import functions as fun
import Phone
from Road import road_path


car_crash = (os.path.join('soundeffects', 'carcrash.wav'))

def act_one():
    fun.clear_screen()
    fun.sound_effect(car_crash)
    time.sleep(8)
    print ("Your head throbs. The smell of radiator fluid and melting plastic is overpowering, making you feel naus"
          "eous. More than nauseous. You know you will pass out from the fumes if you dont get out of the car quickly."
          "\n\nBlood flows to the top of your head and your sense of gravity begins to come back.\n\nYou are upside down"
          ". There isn't a part of your body that doesnt hurt but you know you need to get out of the car. The glass in"
          " the door next to you is shattered and looks large enough to slip out of.\n\nYou unbuckle yourself and feel your"
          "self fall onto the inside roof of your car. You crawl out of the door window, and try to stand.\n\nIt is dark, "
          "and getting cold enough to worry. What should you do first?")
    time.sleep(1.5)
    go_where()


def go_where():
    road_or_phone = raw_input("\n\nDo you want to find your PHONE or head back to the ROAD for help? ")

    if road_or_phone.lower() in ["road"]:
        fun.print_smooth('\n\n"Once I leave here I won\'t be able to return."')

        r_u_sure = raw_input('\n\nAre you sure you want to head to the road without searching the car first? Y or N ')
        if r_u_sure.lower() in ["yes", "y"]:
            fun.clear_screen()
            road_path()

        elif r_u_sure.lower() in ["no", "n"]:
            go_where()

        else:
            fun.print_smooth("\n\nPlease enter Y or N")
            go_where()

    elif road_or_phone.lower() in ["phone"]:
        fun.clear_screen()
        Phone.find_phone()

    else:
        fun.print_smooth("\n\nPlease enter PHONE or ROAD.")
        go_where()



