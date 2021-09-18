# Cesar Hernandez 1835494

lem_juice = float(input('Enter amount of lemon juice (in cups):\n'))

water = float(input('Enter amount of water (in cups):\n'))

agave_nect = float(input('Enter amount of agave nectar (in cups):\n'))

servings = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')

print('{:.2f}'.format(lem_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave_nect), 'cup(s) agave nectar\n')

new_servings = float(input('How many servings would you like to make?\n'))

constant = new_servings/servings # constant to find new servings

print('\nLemonade ingredients - yields', '{:.2f}'.format(new_servings), 'servings')

print('{:.2f}'.format(lem_juice*constant), 'cup(s) lemon juice')
print('{:.2f}'.format(water*constant), 'cup(s) water')
print('{:.2f}'.format(agave_nect*constant), 'cup(s) agave nectar')

gallon_const = 16

print('\nLemonade ingredients - yields', '{:.2f}'.format(new_servings), 'servings')

print('{:.2f}'.format(lem_juice*constant/gallon_const), 'gallon(s) lemon juice')
print('{:.2f}'.format(water*constant/gallon_const), 'gallon(s) water')
print('{:.2f}'.format(agave_nect*constant/gallon_const), 'gallon(s) agave nectar')