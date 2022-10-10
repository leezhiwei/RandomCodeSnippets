# Lee Zhi Wei - IT01
# Overview
# Basic - Done
# Advanced - Werewolf + Threat
# Bonus - Upgrade, Mine, Skele, Options(Partially, as change field will require overhaul, can only print field)(buggy)
import random

# Game variables
game_vars = {
    'turn': 0,                      # Current Turn
    'monster_kill_target': 20,      # Number of kills needed to win
    'monsters_killed': 0,           # Number of monsters killed so far
    'num_monsters': 0,              # Number of monsters in the field
    'gold': 10,                     # Gold for purchasing units
    'threat': 0,                    # Current threat metre level
    'max_threat': 10,               # Length of threat metre
    'danger_level': 1,              # Rate at which threat increases
    }

defender_list = ['ARCHR', 'WALL','MINE']
monster_list = ['ZOMBI', 'WWOLF','SKELE']

defenders = {'ARCHR': {'name': 'Archer',
                       'maxHP': 5,
                       'min_damage': 1,
                       'max_damage': 4,
                       'price': 5,
                       },
             
             'WALL': {'name': 'Wall',
                      'maxHP': 20,
                      'min_damage': 0,
                      'max_damage': 0,
                      'price': 3,
                      },
             
             'MINE': {'name': 'Mine',
                      'maxHP': 1,
                      'min_damage': 0,
                      'max_damage': 0,
                      'price': 8,
                      }
             }

monsters = {'ZOMBI': {'name': 'Zombie',
                      'maxHP': 15,
                      'min_damage': 3,
                      'max_damage': 6,
                      'moves' : 1,
                      'reward': 2
                      },

            'WWOLF': {'name': 'Werewolf',
                      'maxHP': 10,
                      'min_damage': 1,
                      'max_damage': 4,
                      'moves' : 2,
                      'reward': 3
                      },
            'SKELE': {'name': 'Skeleton',
                      'maxHP': 10,
                      'min_damage': 1,
                      'max_damage': 3,
                      'moves': 1,
                      'reward': 4
                      }
            }

field = [ [['',''],['',''],['',''],['',''],['',''],['',''],['','']],
          [['',''],['',''],['',''],['',''],['',''],['',''],['','']],
          [['',''],['',''],['',''],['',''],['',''],['',''],['','']],
          [['',''],['',''],['',''],['',''],['',''],['',''],['','']],
          [['',''],['',''],['',''],['',''],['',''],['',''],['','']] ]

#----------------------------------------------------------------------
# draw_field()
#
#    Draws the field of play
#    The column numbers only go to 3 since players can only place units
#      in the first 3 columns
#----------------------------------------------------------------------

def draw_field():
    letters = ['A','B','C','D','E'] # init letters
    orde = ord(letters[4]) # find unicode for last char 'E'
    count = 0 # count
    print('  ' + "{:^7}{:^7}{:^7}".format("1","2","3")) # print the numbers
    for line in field: # for loop in line
        print('  ' + ("+-----" * len(line)) + '+') # print header
        if count > 4: # if exceed letters list
            char = chr(orde + (count - 4)) #get char var from the count of board
        else: # else within list
            char = letters[count] # use list
        print(char,end=' ') # print letters using count
        for row in line:# for each row in line
            print(f"|{row[0]:^5}",end='')# print the monster name component, padding 5 align to middle
        print('|') # ending pipe
        count += 1 # increment count
        print('  ', end='') # print 2 spaces
        for row in line:# for each row in line
            print(f"|{row[1]:^5}",end='')# print the health component, padding 5 align to middle
        print('|') # ending pipe
    print('  ' + ("+-----" * len(line)) + '+') # final ending header
    return

#----------------------------
# show_combat_menu()
#
#    Displays the combat menu
#----------------------------
def show_combat_menu(game_vars):
    game_vars['turn'] += 1 # increase turn every printing
    maxthreat= game_vars['max_threat'] # max threat for padding from dictionary
    threatno = game_vars['threat'] #set it as local var
    threat = threatno * '-' # threat meter
    print(f"Turn {game_vars['turn']}     Threat = [{threat:<{maxthreat}}]     Danger Level = {game_vars['danger_level']}") # print top turns, threat and level
    print(f"Gold = {game_vars['gold']}   Monsters killed = {game_vars['monsters_killed']}/{game_vars['monster_kill_target']}") # print gold and monsters killed
    print("1. Buy unit     2. End turn") # print menu pt 1
    print("3. Save game    4. Quit     5. Upgrade unit") # print menu pt 2
    
        

