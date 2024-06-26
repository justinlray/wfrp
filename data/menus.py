from data.character_data.character_details import Character
from data.character_data.skills import skill_dict
from data.character_data.talent import talent_dict
#from data.character_data.age_conversion import convert_age


def main_menu():
    print()
    main_menu_select = int(input('Enter selection: '))
    print()
    if main_menu_select == 1:
        new_character = Character()
        new_character.generate_player_character()
    elif main_menu_select == 2:
        print('Option forthcoming.')
    elif main_menu_select == 3:
        print('Skills accessed')
        display_skill()
    elif main_menu_select == 4:
        print('Talents accessed.')
        display_talent()
#   elif main_menu_select == 5:
#        print('Fantasy Racial Age Conversion')
#        convert_age()
    else:
        print('Please enter a valid selection.')


def display_skill():
    skill_select = input('Enter the skill you would like to view: ')
    print(skill_dict[skill_select])


def display_talent():
    talent_select = input('Enter the talent you would like to view: ')
    print(talent_dict[talent_select])
