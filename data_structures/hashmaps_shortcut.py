# using DefaultDic will already instantiate all keys
from collections import defaultdict

city_map = defaultdict(list)
cities = ['Calgary', 'Toronto', 'Vancouver']
city_map['Canada'] += cities # we skipped instantiation of 'Canada'!

# Python has a huge library - USE IT!!! especially in coding problems