#----------------------------
# show_main_menu()
#
#    Displays the main menu
#----------------------------
def show_main_menu():
    print("1. Start new game") # main menu 1st line
    print("2. Load saved game") # main menu 2nd line
    print("3. Game settings") # main menu 3rd line
    print("4. Quit") # main menu last line

#-----------------------------------------------------
# place_unit()
#
#    Places a unit at the given position
#    This function works for both defender and monster
#    Returns False if the position is invalid
#       - Position is not on the field of play
#       - Position is occupied
#       - Defender is placed past the first 3 columns
#    Returns True if placement is successful
#-----------------------------------------------------

def place_unit(field, position, unit_name):
    rowlist = ['A','B','C','D','E'] # row list
    collist = ['1','2','3'] # column list
    if len(position) != 2:
        return False
    try:
        pos = position.upper() # upper the position letter
        row = pos[0] # row var
        column = pos[1] # column var
    except:
        return False # returns false
    if row in rowlist: # if row var in rowlist
        rowindex = rowlist.index(row) # find index
        if column in collist: # if column in column list
            colindex = collist.index(column) # find index
        else: # else
            return False # return false
    else: # else
        return False # return false
    if len(field[rowindex][colindex][0]) == 0: # if length of name in field is 0
        field[rowindex][colindex][0] = unit_name # put unit in field
        field[rowindex][colindex][1] = f'{defenders[unit_name]["maxHP"]}/{defenders[unit_name]["maxHP"]}' #put in field
    else:
        return False # if something at field
    return True # return true when success

#-------------------------------------------------------------------
# buy_unit()
#
#    Allows player to buy a unit and place it using place_unit()
#-------------------------------------------------------------------
def buy_unit(field, game_vars):
    print("What do you wish to buy?") # Header
    for x in defender_list: # loop in defender list
        print(f"{defender_list.index(x) + 1}. {defenders[x]['name']} {defenders[x]['price']} gold") # print the defenders gold etc
    print(f"{len(defender_list) + 1}. Don't buy") # print dont buy
    while True: # loop
        try: # exception handling
            choice = int(input("Your choice? ")) # input
        except ValueError: # if unrecognized input
            print("Please select from the choice above.") # print error
            continue # continue the loop
        if choice != (len(defender_list) + 1): # if choice not 3
            index = choice - 1 #index minus 1
            defender_key = defender_list[index] # get defender key
            if game_vars['gold'] < defenders[defender_key]['price']: # gold checking
                print("You do not have enough gold") # print error
            else: # else gold enough
                game_vars['gold'] -= defenders[defender_key]['price'] # minus gold
                while True: # while loop
                    pos = str(input("Where do you want to place your defender? ")) # input prompt
                    if place_unit(field, pos, defender_key): # if true
                        break # break once
                    else: # false
                        print("Unit positioning is not successful.")# error
                break # break twice
        elif choice == (len(defender_list) + 1): # if choice 3 
            break # break
        else: # else selection invalid
            print("Please select from the choice above.") # error
    return

