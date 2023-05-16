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
    while True:
        error = ""
        for value in user_values[1:]:
            if value == "":
                error = "One of the values was left empty"
            try:
                int_value = int(value)
            except ValueError:
                error = "All stat values need to be a number not a string"
            else:
                if int_value < 0 or int_value > 25:
                    error = "Stat values need to be between 0 and 25"
                  

            



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
    print(new_card_data)


add_cards()