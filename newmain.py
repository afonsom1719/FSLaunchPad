from SimConnect import *
import logging
from SimConnect.Enum import *
from time import sleep
import launchpad_py as launchpad
from simconnect_mobiflight import SimConnectMobiFlight
from mobiflight_variable_requests import MobiFlightVariableRequests

#set up simconnect

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)
LOGGER.info("START")
# time holder for inline commands
ct_g = millis()

# create simconnection and pass used user classes
sm = SimConnect()
aq = AircraftRequests(sm)
ae = AircraftEvents(sm)
smm = SimConnectMobiFlight()
vr = MobiFlightVariableRequests(smm)
vr.clear_sim_variables()



#set up launchpad

lp = launchpad.LaunchpadMk2()
lp.Open(0, "Launchpad Mk2")

while 1:

    #get the buttons pressed for each interaction

    buttons_pressed = lp.ButtonStateXY()

    #LANDING GEAR

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

    #AUTOBRAKE

    autobrake_pos = vr.get("(L:A32NX_AUTOBRAKES_ARMED_MODE)")
    print(autobrake_pos)

    if autobrake_pos == 0:
        lp.LedCtrlXY(3, 2, 0, 0, 0)
        lp.LedCtrlXY(4, 2, 0, 0, 0)
        lp.LedCtrlXY(5, 2, 0, 0, 0)
    elif autobrake_pos == 1:
        lp.LedCtrlXY(3, 2, 0, 0, 255)
        lp.LedCtrlXY(4, 2, 0, 0, 0)
        lp.LedCtrlXY(5, 2, 0, 0, 0)
    elif autobrake_pos == 2:
        lp.LedCtrlXY(3, 2, 0, 0, 0)
        lp.LedCtrlXY(4, 2, 0, 0, 255)
        lp.LedCtrlXY(5, 2, 0, 0, 0)
    elif autobrake_pos == 3:
        lp.LedCtrlXY(3, 2, 0, 0, 0)
        lp.LedCtrlXY(4, 2, 0, 0, 0)
        lp.LedCtrlXY(5, 2, 0, 0, 255)

    if (buttons_pressed != []) :
        print(buttons_pressed[0], buttons_pressed[1])
        if (buttons_pressed[0] == 3 and buttons_pressed[1] == 2):
            if (autobrake_pos == 0):
                vr.set("1 (>L:A32NX_AUTOBRAKES_ARMED_MODE_SET)")
                break
            elif (autobrake_pos == 1):
                vr.set("0 (>L:A32NX_AUTOBRAKES_ARMED_MODE_SET)")
                break
        elif (buttons_pressed[0] == 4 and buttons_pressed[1] == 2):
            if (autobrake_pos == 0):
                vr.set("2 (>L:A32NX_AUTOBRAKES_ARMED_MODE_SET)")
                break
            elif (autobrake_pos == 2):
                vr.set("0 (>L:A32NX_AUTOBRAKES_ARMED_MODE_SET)",)
                break
        
        elif (buttons_pressed[0] == 5 and buttons_pressed[1] == 2):
            if (autobrake_pos == 0):
                vr.set("3 (>L:A32NX_AUTOBRAKES_ARMED_MODE_SET)")
                break
            elif (autobrake_pos == 4):
                vr.set("0 (>L:A32NX_AUTOBRAKES_ARMED_MODE_SET)")
                break

               

 
