#-----------------------------------------------------------
# defender_attack()
#
#    Defender unit attacks.
#
#-----------------------------------------------------------
def defender_attack(defender_name, field, row, column):
    if defender_name == defender_list[0]: # if archer
        for rowlist in field[row]: # goes through every row a defender is in
                if rowlist[0] in monsters: # if one of the grid has a monster
                    monkey = rowlist[0] # monsterkey
                    healthlist = rowlist[1].split('/') # split HP at the /
                    damage = random.randint(defenders[defender_name]['min_damage'],defenders[defender_name]['max_damage']) # random damage calc
                    if monkey == 'SKELE': # if monster is skeleton
                        damage = round(damage / 2) # damaged is halfed and rounded
                    HP = int(healthlist[0]) - damage # minus the damage
                    listofrows = ['A','B','C','D','E'] # row list
                    print(f'{defenders[defender_name]["name"]} in lane {listofrows[row]} shoots {monsters[monkey]["name"]} for {damage} damage!') # print status msg
                    if HP <= 0: # dead monster
                        print(f'{monsters[monkey]["name"]} dies!') # print monster died
                        reward = monsters[monkey]['reward'] # rewards variable
                        print(f'You gain {reward} gold as a reward.') # tell user what reward
                        game_vars['gold'] += reward # add gold to reward
                        game_vars['monsters_killed'] += 1 # add one to monsters killed
                        rowlist[0] = '' # remove from board (name)
                        rowlist[1] = '' # remove from board (HP)
                        game_vars['threat'] += reward # adds to threat meter when monster is killed
                        return 
                    rowlist[1] = f'{HP}/{healthlist[1]}' # append back to grid
    elif defender_name == defender_list[2]: # if mine
        if len(field[row][column + 1][0]) != 0: # if before square has something there
            for row in field: # for row in field
                for column in row: # for column in field
                    if defender_list[2] in column[0]: # if mine
                        rownum = field.index(row) #gets current row index
                        columnnum = row.index(column) # get column index
            list = [-1,0,1] # list with -1 0 and +1
            try: 
                for index1 in range(3): # for index in range of 3
                    row = rownum + list[index1] # row number plus list index eg 3 + -1 = 2
                    for index2 in range(3): # for index in range 3
                        column = columnnum + list[index2] # column number plus index eg 1 + 2 = 3
                        if field[row][column][0] in monsters: # if its a monster
                            monkey = field[row][column][0] # monsterkey
                            healthlist = field[row][column][1].split('/') # split HP at the /
                            damage = 9 # set damage to 9
                            HP = int(healthlist[0]) - damage # minus the damage
                            listofrows = ['A','B','C','D','E'] # row list
                            print(f'{defenders[defender_name]["name"]} in lane {listofrows[row]} explodes and damages {monsters[monkey]["name"]} for {damage} damage!') # print status msg
                            if HP <= 0: # dead monster
                                print(f'{monsters[monkey]["name"]} dies!') # print monster died
                                reward = monsters[monkey]['reward'] # rewards variable
                                print(f'You gain {reward} gold as a reward.') # tell user what reward
                                game_vars['gold'] += reward # add gold to reward
                                game_vars['monsters_killed'] += 1 # add one to monsters killed
                                field[row][column][0] = '' # remove from board (name)
                                field[row][column][1] = '' # remove from board (HP)
                                field[rownum][columnnum][0] = '' #remove mine from board (name)
                                field[rownum][columnnum][1] = '' #remove mine from board (HP)
                                game_vars['threat'] += reward # adds to threat meter when monster is killed
                                return
                            field[row][column][1] = f'{HP}/{healthlist[1]}' # append back to grid
            except IndexError: # if index out of range
                return # returns
    return 
