from SimConnect import *
import logging
from SimConnect.Enum import *
from time import sleep
import launchpad_py as launchpad

#set up simconnect

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)
LOGGER.info("START")
# time holder for inline commands
ct_g = millis()

# creat simconnection and pass used user classes
sm = SimConnect()
aq = AircraftRequests(sm)
ae = AircraftEvents(sm)

#set up launchpad

lp = launchpad.LaunchpadMk2()
lp.Open(0, "Launchpad Mk2")

while 1:

    #get the buttons pressed for each interaction

    buttons_pressed = lp.ButtonStateXY()

    #landing gear

    lg_handle = aq.get("GEAR_HANDLE_POSITION")
    lg_percent = aq.get("GEAR_TOTAL_PCT_EXTENDED")

    if lg_handle == 0:
        lp.LedCtrlXY(4, 3, 10, 10, 10) 
        lp.LedCtrlXY(4, 4, 0, 0, 0) 
    elif lg_handle == 1:
        lp.LedCtrlXY(4, 3, 0, 0, 0) 
        lp.LedCtrlXY(4, 4, 10,10,10)
    if lg_percent == 0:
        lp.LedCtrlXY(3, 1, 255, 0, 0)
        lp.LedCtrlXY(4, 1, 255, 0, 0)
        lp.LedCtrlXY(5, 1, 255, 0, 0)
    if lg_percent == 1:
        lp.LedCtrlXY(3, 1, 0, 255, 0)
        lp.LedCtrlXY(4, 1, 0, 255, 0)
        lp.LedCtrlXY(5, 1, 0, 255, 0)

    if (buttons_pressed != []) :
        print(buttons_pressed[0], buttons_pressed[1])
        if (buttons_pressed[0] == 4 and buttons_pressed[1] == 4):
            print("Lowering gear...")
            #set gear handle position to 1
            trigger_event = ae.find("GEAR_DOWN")
            trigger_event()
        if (buttons_pressed[0] == 4 and buttons_pressed[1] == 3):
            print("Gear up...")
            #set gear handle position to 1
            trigger_event = ae.find("GEAR_UP")
            trigger_event() 
 
























