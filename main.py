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

# example
#mc = aq.find("MAGNETIC_COMPASS")
#mv = aq.find("MAGVAR")
#print(mc.get() + mv.get())

#set up launchpad

lp = launchpad.LaunchpadMk2()
lp.Open(0, "Launchpad Mk2")









#landing gear vars

while 1:
    buttons_pressed = lp.ButtonStateXY()

    if (buttons_pressed != []) :
        print(buttons_pressed[0], buttons_pressed[1], buttons_pressed[2])
        if (buttons_pressed[0] == 4 and buttons_pressed[1] == 4):
            print("success")
            #set gear handle position to 1
            trigger_event = ae.find("GEAR_DOWN")
            trigger_event()
            break



lg_handle = aq.get("GEAR_HANDLE_POSITION")
# print(lg_handle == 1) returning true
lg_percent = aq.get("GEAR_TOTAL_PCT_EXTENDED")







#set up the leds on the launchpad for the gear, if handle is off, show red led 

if lg_handle == 0:
    lp.LedCtrlXY(4, 3, 10, 10, 10) #gear handle up position light
    lp.LedCtrlXY(4, 4, 0, 0, 0) #gear handle down position light

elif lg_handle == 1:
    lp.LedCtrlXY(4, 3, 0, 0, 0) #gear handle up position light
    lp.LedCtrlXY(4, 4, 10,10,10) #gear handle down position light

if lg_percent == 0:
    #set color as red for the 3 landing gear annunciator lights and a light to simulate gear handle position (up/down)
    lp.LedCtrlXY(3, 1, 255, 0, 0)
    lp.LedCtrlXY(4, 1, 255, 0, 0)
    lp.LedCtrlXY(5, 1, 255, 0, 0)
if lg_percent == 1:
    #set color as green for the 3 landing gear annunciator lights and a light to simulate gear handle position (up/down)
    lp.LedCtrlXY(3, 1, 0, 255, 0)
    lp.LedCtrlXY(4, 1, 0, 255, 0)
    lp.LedCtrlXY(5, 1, 0, 255, 0)


#autobrake vars

ab_pos = aq.get("AUTO_BRAKE_SWITCH_CB")

print(ab_pos)

#set up the leds on the launchpad for the autobrake, if it is off, show nothing
#if it is in low, show a blue led on 5,2
#if it is in medium, show a blue led on 6,2
#if it is in max, show a blue led on 7,2

if ab_pos == 1:
    lp.LedCtrlXY(3, 2, 0, 0, 0)
    lp.LedCtrlXY(4, 2, 0, 0, 0)
    lp.LedCtrlXY(5, 2, 0, 0, 0)

elif ab_pos == 2:
    lp.LedCtrlXY(3, 2, 0, 0, 255)
    lp.LedCtrlXY(4, 2, 0, 0, 0)
    lp.LedCtrlXY(5, 2, 0, 0, 0)

elif ab_pos == 3:   
    lp.LedCtrlXY(3, 2, 0, 0, 0)
    lp.LedCtrlXY(4, 2, 0, 0, 255)
    lp.LedCtrlXY(5, 2, 0, 0, 0)

elif ab_pos == 4:
    lp.LedCtrlXY(3, 2, 0, 0, 0)
    lp.LedCtrlXY(4, 2, 0, 0, 0)
    lp.LedCtrlXY(5, 2, 0, 0, 255)


#flaps vars

flaps_pos = aq.get("FLAPS_HANDLE_INDEX") #from 0 to 4, off, 1, 2 ,3, full

#set up the leds on the launchpad for the flaps, if it is off, show a grey led on 6, 4, if it is 1, show the led on 6, 5, if it is 2, show the led on 6, 6, if it is 3, show the led on 6, 7, if it is 4, show the led on 6, 8

if flaps_pos == 0:
    lp.LedCtrlXY(6, 4, 64, 64, 64)
    lp.LedCtrlXY(6, 5, 0, 0, 0)
    lp.LedCtrlXY(6, 6, 0, 0, 0)
    lp.LedCtrlXY(6, 7, 0, 0, 0)
    lp.LedCtrlXY(6, 8, 0, 0, 0)

elif flaps_pos == 1:
    lp.LedCtrlXY(6, 4, 0, 0, 0)
    lp.LedCtrlXY(6, 5, 64, 64, 64)
    lp.LedCtrlXY(6, 6, 0, 0, 0)
    lp.LedCtrlXY(6, 7, 0, 0, 0)
    lp.LedCtrlXY(6, 8, 0, 0, 0)

elif flaps_pos == 2:
    lp.LedCtrlXY(6, 4, 0, 0, 0)
    lp.LedCtrlXY(6, 5, 0, 0, 0)
    lp.LedCtrlXY(6, 6, 64, 64, 64)
    lp.LedCtrlXY(6, 7, 0, 0, 0)
    lp.LedCtrlXY(6, 8, 0, 0, 0)

elif flaps_pos == 3:
    lp.LedCtrlXY(6, 4, 0, 0, 0)
    lp.LedCtrlXY(6, 5, 0, 0, 0)
    lp.LedCtrlXY(6, 6, 0, 0, 0)
    lp.LedCtrlXY(6, 7, 64, 64, 64)
    lp.LedCtrlXY(6, 8, 0, 0, 0)

elif flaps_pos == 4:
    lp.LedCtrlXY(6, 4, 0, 0, 0)
    lp.LedCtrlXY(6, 5, 0, 0, 0)
    lp.LedCtrlXY(6, 6, 0, 0, 0)
    lp.LedCtrlXY(6, 7, 0, 0, 0)
    lp.LedCtrlXY(6, 8, 64, 64, 64)


#parking brake vars

pb_pos = aq.get("BRAKE_PARKING_POSITION")

#set up the leds on the launchpad for the parking brake, if it is off, show nothing, if it is on, show a red led on 7, 6

if pb_pos == 0:
    lp.LedCtrlXY(7, 6, 0, 0, 0)

elif pb_pos == 1:
    lp.LedCtrlXY(7, 6, 255, 0, 0)















