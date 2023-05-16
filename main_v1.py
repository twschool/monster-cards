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


def change_card(card_name, msg_=""):
    # Global varaible prevent errors 
    global creature_dict
    if msg_ == "":
        # If user doesnt pass in a custom message use the default
        msg_ == f"Change card for {card_name}"
    raw_dict_data = creature_dict[card_name]
    enterbox_values = [card_name]
    enterbox_fields = ["Monster name"]
    
    # Interating through all the attributes and values
    for attribute, value in raw_dict_data.items():
        enterbox_values.append(attribute)
        enterbox_values.append(value)
    
    for num in range(0, 4):
        enterbox_fields.append(f"Attribute {num}")
        enterbox_fields.append(f"Attribute {num} value")
    msg_ = ""
    enterbox_title = "Edit card data"
    while True:
        error = False
        error_text = ""
        changed_data = eg.multenterbox(fields=enterbox_fields,
                                        values=enterbox_values, title=enterbox_title)
        count = 0

        for item in changed_data:
            if item == "":
                error = True
                error_text = "One of the fields was empty"
            
        # Complex system for catching int errors

        # Ever
            if count % 2 == 0:
                if count != 0:
                    print(f"Got through: {item}")
                    try:
                        item_num = int(item)
                    except ValueError:
                        error = True
                        error_text = "A number was expected instead got a string (word)"
                    else:
                        if item_num > 25 or item_num < 1:
                            error = True
                            error_text = "Invalid number numbers can only be between 1-25"
            count += 1
                    
        if error is False:
            break
        else:
            eg.msgbox(msg=f"Error: {error_text}")

    # Shortened name for tidyness
    cd = changed_data
    creature_dict[cd[0]] = {cd[1] : cd[2], cd[3]: cd[4], cd[5]: cd[6]}


def return_all_monsters():
    monsters_ = []
    for creature in creature_dict:
        monsters_.append(creature)
    return monsters_


def add_cards():
    enterbox_fields = ["Creature Name"]
    enterbox_values = ["Strength", "Speed", "Stealth", "Cunning"]
    for stat in enterbox_values:
        enterbox_fields.append(f"{stat}")
    enterbox_title = "edit card data"
    new_card_data = eg.multenterbox(fields=enterbox_fields,
                                    msg="Add custom card (Stat values must be between 1-25)")
    if new_card_data is None:
        return [False, "User exited out of edit statement"]
    while True:
        enterbox_msg = "New card data entry"
        data_backup = new_card_data
        new_card_data = eg.multenterbox(fields=enterbox_fields,
                                        msg=enterbox_msg,
                                        values=new_card_data)
        if new_card_data is None:
            does_exit = eg.buttonbox(msg="Do you want to exit without saving changes",
                                    choices = ["Yes", "No"])
            if does_exit == "Yes":
                return [None, "User exited without saving"]
            else:
                # If user mistakenly cancels then they can go back
                new_card_data = data_backup
                continue
        else:
            # If user didnt raise a error then exit out of this function
            for value in new_card_data[1:]:
                if value == "" or new_card_data[0] == "":
                    eg.msgbox("No values can be left empty")
                    continue
                try:
                    converted = int(value)
                except ValueError:
                    eg.msgbox("All values have to be a integer (apart from card name)")
                    continue
            break
                                 
    print(new_card_data)


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
    action = eg.buttonbox(choices=options, msg="What would you like to do?")
    if action == "Exit":
        exit("User exited the program")

    elif action == "Delete card":
        deletedata()
    elif action == "Add card":
        add_cards()
    elif action == "Search card":
        action_search = eg.buttonbox(msg="Do you want to view and edit a card or just view a card?",
                                     choices=["View a card", "View and edit a card"])
        change_card()
   



# change card
msg_ = "What card do you want to search"
to_search = eg.buttonbox(choices=monsters, msg=msg_, title="Monster search")
change_card(card_name=to_search)