#-----------------------------------------------------------
# monster_advance()
#
#    Monster unit advances.
#       - If it lands on a defender, it deals damage
#       - If it lands on a monste5r, it does nothing
#       - If it goes out of the field, player loses
#-----------------------------------------------------------
def monster_advance(monster_name, field, row, column, defenders, monsters):
    rowlist = ['A','B','C','D','E'] # row list
    if monster_name == 'ZOMBI' or monster_name == 'SKELE': # zombie move one space and skeleton move one space
        if len(field[row][column - 1][0]) != 0: # one space before obstacle
            if field[row][column - 1][0] in defenders: # if defender
                healthlist = field[row][column - 1][1].split('/') # split defender health by slash
                damage = random.randint(monsters[monster_name]['min_damage'], monsters[monster_name]['max_damage']) # random attack pts
                HP = int(healthlist[0]) - damage # minus the damage
                print(f'{monsters[monster_name]["name"]} in lane {rowlist[row]} hits {defenders[field[row][column - 1][0]]["name"]} for {damage} damage!') # print damage message
                if HP <= 0: # if HP is zero or less
                    field[row][column - 1][0] = '' # remove name from field
                    field[row][column - 1][1] = '' # remove HP from field
                    return # return
                field[row][column - 1][1] = f'{HP}/{healthlist[1]}' # else will reappend HP
                return # return
            else: # A monster is in front
                print(f'{monsters[monster_name]["name"]} in lane {rowlist[row]} is blocked from advancing.') # print monster cannot advance
                return 
    elif monster_name == 'WWOLF': #Warewolf 2 space
        if len(field[row][column - 1][0]) != 0: # if any block before has obstacle
            if field[row][column - 1][0] in defenders: # if defender
                healthlist = field[row][column - 1][1].split('/') # split defender health by slash
                damage = random.randint(monsters[monster_name]['min_damage'], monsters[monster_name]['max_damage']) # random attack pts
                HP = int(healthlist[0]) - damage # minus the damage
                print(f'{monsters[monster_name]["name"]} in lane {rowlist[row]} hits {defenders[field[row][column - 1][0]]["name"]} for {damage} damage!') # print damage message
                if HP <= 0: # if HP is zero or less
                    field[row][column - 1][0] = '' # remove name from field
                    field[row][column - 1][1] = '' # remove HP from field
                    return # return
                field[row][column - 1][1] = f'{HP}/{healthlist[1]}' # else will reappend HP
                return # return
            else: # monster
                print(f'{monsters[monster_name]["name"]} in lane {rowlist[row]} is blocked from advancing.') # print monster cannot advance
                return # do nothing
        elif len(field[row][column - 2][0]) != 0: # if obstacle 2 spaces before
            field[row][column - 1][0] = monster_name # puts field on minus one of current space (name)
            field[row][column - 1][1] = field[row][column][1] # puts field on minus one of current space (HP)
            field[row][column][0] = '' # replaces previous space with blank (Name)
            field[row][column][1] = '' # replaces previous space with blank (HP)
            return # return   
    moves = column - monsters[monster_name]['moves'] # index of the next location
    if moves < 0: # if moves negative
        moves = 0 # set to first column
    field[row][moves][0] = monster_name # puts field on minus moves of current space (name)
    field[row][moves][1] = field[row][column][1] # puts field on minus moves of current space (HP)
    field[row][column][0] = '' # replaces previous space with blank (Name)
    field[row][column][1] = '' # replaces previous space with blank (HP)
    print(f'{monsters[monster_name]["name"]} in lane {rowlist[row]} advances!') # print monster advances
    return 

#---------------------------------------------------------------------
# spawn_monster()
#
#    Spawns a monster in a random lane on the right side of the field.
#    Assumes you will never place more than 5 monsters in one turn.
#---------------------------------------------------------------------
def spawn_monster(field, monster_list):
    monsternum = random.randint(0,2) # random index
    row = random.randint(0,4) # random row
    column = -1 # column is always last to spawn
    monsterchosen = monster_list[monsternum] # name from list, eg ZOMBI
    HPTotal = monsters[monsterchosen]['maxHP'] # get hp from dictionary
    HP = HPTotal # make HP HPTotal
    field[row][column][0] = monsterchosen # add it to field
    field[row][column][1] = f'{HP}/{HPTotal}' # add HP to field
    return 

#-----------------------------------------
# save_game()
#
#    Saves the game in the file 'save.txt'
#-----------------------------------------
def save_game(field,game_vars,monsters,defenders):
    data = f'{field}\n{game_vars}\n{monsters}\n{defenders}' # init data variable
    savegame = open('save.txt', 'w') # open it in write mode
    savegame.write(data) # write data
    savegame.close() # close file
    print("Game saved.")

#-----------------------------------------
# load_game()
#
#    Loads the game from 'save.txt'
#-----------------------------------------
def load_game(field,game_vars,monsters,defenders):
    savefile = open('save.txt', 'r') # load save file
    data = savefile.read() # read save file into data
    savefile.close() # close file
    datalist = data.split('\n') # split by newline
    exec(f'global field\nfield = {datalist[0]}') # make field global in the exec scope then reassign field variable
    exec(f'global game_vars\ngame_vars = {datalist[1]}') # make game_vars global in the exec scope then reassign field variable
    exec(f'global monsters\nmonsters = {datalist[2]}') # make monsters variable global in exec scope and reassign from monsters dictionary
    exec(f'global defenders\ndefenders = {datalist[3]}') # make defenders variable global in exec scope and reassign from defenders dictionary
    return

#-----------------------------------------------------
# initialize_game()
#
#    Initializes all the game variables for a new game
#-----------------------------------------------------
def initialize_game():
    game_vars['turn'] = 0 
    game_vars['monster_kill_target'] = 20
    game_vars['monsters_killed'] = 0
    game_vars['num_monsters'] = 0               # init dict
    game_vars['gold'] = 10
    game_vars['threat'] = 0
    game_vars['danger_level'] = 1

