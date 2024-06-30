
from FlightController import FlightController
from Waypoint import Waypoint

wpt1 = Waypoint(52.631970, -1.226045)
wpt2 = Waypoint(52.632441, -1.226059)
wpt3 = Waypoint(52.633088, -1.226965)

fc1 = FlightController([wpt1, wpt2, wpt3])

fc1.run()