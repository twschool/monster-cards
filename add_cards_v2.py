"""
Second version of the add cards module which allows users to
add custom cards to the monster dictionary
this version is the developed outcome as I
found a better way for the user to enter data
than add_cards_v1"""


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


def card_check(user_values):
    enterbox_fields = ["Monster name"]
    
    # Interating through all the attributes and values
    for attribute, value in raw_dict.items():
        user_values.append(attribute)
        user_values.append(value)
    
    for num in range(0, 4):
        enterbox_fields.append(f"Attribute {num}")
        enterbox_fields.append(f"Attribute {num} value")
    msg_ = ""
    enterbox_title = "Edit card data"

    while True:
        error = False
        error_text = ""
        changed_data = eg.multenterbox(fields=enterbox_fields,
                                        values=user_values, title=enterbox_title)
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
            return True
        else:
            eg.msgbox(msg=f"Error: {error_text}")


def add_cards():
    enterbox_fields = ["Creature Name"]
    enterbox_values = ["Strength", "Speed", "Stealth", "Cunning"]
    for stat in enterbox_values:
        enterbox_fields.append(f"{stat}")
    enterbox_title = "Edit card data"
    new_card_data = eg.multenterbox(fields=enterbox_fields,
                                    msg="Add custom card (Stat values must be between 1-25)")
    print(f"NCD: {new_card_data}")

    check_output = card_check(new)
    print(f"CO: {check_output}")
    # enterbox_msg = "Press ok to submit this card otherwise press cancel to exit or edit the data if anything is wrong"
    # new_card_data = eg.multenterbox(fields=enterbox_fields,
    #                                 msg=enterbox_msg,
    #                                 values=new_card_data)
    print(new_card_data)


add_cards()