#Field check checks for monsters, if present return False, else returns True

def field_check(field, monsters):
    for row in field: # each row in field
        for column in row: # each column in row
            if column[0] in monsters: # if name is monster
                return False # return False
    return True # else returns True

# Actions upon ending turn, advance monster, defender attack, and add gold

def end_turn(field, game_vars, monster_list, defenders):
    for row in field: # each row in field
        for column in row: # each column in row
            if len(column[0]) != 0: # if column is not blank
                if column[0] in monsters: # if monster
                    monster_advance(column[0], field, field.index(row),row.index(column), defenders, monsters) # advance
                elif column[0] in defenders: # if defender
                    defender_attack(column[0], field, field.index(row),row.index(column)) # attack
    game_vars['gold'] += 1 # plus one gold
    game_vars['threat'] += random.randint(1,game_vars['danger_level']) #threat level increases by random 1 and danger level
    if game_vars['turn'] % 12 == 0: # every 12 turns
        game_vars['danger_level'] += 1 # danger level adds one
        for key in monsters: # for key in defender dictionary
            monsters[key]['min_damage'] += 1 # add min damage
            monsters[key]['max_damage'] += 1 # add max damage
            monsters[key]['reward'] += 1 # add reward
            monsters[key]['maxHP'] += 1 # add max HP
        print('The evil grows stronger!') # Here the message
    threatchecker(game_vars, field, monster_list) # checks threat at end of each turn
    return 

# Kill count checker, return true when killcount is reached, return false when not

def kill_count(game_vars):
    if game_vars['monsters_killed'] >= game_vars['monster_kill_target']: #if killcount more than target
        return True # return true
    return False # else false

# monster checker at first row, if present, will return tuple with True or False, index 0 and monster name, index 1

def moncheck(field, monsters): # monsterchecker
    for row in field: # for every row in field
        if row[0][0] in monsters: # if row index 0 (first column) and index 0 (monster key) in monsters
            monname = monsters[row[0][0]]['name'] # acquire name
            return True, monname # returns bool True and monster name
    return False, '' # else will return bool False and blank str

# savefile checker, if present return True, else return False

def filecheck():
    try:
        file = open('save.txt', 'r') # try and open file in read mode
        file.close() # if found close
    except FileNotFoundError: # if not found
        return False # return false
    return True # else return True

# threat checker, will spawn monster if more than or equals to max threat var, deduct max threat once monster is spawn

def threatchecker(game_vars, field, monster_list):
    if game_vars['threat'] >= game_vars['max_threat']: # if threat meter is more than max threat
        spawn_monster(field, monster_list) # spawn monster
        game_vars['threat'] -= game_vars['max_threat'] # minus threat meter by max threat

# upgrade unit, upgrade at dictionary

def upgrade_unit(game_vars, defenders, count):
    basegold = 8 # base amount of gold
    addgold = basegold + (2 * count) # additonal gold and the basegold added
    print(f'{defenders["ARCHR"]["name"]} Minimum Damage: {defenders["ARCHR"]["min_damage"]} Maximum Damage: {defenders["ARCHR"]["max_damage"]} Maximum HealthPoints: {defenders["ARCHR"]["maxHP"]}')
    # print current stats
    while True: # loop for input prompt
        selection = input(f"Are you sure you want to upgrade your archer? Requires {addgold} gold. (Y/N)") # input prompt
        uppsel = selection.upper() # upper case the selection
        if uppsel == 'Y': # if yes
            if game_vars['gold'] < addgold: # not enough gold
                done = False # if upgrade not done
                print("You do not have enough gold") # print not enough gold
                break # break out of loop
            else: # else if enough gold
                done = True # if upgrade done
                game_vars['gold'] -= addgold # minus the gold
                defenders['ARCHR']['min_damage'] += 1 # add in the min damage
                defenders['ARCHR']['max_damage'] += 1 # add in max damage
                defenders['ARCHR']['maxHP'] += 1 # add in maxhp
                break # break out
        elif uppsel == 'N': # if no
            done = False # if upgrade not done
            break # break out
        else: # else invalid input
            print('Please type Y or N') # prompt user to key in proper input
            continue # continue loop
    return done # returns fn   
    
