
"""
First version of the main component all components being combined into one main program
"""


import easygui as eg
# Dictionary
creature_dict = {
    "Stoneling": {
        "Strength": 7,
        "Speed": 1,
        "Stealth": 25,
        "Cunning": 15
    },
    "Vexscream": {
        "Strength": 1,
        "Speed": 6,
        "Stealth": 21,
        "Cunning": 19
    },
    "Dawnmirage": {
        "Strength": 5,
        "Speed": 15,
        "Stealth": 18,
        "Cunning": 22
    },
    "Blazegolem": {
        "Strength": 15,
        "Speed": 20,
        "Stealth": 23,
        "Cunning": 6
    },
    "Websnake": {
        "Strength": 7,
        "Speed": 15,
        "Stealth": 10,
        "Cunning": 5
    },
    "Moldvine": {
        "Strength": 21,
        "Speed": 18,
        "Stealth": 14,
        "Cunning": 5
    },
    "Vortexwing": {
        "Strength": 19,
        "Speed": 13,
        "Stealth": 19,
        "Cunning": 2
    },
    "Rotthing": {
        "Strength": 16,
        "Speed": 7,
        "Stealth": 4,
        "Cunning": 12
    },
    "Froststep": {
        "Strength": 14,
        "Speed": 14,
        "Stealth": 17,
        "Cunning": 4
    },
    "Wispghoul": {
        "Strength": 17,
        "Speed": 19,
        "Stealth": 3,
        "Cunning": 2
    }
}


def cancel_func(message="Do you want to go back to the main menu?"):
    result = eg.buttonbox(msg=message,
                        choices=["Yes", "No"], title="Exit")
    if result == "Yes":
        return True
    else:
        return False


def change_card(card_data, msg_="", enterbox_title="", is_in_dict=True):
    # Global varaible prevent errors 
    global creature_dict

    card_name = card_data[0]
    enterbox_values = []    
    enterbox_fields = ["Monster name" ,"Strength", "Speed", "Stealth", "Cunning"]

    if msg_ == "":
        # If user doesnt pass in a custom message use the default
        msg_ == f"Change card for {card_name}"
    
    if enterbox_title == "":
        # If user doesnt pass in a custom title use the default
        enterbox_title = "Edit card data"

    
    
    if is_in_dict is True:
        enterbox_values.append(card_name)
        raw_dict_data = creature_dict[card_name]
        for attribute, value in raw_dict_data.items():
            enterbox_values.append(value)
    else:
        enterbox_values = card_data
    
    
    # If a dictionary was given then turn the dictionary into a list
   
    changed_data = enterbox_values
    while True:
        error = False
        count = 0

        error_text = ""
        changed_data = eg.multenterbox(msg="Confirm your card values" ,fields=enterbox_fields,
                                        values=enterbox_values, title=enterbox_title)
        if changed_data is None:
            if cancel_func() is False:
                continue
            else:
                return
        else:
            enterbox_values = changed_data
        if changed_data[0] == "":
            error_text = "Monster name was empty"
            error = True

        for item in changed_data[1:]:
            if item == "":
                error_text = "Stat value(s) was empty"
                count += 1
                error = True
                        
            # Complex system for catching int errors

            try:
                item_num = int(item)
            except ValueError:
                error = True
                error_text = "A number was expected instead got a string (word)"
            else:
                if item_num > 25 or item_num < 1:
                    error = True
                    error_text = "Invalid number numbers can only be between 1-25"

                
        if error is False:
            break
        else:
            eg.msgbox(msg=f"Error: {error_text}")

    # Shortened name for tidyness
    cd = changed_data
    creature_dict[cd[0]] = {"Strength" : cd[1], "Speed": cd[2], "Stealth": cd[3], "Cunning": cd[4]}


def return_all_monsters():
    monsters_ = []
    for creature in creature_dict:
        monsters_.append(creature)
    return monsters_


def displaydata():
    heading_string = "Creature name\tStrength\tSpeed\tStealth\tCunning"
    print(heading_string)
    print()
    for creature, attributes in creature_dict.items():
        power_list = []
        for power, value in attributes.items():
            power_list.append(value)
        pl = power_list
        print(f"{creature}\t\t{pl[0]}\t\t\t{pl[1]}\t\t{pl[2]}\t\t{pl[3]}")


def add_cards():
    enterbox_fields = ["Creature Name"]
    enterbox_values = ["Strength", "Speed", "Stealth", "Cunning"]
    for stat in enterbox_values:
        enterbox_fields.append(f"{stat}")
    enterbox_title = "edit card data"
    new_card_data = eg.multenterbox(fields=enterbox_fields,
                                    msg="Add custom card (Stat values must be between 1-25)",
                                    title=enterbox_title)
    if new_card_data is None:
        return [False, "User exited out of edit statement"]
    else:
        change_card(card_data=new_card_data, is_in_dict=False)


def deletedata():
    while True:
        # Loops forever (just for testing)
        monsters = return_all_monsters()
        msg_ = "What card do you want to delete"
        try:
            to_delete = eg.buttonbox(choices=monsters, msg=msg_, title="Delete card")
            del creature_dict[to_delete]
            return
        except IndexError:
            """If user deletes all cards then runs this function again
            then the msgbox will print the error without crashing"""
            eg.msgbox(msg="No cards found in database")


def displaydata():
    heading_string = "Creature name\tStrength\tSpeed\tStealth\tCunning"
    print(heading_string)
    print()
    for creature, attributes in creature_dict.items():
        power_list = []
        for power, value in attributes.items():
            power_list.append(value)
        pl = power_list
        print(f"{creature}\t\t{pl[0]}\t\t\t{pl[1]}\t\t{pl[2]}\t\t{pl[3]}")


options = ["Delete card", "Add card", "Search card", "Output menu", "Exit"]
while True:
    action = eg.buttonbox(choices=options,
                        msg="What would you like to do?",
                        title="Main Menu")
    if action == "Exit":
        exit("User exited the program")

    elif action == "Delete card":
        deletedata()
    elif action == "Add card":
        add_cards()
    elif action == "Search card":
        
        action_search = eg.buttonbox(msg="Do you want to view and edit a card or just view a card?",
                                    choices=["View a card", "View and edit a card"])
        ca = return_all_monsters()
        
        msg_ = "What card do you want to search"
        to_search = eg.buttonbox(choices=ca,
                                msg=msg_,
                                title="Monster search")
        
        
        if "edit" in action_search:
            change_card([to_search], is_in_dict=True)
        else:
            card_data = creature_dict[to_search]
            print(card_data)
            message = f"{to_search}\n"\
                f"Strength: {card_data['Strength']}\n"\
                f"Speed: {card_data['Speed']}\n"\
                f"Stealth: {card_data['Stealth']}\n"\
                f"Cunning: {card_data['Cunning']}"
            eg.msgbox(msg=message,
                    title="Searched card data")
    elif action == "Output menu":
        displaydata()