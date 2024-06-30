import math

def getBearing(lat1, long1, lat2, long2):

	#Taken from nautical_calculations library

    lat1 = float(lat1); long1 = float(long1);  lat2 = float(lat2); long2 = float(long2)
    startlat = math.radians(lat1)
    startlong = math.radians(long1)
    endlat = math.radians(lat2)
    endlong = math.radians(long2)
    dlong = endlong - startlong
    dPhi = math.log(math.tan(endlat / 2.0 + math.pi / 4.0) / math.tan(startlat / 2.0 + math.pi / 4.0))

    if abs(dlong) > math.pi:
        if dlong > 0.0:
            dlong = -(2.0 * math.pi - dlong)
        else:
            dlong = (2.0 * math.pi + dlong)
    bearing = (math.degrees(math.atan2(dlong, dPhi)) + 360.0) % 360.0;
    return bearing

def calculateDistanceBetweenCoordinates(lat1, long1, lat2, long2):

	lat1 = float(lat1)
	long1 = float(long1)
	lat2 = float(lat2)
	long2 = float(long2)

	R = 6371 # Radius of earth in metres
	
	lat1rads = math.radians(lat1)
	lat2rads = math.radians(lat2)
	deltalat = math.radians((lat2 - lat1))
	deltalong = math.radians((long2 - long1))
	
	a = math.sin(deltalat / 2) * math.sin(deltalat / 2) + math.cos(lat1rads) * math.cos(lat2rads) * math.sin(deltalong / 2) * math.sin(deltalong / 2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
	d = R * c

	return d

