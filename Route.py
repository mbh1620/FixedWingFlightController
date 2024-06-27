from calculationFunctions import getBearing, calculateDistanceBetweenCoordinates

class Route:

	def __init__(self, listOfWaypoints):

		self.listOfWaypoints = listOfWaypoints
		self.currentWaypointIndex = 0

	def getCurrentWaypoint(self):

		return self.listOfWaypoints[self.currentWaypointIndex]

	def increaseCurrentWaypointIndex(self):

		self.currentWaypointIndex += 1

	def calculateHeadingToCurrentWaypoint(self, currentGPSPosition):

		bearingToCoordinate = getBearing(currentGPSPosition[0], currentGPSPosition[1], self.listOfWaypoints[self.currentWaypointIndex][0], self.listOfWaypoints[self.currentWaypointIndex][1])

		return bearingToCoordinate

	def waypointReached(self, currentGPSPosition, toleranceDistance=0.005):

		distance = calculateDistanceBetweenCoordinates(currentGPSPosition[0], currentGPSPosition[1], self.listOfWaypoints[self.currentWaypointIndex][0], self.listOfWaypoints[self.currentWaypointIndex][1])

		if distance <= toleranceDistance:

			self.increaseCurrentWaypointIndex()

			return True

		else:

			return False

	def generateRoute(routeType, startingPosition):

		#routeType 
		pass


