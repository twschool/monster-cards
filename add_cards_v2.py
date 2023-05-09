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

def nonecheck(user_input):
    if user_input is None:
        return True
    else:
        return False


def add_cards():
    enterbox_fields = ["Creature Name"]
    enterbox_values = ["Strength", "Speed", "Stealth", "Cunning"]
    for stat in enterbox_values:
        enterbox_fields.append(f"{stat}")
    enterbox_title = "edit card data"
    new_card_data = eg.multenterbox(fields=enterbox_fields,
                                    msg="Add custom card (Stat values must be between 1-25)")
    if nonecheck(new_card_data):
        return [False, "User exited out of edit statement"]
    while True:
        enterbox_msg = "New card data entry"
        data_backup = new_card_data
        new_card_data = eg.multenterbox(fields=enterbox_fields,
                                        msg=enterbox_msg,
                                        values=new_card_data)
        if nonecheck(new_card_data):
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


add_cards()