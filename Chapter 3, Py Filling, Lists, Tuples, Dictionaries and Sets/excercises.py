# 3.1
years_list = [1989, 1990, 1991, 1992, 1993, 1994]

# 3.2
years_list[3]

# 3.3
years_list[-1]

# 3.4
things = ["mozzarella", "cinderella", "salmonella"]
things

# 3.5
things[1].capitalize()
things

# 3.6
things[0] = things[0].upper()
things

# 3.7
things.pop(2)
things

# 3.8
surprise = ["Groucho", "Chico", "Harpo"]
surprise

# 3.9
surprise[-1] = surprise[-1].lower()
surprise
surprise[-1] = surprise[-1][::-1]
surprise
surprise[-1] = surprise[-1].capitalize()
surprise

# 3.10
e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
e2f

# 3.11
e2f['walrus']

# 3.12
f2e = {}
for english, french in e2f.items():
    f2e[french] = english
f2e

# 3.13
f2e['chien']

# 3.14
set(e2f.keys())

# 3.15
life = {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'],
                    'octopi': {},
                    'emus': {}},
        'plants': {},
        'other': {}
        }
life

# 3.16
print(life.keys())

print(list(life.keys()))

# 3.17
print(life['animals'].keys())

# 3.18
print(life['animals']['cats'])
