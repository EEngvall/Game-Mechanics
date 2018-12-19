#Gacha Summon Function Test
import random
def summon_hero():
    summon_chance = (random.randint(1, 1000))
    mythic_heroes = ['Mythic 1', 'Mythic 2', 'Mythic 3']
    legendary_heroes = ['Legendary 1', 'Legendary 2', 'Legendary 3']
    epic_heroes = ['Trash', 'More Trash', 'Epic Trash']
    if summon_chance <= 17:
        print('Mythic Summon!')
        print(mythic_heroes[random.randint(0, len(mythic_heroes)-1)])
    elif summon_chance <= 200:
        print('Legendary Summon!')
        print(legendary_heroes[random.randint(0, len(legendary_heroes)-1)])

    elif summon_chance <= 1000:
        print('Epic Summon!')
        print(epic_heroes[random.randint(0, len(epic_heroes)-1)])


print('Hello Summoner!')
print('How would you like to proceed?\n')
print('1. Summon a Hero.')
print('2. Show summon rates.')
print('3. To Exit')
user_input = input()
print()
while user_input != 'Q' or 'q':

    if user_input == '1':
        summon_hero()
    elif user_input == '2':
        print('Epic Hero: 78.3%')
        print('Legendary Hero: 18.3%')
        print('Legendary Hero: 1.7%')
    elif user_input == '3':
        print('Goodbye!')
        break
    
    user_input = input('Select Choice: \n')
    print()