#-----------------------------------------
#               MAIN GAME
#-----------------------------------------
exitflag = False # to break from multiple loop
continueflag = False # flag to know if a continue is required
sel = 0  # set selection to zero
count = 0 # count of upgrade
print("Desperate Defenders")
print("-------------------")  # main name
print("Defend the city from undead monsters!")
print()
while True: # while loop
    if exitflag == True:
        break # break out of main loop
    if continueflag == False: # when no save_game loaded
        show_main_menu() # menu
        try: #exception checking
            sel = int(input("Your choice? ")) # user selection
        except ValueError: # when user type in letters, 
            print("Invalid input, enter from selection above.") # show error
            continue # continue loop
        initialize_game() # init game when no save file
    if sel == 1: # start game
        sel = 0 # re-init variable
        while True: # loop after selection
            if exitflag == True: # break out of main game loop
                break
            if field_check(field, monsters):
                spawn_monster(field,monster_list) #spawn in field
            draw_field() # draw field
            show_combat_menu(game_vars) # show menu
            while True: # while loop for input prompt, will loop input prompt only
                try:
                    sel = int(input("Your choice? ")) # try with input prompt
                except ValueError:  # if alpha or other chars
                    print("Invalid Choice, choose a number instead.") # print error
                    continue
                if sel == 1: # buy unit
                    buy_unit(field, game_vars) # buys unit
                    end_turn(field, game_vars, monster_list, defenders) # end turn
                    break # break out of loop
                elif sel == 2: # end turn
                    end_turn(field, game_vars, monster_list, defenders) # ends turn
                    break # break out of loop
                elif sel == 3: # save game
                    if filecheck(): # file exists
                        sel = input("Are you sure do you want to override your save file? (Y/N) ") # selection for yes or no
                        selcap = sel.capitalize() # will captialise
                        if selcap == 'Y': # if yes
                            save_game(field,game_vars,monsters,defenders) #use save file fn
                            exitflag = True #sets exit flag
                            break #breaks out of this loop
                        elif selcap == 'N': #if does not override, reset loop
                            continue # continues
                    else: # if file dont exist
                        save_game(field,game_vars,monsters,defenders) # save the game
                        exitflag = True # set flag to true
                        break # break out of loop
                elif sel == 4: # quit
                    exitflag = True # set flag to true
                    break # break out of one
                elif sel == 5:
                    if upgrade_unit(game_vars, defenders, count): # if upgrade function returns True
                        count += 1 # add count
                        end_turn(field, game_vars, monster_list, defenders) # end turn
                        break # break out of loop to continue
                else: # if other numbers
                    print("Invalid option, Please select from options above.") # error
            if kill_count(game_vars): # checking if monster count is more than target
                print("You have protected the city! You win!") # print winning message
                exitflag = True # set exit flag
            elif moncheck(field, monsters)[0]: # if monsterchecker returns True
                print(f'A {moncheck(field, monsters)[1]} has reached the city! All is lost!') # print lose message pt 1
                print('You have lost the game. :(') # print lose msg pt 2
                exitflag = True # set exit flag
    elif sel == 2: # load save
        if filecheck() == False: # if file not present
            print("Savefile not present, save your file before loading.") # print error
            continue # continue selection loop
        else: # if file present
            load_game(field,game_vars,monsters,defenders) # load game
            continueflag = True # set continueflag var to true
            sel = 1 # set selection to 1 to re-init game with new variables
            continue # continue loop
    elif sel == 3: # settings
        sel = 0 # reset sel
        while True:
            print("Type the option number below to change the following options.")
            print("1. Board Size, eg number of lanes and length")
            print("2. Kill Target")
            print("3. Threat meter length") # options
            print("4. Enter a new game")
            print("5. Return to main menu")
            try: 
                sel = int(input("What is your choice? ")) # try prompt
            except ValueError: # invalid symbols or alpha
                print("You have inputted an invalid option, please choose from the options above.") # print error
                continue # continue loop
            if sel == 1: # change the board size
                loop = True # loop flag, will loop if true
                baserow = len(field)
                basecolumn = len(field[0])
                while loop: # while loop, using loop var
                    print(f"The current board size is {len(field)} by {len(field[0])}") # show current stats
                    sel = input("Do you wish to change it?(Y/N) ") # ask if user is sure
                    if sel.upper() == 'Y': # if yes
                        while True: # another loop
                            try: # try the prompt
                                row = int(input("What do you want to change the row to? ")) # input prompt
                            except ValueError: # if invalid chars like symbols or letter
                                print("You have entered an invalid option") # print error
                                continue # continue inner loop
                            try: # try the prompt
                                column = int(input("What do you want to change the column to? ")) # input prompt
                            except ValueError: # if invalid chars like symbols or letter
                                print("You have entered an invalid option") # print error
                                continue # continue inner loop
                            if row > baserow: # if inputted row is more than baserow
                                newrow = row - baserow # find difference
                                for x in range(newrow): # for loop in range of diff
                                    field.append(field[0]) # add needed rows
                            elif row < baserow: # if row inputted less
                                remrow = baserow - row # difference
                                for x in range(remrow):# for loop in range of difference
                                    field.remove(field[0]) # remove field
                            elif row == baserow: # if row and the baserow is equal
                                print(f'Row is already set to {row}') # already set msg
                            if column > basecolumn: # if input column is more than base column
                                newcol = column - basecolumn # difference
                                for row in field: # for loop in row
                                    for x in range(newcol): # for loop in range of difference
                                        row.append(row[0]) # append more rowa
                            elif column < basecolumn: # if input is less than base
                                remcol = basecolumn - column # removal diff
                                for row in field: # for row in field
                                    for x in range(remcol): # for x in range of removal difference
                                        row.remove(row[0]) # remove column
                            elif column == basecolumn: # if column and base is same
                                print(f'Column is already set to {column}') # print already set
                            loop = False # set loop to false
                            break # break out of inner loop
                    elif sel.upper() == 'N': # if no
                        break # break out of outer loop
                    else: # invalid option for y/n
                        print("Invalid option") # print error
                        continue # continue outer loop
            elif sel == 2: # change kill target
                loop = True # loop flag, will loop if true
                while loop: # while loop, using loop var
                    print(f"The current kill target is {game_vars['monster_kill_target']}") # show current stats
                    sel = input("Do you wish to change it?(Y/N) ") # ask if user is sure
                    if sel.upper() == 'Y': # if yes
                        while True: # another loop
                            try: # try the prompt
                                option = int(input("What do you want to change it to? ")) # input prompt
                            except ValueError: # if invalid chars like symbols or letter
                                print("You have entered an invalid option") # print error
                                continue # continue inner loop
                            game_vars['monster_kill_target'] = option # else change var
                            loop = False # set loop to false
                            break # break out of inner loop
                    elif sel.upper() == 'N': # if no
                        break # break out of outer loop
                    else: # invalid option for y/n
                        print("Invalid option") # print error
                        continue # continue outer loop
            elif sel == 3: # change threat meter length
                loop = True # loop flag, will loop if true
                while loop: # while loop, using loop var
                    print(f"The current max threat is {game_vars['max_threat']}") # show current stats
                    sel = input("Do you wish to change it?(Y/N) ") # ask if user is sure
                    if sel.upper() == 'Y': # if yes
                        while True: # another loop
                            try: # try the prompt
                                option = int(input("What do you want to change it to? ")) # input prompt
                            except ValueError: # if invalid chars like symbols or letter
                                print("You have entered an invalid option") # print error
                                continue # continue inner loop
                            game_vars['max_threat'] = option # else change var
                            loop = False # set loop to false
                            break # break out of inner loop
                    elif sel.upper() == 'N': # if no
                        break # break out of outer loop
                    else: # invalid option for y/n
                        print("Invalid option") # print error
                        continue # continue outer loop
            elif sel == 4: # enter a new game
                sel = 1 # sets sel to 1 for init game
                continueflag = True # sets continueflag to true
                break # break out of input loop
            elif sel == 5:
                sel = 0 # set selection to 0 to main menu
                break # break out of input loop
            else: # invalid numbers
                print("You have inputted an invalid option, please choose from the options above.") # error
    elif sel == 4: # quit
        break # break
    else: # zeros, nines eights, ridiculous inputs captured here
        print("Invalid option, select from the numbers above.") # print error
print("See you next time!") # ending text

# TO DO: ADD YOUR CODE FOR THE MAIN GAME HERE!
    
    
