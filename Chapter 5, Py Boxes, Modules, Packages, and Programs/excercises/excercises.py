# 5.1
# see zoo.py

# 5.2
from collections import defaultdict
from collections import OrderedDict
from zoo import hours
import zoo as menagerie
import zoo
zoo.hours()

# 5.3
menagerie.hours()

# 5.4
hours()

# 5.5
plain = {'a': 1, 'b': 2, 'c': 3}
plain

# 5.6
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
fancy

# 5.7
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
dict_of_lists['a']
