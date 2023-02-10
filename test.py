from SimConnect import *
import launchpad_py as launchpad

from simconnect_mobiflight import SimConnectMobiFlight
from mobiflight_variable_requests import MobiFlightVariableRequests
from time import sleep

#set up launchpad

lp = launchpad.LaunchpadMk2()
lp.Open(0, "Launchpad Mk2")
lp.Reset()


while 1:
    buttons_pressed = lp.ButtonStateXY()

    if (buttons_pressed != []) :
        print(buttons_pressed[0], buttons_pressed[1], buttons_pressed[2])
        break



#lp.ledCtrlXY(4, 3, 0, 255, 0) #gear handle up position light
#lp.Reset()

















