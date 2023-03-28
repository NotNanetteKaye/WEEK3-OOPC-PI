# youtube video: https://www.youtube.com/watch?v=RcZsTI5h0kg

# coding HashMaps: Initializing the HashMap
city_map = {}
# OR
city_map1 = dict()

# coding HashMaps: Adding Data
cities = ['Calgary', 'Vancouver', 'Toronto']
city_map['Canada'] = [] # Initialize a new key everytime in HashMap
city_map['Canada'] += cities # Adding data to 'Canada' key

# coding HashMaps: Retrieving Data
# hashmap.keys() # will return all HashMap keys in a list
# hashmap.values() # will return all the HashMap values in a list
# hashmap.items() # will return all HashMap keys y values as a tuple

print(city_map.keys())
print(city_map.values())