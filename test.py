from SimConnect import *
import launchpad_py as launchpad

from simconnect_mobiflight import SimConnectMobiFlight
from mobiflight_variable_requests import MobiFlightVariableRequests
from time import sleep

#set up launchpad

lp = launchpad.LaunchpadMk2()
lp.Open(0, "Launchpad Mk2")
lp.Reset()


smm = SimConnectMobiFlight()
vr = MobiFlightVariableRequests(smm)
vr.clear_sim_variables()



autobrake_pos = vr.get("(L:A32NX_AUTOBRAKES_ARMED_MODE)")
ap1 = vr.get("(L:A32NX_AUTOPILOT_1_ACTIVE)")
print(ap1)

















