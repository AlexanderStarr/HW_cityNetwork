#Alexander Starr
#22C:016:A01
#00567613

def createDistanceMatrix():
    # Creates a list of city names and a 128 x 128 matrix of distances,
    # in which the value at distances[i][j] is the distance between
    # the two cities at index i and j in the names list.
    names = []   # Initializes the names list
    distances = []   # Initializes the distance matrix to be empty
    for row in range(128):
        # Fills the distance matrix with 128 rows, each containing 128 zeroes.
        distances.append([0]*128)
        
    f = open("miles.dat", "r")
    line = f.readline().strip()
    while line[0] == "*":
        # This skips the header lines, which all start with a *.
        line = f.readline().strip()
    
    expectedDistances = 0
    while line[0] != "*":
        # This while loop encompasses the file to be scanned, it will continue
        # executing until the end-of-file line is reached (starts with *).
        # Each time through this loop corresponds to the information for one
        # city, so first the city name is recorded, then the mileages extracted.
        names.append(getCityName(line)) # Adds city name to the names list
        line = f.readline().strip() # Get the next line, which contains mileages
        
        distances_recorded = 0
        current_city_distances = []
        while distances_recorded < expectedDistances:
            # Gets all of the mileages associated with the current city and
            # stores them as a list to be used later.  Because mileages can
            # span multiple lines, it is necessary to keep track of the number
            # recorded and get the next line if there are more to be recorded.
            miles_in_line = getMileages(line)
            current_city_distances.extend(miles_in_line)
            distances_recorded = distances_recorded + len(miles_in_line)
            line = f.readline().strip()
            
        i = len(current_city_distances)
        j = i - 1
        for dist in current_city_distances:
            # This puts the mileages into the distances matrix.
            distances[i][j] = dist
            distances[j][i] = dist
            j = j - 1
        expectedDistances = expectedDistances + 1
        
    f.close()
    return names, distances

def getCityName(line):
    # Receives as an argument a line containing a city name with the latitude,
    # longitude, and population.  The latitude and longitude are always
    # contained in brackets immediately following the city and state.
    # This is exploited to split the string to get the city name.
    city_comma_state = line.split("[")[0]
    city, state = city_comma_state.split(", ")
    city_state = city + " " + state
    return city_state

def getMileages(line):
    # Receives a line with the mileages separated by spaces.  Returns a list
    # with the mileages as integers.
    mileages = map(int, line.split())
    return mileages

def createCityNetwork(cityList, distances, r):
    # Creates/returns a network of cities and their neighbors, as defined by the
    # distance r.  So network[city] should evaluate to a list of cities that are
    # no farther than r miles away from city
    network = {} # Initializes the network to an empty dictionary
    for city in cityList:
        # Adds cities and their neighbors to the network
        network[city] = findNeighbors(cityList, distances, r, city)
    return network

def findNeighbors(cityList, distances, r, city):
    # Takes a cityList, a distances matrix, a value r, and a city, then 
    # returns a list of all the cities which are no further than r miles away.
    neighbors = []
    city_index = cityList.index(city)
    distance_list = distances[city_index]
    for i in range(len(distance_list)):
        # Searches the sublist of the matrix distances that contains the 
        # distances city is from each other city.  Adds that city to
        # the list neighbors if it is close enough.
        if distance_list[i] <= r:
            neighbors.append(cityList[i])
    
    return neighbors

cityList, distances = createDistanceMatrix()