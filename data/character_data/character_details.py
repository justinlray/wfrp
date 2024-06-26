from data.character_data.universal_charts import distinguishing_marks, star_sign, dooming

class Character:
  def __init__(self):
    self.character_details = {
      'Player Name': '',
      'Character Name': '',
      'Player ID': 0,
      'Character ID': 0,
      'Race': '',
      'Current Career': '',
      'Previous Careers': '',
      'Current Experience Points': 0,
      'Total Experience Points': 0
    }
    self.personal_details = {
      'Age': 0,
      'Gender': 0,
      'Eye Colour': '',
      'Hair Colour': '',
      'Weight': 0,
      'Height': 0,
      'Star Sign': '',
      'Number of Siblings': 0,
      'Birthplace': '',
      'Distinguishing Marks': '',
      'Dooming': ''
    }
    self.main_profile = {
      'Weapon Skill': 0,
      'Ballistic Skill': 0,
      'Strength': 0,
      'Toughness': 0,
      'Agility': 0,
      'Intelligence': 0,
      'Willpower': 0,
      'Fellowship': 0
    }
    self.secondary_profile = {
      'Attacks': 0,
      'Wounds': 0,
      'Strength Bonus': 0,
      'Toughness Bonus': 0,
      'Movement': 0,
      'Magic': 0,
      'Insanity Points': 0,
      'Fate Points': 0
    }
    self.weapons = []
    self.armour = []
    self.skills = {}
    self.talents = []
    self.trappings = {}
    self.money = {
      'Gold Crowns': 0,
      'Silver Schillings': 0,
      'Brass Pennies': 0
    }
    self.spell_grimoire = {}

  def __repr__(self):
    return repr(self.character_details['Character Name'])
    return repr(self.character_details['Race'])

  def update_skills(self, skill):
    self.skills[skill] = 'Trained'
  
  def update_talents(self, talent):
    self.talents.append(talent)

  def generate_player_character(self):
    print('Generating Player Character (PC)')
    self.character_details['Player Name'] = str(input("Enter the player's name: "))

  
    #Selecting Race, Birthplace
    print('''\nStandard Player Race options:\n
    1. Dwarf
    2. Halfling
    3. High Elf
    4. Human
    5. Wood Elf\n''')
    race_selection = int(input("Enter the number of your selection: "))
    if race_selection == 1:
      self.character_details['Race'] = 'Dwarf'
      print("Dwarf has been selected.\n")
      from data.character_data.races.dwarf_char_creation import characteristic_base, starting_wounds, starting_fate_points, starting_skills, starting_talents, female_height_base, male_height_base, weight_table, hair_colour, eye_colour, number_of_siblings, age, dwarf_birthplace, female_names, male_names
      new_d10 = int(input('Roll 1d10 and enter it here: '))
      if new_d10 < 4:
        print('Your character was born within the boundaries of the Empire.')
        from data.character_data.races.human_char_creation import birthplace_state, birthplace_local
        new_d10 = int(input('Roll 1d10 and enter it here: '))
        new_d10_2 = int(input('Roll 1d10 and enter it here: '))
        self.personal_details['Birthplace'] = birthplace_state[new_d10], birthplace_local[new_d10_2]
        print('Your character was born in a ' + self.personal_details['Birthplace'][1] + ' in the region of ' + self.personal_details['Birthplace'][0] + '\n')
      else:
        self.personal_details['Birthplace'] = dwarf_birthplace[new_d10]
        print('Your character was born in ' + self.personal_details['Birthplace'])
    elif race_selection == 2:
      self.character_details['Race'] = 'Halfling'
      print("Halfling has been selected.\n")
      from data.character_data.races.halfling_char_creation import characteristic_base, starting_wounds, starting_fate_points, starting_skills, starting_talents, random_talents, female_height_base, male_height_base, weight_table, hair_colour, eye_colour, number_of_siblings, age, halfling_birthplace, female_names, male_names
      new_d10 = int(input('Roll 1d10 and enter it here: '))
      if new_d10 > 5:
        print('Your character was born within the boundaries of the Empire.')
        from data.character_data.races.human_char_creation import birthplace_state, birthplace_local
        new_d10 = int(input('Roll 1d10 and enter it here: '))
        new_d10_2 = int(input('Roll 1d10 and enter it here: '))
        self.personal_details['Birthplace'] = birthplace_state[new_d10], birthplace_local[new_d10_2]
        print('Your character was born in a ' + self.personal_details['Birthplace'][1] + ' in the region of ' + self.personal_details['Birthplace'][0] + '\n')
      else:
        self.personal_details['Birthplace'] = halfling_birthplace[new_d10]
        print('Your character was born in ' + self.personal_details['Birthplace'])
    elif race_selection == 3:
      self.character_details['Race'] = 'High Elf'
      print("High Elf has been selected.\n")
      from data.character_data.races.high_elf_char_creation import characteristic_base, starting_wounds, starting_fate_points, starting_skills, starting_talents, female_height_base, male_height_base, weight_table, hair_colour, eye_colour, number_of_siblings, age, high_elf_birthplace, female_names, male_names
      new_d10 = int(input('Roll 1d10 and enter it here: '))
      self.personal_details['Birthplace'] = high_elf_birthplace[new_d10]
      print('Your character was born in ' + self.personal_details['Birthplace'])
    elif race_selection == 4:
      self.character_details['Race'] = 'Human'
      print("Human has been selected.\n")
      from data.character_data.races.human_char_creation import characteristic_base, starting_wounds, starting_fate_points, starting_skills, starting_talents, random_talents, female_height_base, male_height_base, weight_table, hair_colour, eye_colour, number_of_siblings, age, birthplace_state, birthplace_local, female_names, male_names
      new_d10 = int(input('Roll 1d10 and enter it here: '))
      new_d10_2 = int(input('Roll 1d10 and enter it here: '))
      self.personal_details['Birthplace'] = birthplace_state[new_d10], birthplace_local[new_d10_2]
      print('Your character was born in a ' + self.personal_details['Birthplace'][1] + ' in the region of ' + self.personal_details['Birthplace'][0] + '\n')
      new_d100 = int(input('Roll 1d100 and enter it here: '))
      self.personal_details['Dooming'] = dooming[new_d100]
      print("On your character's tenth birthday, a priest of Morr or an elder prophesied how you would meet your end. This is what you remember them saying:")
      print(self.personal_details['Dooming'])
    elif race_selection == 5:
      self.character_details['Race'] = 'Wood Elf'
      print("Wood Elf has been selected.\n")
      from data.character_data.races.wood_elf_char_creation import characteristic_base, starting_wounds, starting_fate_points, starting_skills, starting_talents, female_height_base, male_height_base, weight_table, hair_colour, eye_colour, number_of_siblings, age, wood_elf_birthplace, female_names, male_names
      new_d10 = int(input('Roll 1d10 and enter it here: '))
      if new_d10 == 1:
        print('Your character was born within the boundaries of the Empire.')
        from data.character_data.races.human_char_creation import birthplace_state, birthplace_local
        new_d10 = int(input('Roll 1d10 and enter it here: '))
        new_d10_2 = int(input('Roll 1d10 and enter it here: '))
        self.personal_details['Birthplace'] = birthplace_state[new_d10], birthplace_local[new_d10_2]
        print('Your character was born in a ' + self.personal_details['Birthplace'][1] + ' in the region of ' + self.personal_details['Birthplace'][0] + '\n')
        pass
      else:
        self.personal_details['Birthplace'] = wood_elf_birthplace[new_d10]
        print('Your character was born in ' + self.personal_details['Birthplace'])
    else:
      "This is not a valid selection.\n"
  
  
    #Generating Main Profile Characteristics 
    print("Generating Main Profile\n")
    self.main_profile['Weapon Skill'] = int(input('Roll 2d10 and add them together: ')) + characteristic_base['Weapon Skill']
    print('Your Weapon Skill is ' + str(self.main_profile['Weapon Skill']) + '\n')
    self.main_profile['Ballistic Skill'] = int(input('Roll 2d10 and add them together: ')) + characteristic_base['Ballistic Skill']
    print('Your Ballistic Skill is ' + str(self.main_profile['Ballistic Skill']) + '\n')
    self.main_profile['Strength'] = int(input('Roll 2d10 and add them together: ')) + characteristic_base['Strength']
    print('Your Strength is ' + str(self.main_profile['Strength']) + '\n')
    self.main_profile['Toughness'] = int(input('Roll 2d10 and add them together: ')) + characteristic_base['Toughness']
    print('Your Toughness is ' + str(self.main_profile['Toughness']) + '\n')
    self.main_profile['Agility'] = int(input('Roll 2d10 and add them together: ')) + characteristic_base['Agility']
    print('Your Agility is ' + str(self.main_profile['Agility']) + '\n')
    self.main_profile['Intelligence'] = int(input('Roll 2d10 and add them together: ')) + characteristic_base['Intelligence']
    print('Your Intelligence is ' + str(self.main_profile['Intelligence']) + '\n')
    self.main_profile['Willpower'] = int(input('Roll 2d10 and add them together: ')) + characteristic_base['Willpower']
    print('Your Willpower is ' + str(self.main_profile['Willpower']) + '\n')
    self.main_profile['Fellowship'] = int(input('Roll 2d10 and add them together: ')) + characteristic_base['Fellowship']
    print('Your Fellowship is ' + str(self.main_profile['Fellowship']) + '\n')
    input('The Main Profile is complete. Press enter to proceed.\n')
    
    #Generating Secondary Profile
    print('Generating Secondary Profile\n')
    self.secondary_profile['Attacks'] = characteristic_base['Attacks']
    print('Your Attack value is equal to ' + str(self.secondary_profile['Attacks']) + '\n')
    #Wounds
    new_roll = int(input('Roll 1d10: '))
    self.secondary_profile['Wounds'] = starting_wounds[new_roll]
    print('Your Wounds are equal to ' + str(starting_wounds[new_roll]) + '\n')
    input('Press enter to proceed.\n')
    self.secondary_profile['Strength Bonus'] = self.main_profile['Strength'] // 10
    print('Your Strength Bonus is ' + str(self.secondary_profile['Strength Bonus']) + '\n')
    input('Press enter to proceed.\n')
    self.secondary_profile['Toughness Bonus'] = self.main_profile['Toughness'] // 10
    print('Your Toughness Bonus is ' + str(self.secondary_profile['Toughness Bonus']) + '\n')
    input('Press enter to proceed.\n')
    self.secondary_profile['Movement'] = characteristic_base['Movement']
    print('Your Movement is ' + str(self.secondary_profile['Movement']) + '\n')
    input('Press enter to proceed.\n')
    self.secondary_profile['Magic'] = characteristic_base['Magic']
    print('Your Magic is ' + str(self.secondary_profile['Magic']) + '\n')
    input('Press enter to proceed.\n')
    self.secondary_profile['Insanity Points'] = characteristic_base['Insanity Points']
    print('Your Insanity Points value is equal to ' + str(self.secondary_profile['Insanity Points']) + '\n')
    input('Press enter to proceed.\n')
    new_roll = int(input('Roll 1d10: '))
    self.secondary_profile['Fate Points'] = starting_fate_points[new_roll]
    print('Your Fate Points are equal to ' + str(starting_fate_points[new_roll]) + '\n')
    input('The Secondary Profile is complete. Press enter to proceed.\n')
  
    #Add starting Skills
    print('You gain the following Skills:')
    for sk in starting_skills:
      if type(sk) == str:
        print(sk)
        self.update_skills(sk)
      elif type(sk) == list:
        print('\nYou may choose one of the following:')
        counter = 1
        for s in sk:
          print(str(counter) + '. ' + s)
          counter = counter + 1
        skill_select = (int(input('Enter the number for your selection: ')) - 1)
        if (skill_select + 1) > len(sk):
          skill_select = (input('Please enter a valid number: ')) - 1
        self.update_skills(sk[skill_select])
        print('\nAdding chosen Skill.\n')
    
    #Add starting Talents
    print('You gain the following Talents:')
    for tal in starting_talents:
      if type(tal) == str:
        print(tal)
        self.update_talents(tal)
      elif type(tal) == list:
        print('\nYou may choose one of the following:')
        counter = 1
        for t in tal:
          print(str(counter) + '. ' + t)
          counter = counter + 1
        talent_select = (int(input('Enter the number for your selection: ')) - 1)
        if (talent_select + 1) > len(sk):
          talent_select = (input('Please enter a valid number: ')) - 1
        self.update_talents(tal)
        print('You gain the chosen Talent: ' + tal[talent_select])
    else:
      pass
  
    if self.character_details['Race'] == 'Halfling':
      new_d100 = int(input('Roll a d100 and input the result: '))
      print('You gain the following random Talent: ' + random_talents[new_d100])
    elif self.character_details['Race'] == 'Human':
      new_d100 = int(input('Roll a d100 and input the result: '))
      print('You gain the following random Talent: ' + random_talents[new_d100])
      new_d100 = int(input('Roll a d100 and input the result: '))
      print('You gain the following random Talent: ' + random_talents[new_d100])
  
  
    #Gender
    print('''\n
    What is the character's gender?
    1. Male
    2. Female
    ''')
    new_choice = int(input('Enter your selection: '))
    if new_choice == 1:
      self.personal_details['Gender'] = "Male"
    elif new_choice == 2:
      self.personal_details['Gender'] = "Female"
  
    #Name
    print('''\n
    What is the character's name?
    1. Choose new name
    2. Randomly select name
    ''')
    new_choice = int(input('Enter selection: '))
    if new_choice == 1:
      self.character_details['Character Name'] = input("Enter the character's name: ")
    elif new_choice == 2:
      new_d100 = int(input('Roll 1d100 and enter the result: '))
      if self.personal_details['Gender'] == 'Male':
        self.character_details['Character Name'] = male_names[new_d100]
      elif self.personal_details['Gender'] == 'Female':
        self.character_details['Character Name'] = female_names[new_d100]
    print('Character name is ' + str(self.character_details['Character Name']) + ' and gender is '+ str(self.personal_details['Gender']))
    
    #Height
    if self.personal_details['Gender'] == 'Female':
      new_d10 = int(input('Roll 1d10 and input the result: '))
      h_inches = female_height_base + new_d10
      h_feet = h_inches // 12
      h_remainder_inches = h_inches - (h_feet * 12)
      print("Character height is equal to " + str(h_feet) + " feet, " + str(h_remainder_inches) + " inches")
      
    elif self.personal_details['Gender'] == 'Male':
      new_d10 = int(input('Roll 1d10 and input the result: '))
      h_inches = male_height_base + new_d10
      h_feet = h_inches // 12
      h_remainder_inches = h_inches - (h_feet * 12)
      print("Character height is equal to " + str(h_feet) + " feet, " + str(h_remainder_inches) + " inches")
    self.personal_details['Height'] = str(h_feet) + " feet, " + str(h_remainder_inches) + " inches"
  
    #Weight
    new_d100 = int(input('Roll 1d100 and input the result: '))
    self.personal_details['Weight'] = weight_table[new_d100]
    print('Your character weighs ' + str(self.personal_details['Weight']) + ' lbs.')
    
    #Hair color
    new_d10 = int(input('Roll 1d10 and input the reuslt: '))
    self.personal_details['Hair Colour'] = hair_colour[new_d10]
    print('Your character has ' + self.personal_details['Hair Colour'] + ' hair.')
  
    #Eye color
    new_d10 = int(input('Roll 1d10 and input the reuslt: '))
    self.personal_details['Eye Colour'] = eye_colour[new_d10]
    print('Your character has ' + self.personal_details['Eye Colour'] + ' eyes.')
    
    #Distinguishing Marks
    new_d100 = int(input('Roll 1d100 and input the result: '))
    self.personal_details['Distinguishing Marks'] = distinguishing_marks[new_d100]
    print("Your character's Distinguishing Feature is a " + self.personal_details['Distinguishing Marks'] + '.')
  
    #Number of Siblings
    new_d10 = int(input('Roll 1d10 and input the reuslt: '))
    self.personal_details['Number of Siblings'] = number_of_siblings[new_d10]
    print('Your character has ' + str(self.personal_details['Number of Siblings']) + ' siblings.')
   
    #Star Sign
    new_d100 = int(input('Roll 1d100 and input the result: '))
    self.personal_details['Star Sign'] = star_sign[new_d100]
    print('Your character was born under the ' + self.personal_details['Star Sign'][0] + ', the ' + self.personal_details['Star Sign'][1])
  
  #age
    new_d100 = int(input('Roll 1d100 and input the result: '))
    self.personal_details['Age'] = age[new_d100]
    print("Your character's age is " + str(self.personal_details['Age']) + '.')
  
  #Starting Career
    
  def generate_non_player_character():
    print('Generating Non Player Character (NPC) - Coming Soon')
    


    