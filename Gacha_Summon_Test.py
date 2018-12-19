#Gacha Summon Function Test
import random

#Function used to generate a summon randomly.  
#import random was used to decide which summon is selected by assiging a random value between 1-1000 and then selecting a summon based on that value.
monster_box = []
def summon_hero():
    summon_chance = (random.randint(1, 1000))
    mythic_heroes = ['', 'Mythic 2', 'Mythic 3']
    legendary_heroes = ['Legendary 1', 'Legendary 2', 'Legendary 3']
    epic_heroes = ['Epic 1', 'Epic 2', 'Epic 3']

    if summon_chance <= 17:
        print('Mythic Summon!')
        new_monster = mythic_heroes[random.randint(0, len(mythic_heroes)-1)]
        print(new_monster)
        print()
        monster_box.append(new_monster);
        
    elif summon_chance <= 200:
        print('Legendary Summon!')
        new_monster = legendary_heroes[random.randint(0, len(legendary_heroes)-1)]
        print(new_monster)
        print()
        monster_box.append(new_monster);

    elif summon_chance <= 1000:
        print('Epic Summon!')
        new_monster = epic_heroes[random.randint(0, len(epic_heroes)-1)]
        print(new_monster)
        print()
        monster_box.append(new_monster);
       
print('****Hello Summoner!****')
print('How would you like to proceed?\n')
print('1. Summon a Hero.')
print('2. Show summon rates.')
print('3. Show Monster Box')
print('4. Exit')

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
        print('****Your Monsters****')
        for items in monster_box:
            print(items)
    elif user_input == '4':
        print('Goodbye!')
        break
    
    user_input = input('Select Choice: ')
    print()
