import keyword
import os, json, time, random as rand, sys
from typing import Any


# THIS FUNCTION PRINTS A WELCOME MESAGE AND CALLS THE <display_main_menu> FUNCTION
def display_welcome_message() -> None:
    clr_terminal()
    print(BORDER)
    print("\n        WELCOME TO NOTEPLAY\n")
    print(BORDER)
    display_main_menu()


# THIS FUNCTION PRINTS THE MAIN MENU
def display_main_menu() -> None:
    print(f"{BORDER}\n")
    for num, item in enumerate(iterable=MAIN_MENU_ITEMS, start=1):
        print(f"    [{num}] {item}")
    print(f"\n{BORDER}")


# THIS FUNCTION PRINTS THE ITEMS OF PROGRAM'S MAIN MENU
def display_main_menu_items(array: list | tuple, title: str) -> None:
    clr_terminal()
    print(f"{BORDER}\n        {title}\n{BORDER}\n")
    for num, item in enumerate(iterable=array, start=1):
        print(f"    [{num}] {item}")
    print(f"\n{BORDER}")


# THIS FUNCTION QUITS THE SELECTED PROGRAM TO MAIN MENU
def quit_to_main_menu(title: str) -> int:
    while True:
        clr_terminal()
        print(f"{BORDER}\n\n    [1] QUIT {title}\n    [2] QUIT PROGRAM\n\n{BORDER}")
        try:
            user_confirmation: int = int(input("INPUT: "))
        except ValueError:
            continue
        if user_confirmation == 1:
            return user_confirmation
        elif user_confirmation == 2:
            sys.exit()
        else:
            continue




# --------------------------------------------------
# SCHEDULE ORGANIZER
class ScheduleOrganizer:
    # THIS FUNCTION GETS THE INPUT OF THE USER, SUBJECT CODE, START TIME, END TIME, DAY OF A SCHEDULE 
    def add_schedule(self) -> None:
        while True:
            subject_code: str = Schedule_Organizer.display_subject_items()
            subject_start_time: int = Schedule_Organizer.display_time_items("START")
            subject_end_time: int = Schedule_Organizer.display_time_items("END")
            subject_day: str = Schedule_Organizer.display_day_items()
            schedules[subject_day] = {"SUBJECT CODE": subject_code, "SUBJECT START TIME": subject_start_time, "SUBJECT END TIME": subject_end_time, "SUBJECT DAY": subject_day}
            try: #CREATES A FILE IF THE FILE DOESN'T EXIST
                with open(file=SCHEDULES_FILE_NAME, mode="x") as schedules_json:
                    schedules_json.write(json.dumps(schedules, indent=4))
            except FileExistsError: 
                #ACCESS THE DATA OF THE JSON FILE CONVERTS THE DATA INTO PYTHON DICTIONARY AND ASSIGN THE SCHEDULE TO THEIR RESPECTIVE DAY OF THE WEEK AND CONVERT THE PYTHON DICTIONARY INTO A JSON AND WRITES THE JSON FILE WITH NEW DATA
                with open(file=SCHEDULES_FILE_NAME, mode="r") as schedules_json:
                    schedules_json_data = json.load(schedules_json)
                schedules_json_data[subject_day][subject_code] = {"SUBJECT CODE": subject_code, "SUBJECT START TIME": subject_start_time, "SUBJECT END TIME": subject_end_time, "SUBJECT DAY": subject_day}
                with open(file=SCHEDULES_FILE_NAME, mode="w") as schedules_json:
                    schedules_json.write(json.dumps(schedules_json_data, indent=4))
            break
    

    # THIS FUNCTION GETS THE INPUT OF THE USER ASKING WHETHER THE USER IS DONE ENTERING ALL SCHEDULES OR NOT
    def get_user_done_add_schedule(self) -> int:
        print(f"ARE YOU DONE ENTERING ALL YOUR SCHEDULES\n\n[1] YES\n[2] NO\n{BORDER}\n")
        while True:
            try:
                is_user_done: int = int(input("INPUT: "))
            except ValueError:
                continue
            if is_user_done > 2 or is_user_done < 1:
                continue
            else:
                return is_user_done
    

    # THIS FUNCTION LOOPS AND ENUMERATE THROUGH THE TUPLE CALLED SUBJECT_TUPLE AND PRINTS THE ELEMENT AND GETS THE USER'S INPUT AFTER THE LOOP
    def display_subject_items(self) -> str:
        while True:
            clr_terminal()
            print(f"{BORDER}\n        SELECT A SUBJECT CODE\n{BORDER}\n{BORDER}\n")
            for num, item in enumerate(iterable=SUBJECT_TUPLE, start=1):
                print(f"        [{num}] {item}")
            print(f"\n{BORDER}")
            try:
                subject_code: int = int(input("INPUT: "))
            except ValueError:
                continue
            if subject_code > len(SUBJECT_TUPLE) or subject_code < 1:
                continue
            else:
                return SUBJECT_TUPLE[subject_code - 1]
    

    # THIS FUNCTION LOOPS AND ENUMERATE THROUGH THE TUPLE CALLED TIME_TUPLE PRINTS THE ELEMENT AND GETS THE USER'S INPUT AFTER THE LOOP
    def display_time_items(self, title: str) -> int:
        while True:
            print(BORDER)
            print(f"        SELECT A SUBJECT {title} TIME")
            print(BORDER)
            print(f"{BORDER}\n")
            for num, item in enumerate(iterable=TIME_TUPLE, start=1):
                print(f"        [{num}] {item}")
            print(f"\n{BORDER}")
            if title == "START":
                try:
                    subject_start_time: int = int(input("INPUT: "))
                except ValueError:
                    continue
                if subject_start_time > len(TIME_TUPLE) or subject_start_time < 1:
                    continue
                else:
                    return TIME_TUPLE[subject_start_time - 1]
            else:
                try:
                    subject_end_time: int = int(input("INPUT: "))
                except ValueError:
                    continue
                if subject_end_time > len(TIME_TUPLE) or subject_end_time < 1:
                    continue
                else:
                    return TIME_TUPLE[subject_end_time - 1]
    

    # THIS FUNCTION LOOPS AND ENUMERATE THROUGH THE TUPLE CALLED DAY_TUPLE AND PRINTS THE ELEMENT AND GETS THE USER'S INPUT AFTER THE LOOP
    def display_day_items(self) -> str:
        while True:
            print(BORDER)
            print("        SELECT A SUBJECT DAY")
            print(BORDER)
            print(f"{BORDER}\n")
            for num, item in enumerate(iterable=DAY_TUPLE, start=1):
                print(f"        [{num}] {item}")
            print(f"\n{BORDER}")
            
            try:
                subject_day: int = int(input("INPUT: "))
            except ValueError:
                continue
            
            if subject_day > len(SUBJECT_TUPLE) or subject_day < 1:
                continue
            else:
                return DAY_TUPLE[subject_day - 1]
    

    # THIS FUNCTION SORTS THE SCHEDULES BY THE SBUJECT'S START TIME IN ASCENDING ORDER
    def sort_schedule(self) -> None:
        with open(file=SCHEDULES_FILE_NAME, mode='r') as schedules_json:
            schedules_json_data = json.load(schedules_json)
        for day in schedules_json_data.keys():
            if len(schedules_json_data[day]) < 2:
                continue
            
            subject_values = [] 
            for attrs in schedules_json_data[day].values():
                subject_values.append(attrs)
                
            sorted_monday_schedule = sorted(subject_values, key=lambda x: x["SUBJECT START TIME"])
            print(sorted_monday_schedule)
            
            schedules_json_data[day] = {}
            for values in sorted_monday_schedule:
                schedules_json_data[day][values['SUBJECT CODE']] = values
                with open(file=SCHEDULES_FILE_NAME, mode='w') as schedules_json:
                    schedules_json.write(json.dumps(schedules_json_data, indent=4))
    

    # THIS FUNCTION ACCESS THE DATA OF JSON FILE AND CONVERTS DATA TO PYTHON DICTIONARY AND GETS THE USER INPUT IF TO VIEW SPECIFIC DAY OF SCHEDULE OR VIEW ALL SCHEDULES OR TO QUIT THE VIEW SCHEDULE
    def view_schedules(self) -> None:
        with open(file=SCHEDULES_FILE_NAME, mode="r") as schedules_json:
            schedules_json_data = json.load(schedules_json)
        while True:
            clr_terminal()
            print(f"{BORDER}")
            print(f"        VIEW SCHEDULE")
            print(f"{BORDER}\n")
            print(f"    [1] VIEW ALL SCHEUDULES")
            print(f"    [2] SELECT SCHEUDULE")
            print(f"    [3] QUIT")
            print(f"\n{BORDER}")
            try:
                view_schedule_select: int = int(input("INPUT: "))
            except ValueError:
                continue
            if view_schedule_select == 1:
                clr_terminal()
                print(f"{BORDER}")
                print(f"        VIEW SCHEDULE")
                for day, subjs in schedules_json_data.items():
                    print(f"{BORDER}")
                    print(f"\n{day}:")
                    for subj, attrs in subjs.items():
                        print(f"    {subj}:")
                        for attr, val in attrs.items():
                            print(f"        {attr}: {val}")
                    print(f"\n{BORDER}")
                x = input("PRESS ENTER TO CONTINUE...")
            elif view_schedule_select == 2:
                while True:
                    clr_terminal()
                    print(f"{BORDER}")
                    print(f"        VIEW SCHEDULE")
                    print(f"{BORDER}\n")
                    for num, day in enumerate(DAY_TUPLE, start=1):
                        print(f"    [{num}] {day} SCHEDULE")
                    print(f"\n{BORDER}")
                    try:
                        schedule_select: int = int(input("INPUT: "))
                    except ValueError:
                        continue
                    if schedule_select > len(SUBJECT_TUPLE) or schedule_select < 0:
                        continue
                    else:
                        clr_terminal()
                        print(f"{BORDER}")
                        print(f"        VIEW SCHEDULE")
                        print(f"{BORDER}\n")
                        day = DAY_TUPLE[schedule_select-1]
                        print(f"{day}")
                        for subj, attrs in schedules_json_data[day].items():
                            print(f"    {subj}")
                            for attr, val in attrs.items():
                                print(f"    {attr}: {val}")
                        print(f"\n{BORDER}")
                    x = input("PRESS ENTER TO CONTINUE...")
                    break
            elif view_schedule_select == 3:
                break
            else:
                continue
                    

    # THIS FUNCTION CLEARS THE SCHEDULE
    def clear_schedule(self) -> None:
        try:
            with open(file=SCHEDULES_FILE_NAME, mode="w") as notes_json:
                notes_json.write(json.dumps(schedules, indent=4))
        except FileNotFoundError:
            print("INVALID, FILE DOES NOT EXIST")
    

    # THIS FUNCTION GETS THE USER CONFIRMATION IF THE USER REALY WANTS TO CLEAR THE SCHEDULE
    def get_clear_schedule_confirmation(self) -> int:
        while True:
            print(BORDER)
            print("ARE YOU SURE DO YOU WANT TO CLEAR YOUR SCHEDULE")
            print("[1] YES")
            print("[2] NO")
            print(BORDER)
            try:
                user_input: int = int(input("INPUT:"))
            except:
                continue
            return user_input
# --------------------------------------------------




# --------------------------------------------------
# NOTES
class Notes:
    # THIS FUNCTION GETS THE INPUT OF THE USER, SUBJECT, TOPIC, DEFINITION, KEYWORD OF NOTES
    def add_notes(self) -> None:
        notes_subject: str = Notes_.get_user_input_notes(title="SUBJECT")
        notes_topic: str = Notes_.get_user_input_notes(title="TOPIC").upper()
        notes_definition: str = Notes_.get_user_input_notes(title="DEFINTION").upper()
        notes_keyword: str = Notes_.get_user_input_notes(title="KEYWORD").upper()
        try:
            # CREATES A JSON FILE IF THE FILE DOESN'T EXISTS
            with open(NOTES_FILE_NAME, "x") as notes_json:
                notes_json_data = json.dumps(obj=notess, indent=4)
                notes_json.write(notes_json_data)
            with open(NOTES_FILE_NAME, mode="r") as notes_json:
                notes_json_data = json.load(notes_json)
        except FileExistsError:
            # ACCESS THE DATA OF JSON FILE AND CONVERTS THE DATA TO PYTHON DICTIONARY
            with open(NOTES_FILE_NAME, "r") as notes_json:
                notes_json_data = json.load(notes_json)
        # ASSIGN THE USER'S NOTES TO THE RESPECTIVE SUBJECT
        notes_json_data[notes_subject] = {notes_topic: {"TOPIC": notes_topic, "DEFINITION": notes_definition, "KEYWORD": notes_keyword}}
        with open(NOTES_FILE_NAME, "w") as notes_json:
            notes_json.write(json.dumps(obj=notes_json_data, indent=4))
    

    # THIS FUNCTION ASKS THE USER WHETHER THE USER IS DONE ENTERING THE NOTES OR NOT 
    def get_user_done_add_notes(self) -> int:
        while True:
            print(f"{BORDER}ARE YOU DONE ENTERING YOUR NOTES{BORDER}\n\n[1] YES\n[2] NO\n{BORDER}")
            try:
                is_user_done: int = int(input("INPUT: "))
            except:
                continue
            if is_user_done > 2 or is_user_done < 1:
                continue
            else:
                return is_user_done
    

    # THIS FUNCTION CLEAR THE NOTES AND GETS THE USER CONFIRMATION IF THE USER REALY WANTS TO CLEAR THE SCHEDULE OR NOT
    def clear_notes(self) -> None:
        user_confirmation: int = int(input("ARE YOU SURE DO YOU WANT TO CLEAR YOUR NOTES"))
        if user_confirmation == 1:
            with open(file=NOTES_FILE_NAME, mode="w") as notes_json:
                notes_json.write(json.dumps(obj=notess, indent=4))
    

    # THIS FUNCTION GETS THE USER'S INPUT
    def get_user_input_notes(self, title: str) -> str:
        clr_terminal()
        print(f"{BORDER}\nENTER A {title}\n{BORDER}")
        if title == "SUBJECT":
            print("")
            for num, subj in enumerate(SUBJECT_TUPLE, start=1):
                print(f"    [{num}] {subj}")
            print(f"\n{BORDER}")
            user_input_int: int = int(input("INPUT: "))
            return SUBJECT_TUPLE[user_input_int - 1]
        else:
            user_input: str = input("INPUT: ")
            return user_input.upper()
    

    # THIS FUNCTION PRINTS ALL THE NOTES
    def view_notes(self) -> None:
        with open(file=NOTES_FILE_NAME, mode="r") as notes:
            json_data = json.load(notes)
        print(f"{BORDER}\n            ADD NOTES")
        for subj, topics in json_data.items():
            if len(topics) == 0: 
                print(f"{subj}: DOESN'T HAVE A TOPIC")
                print(f"{BORDER}")
            else:
                print(f"{BORDER}\n")
                print(f"{subj}:")
            for topic, attrs in topics.items():
                for attr, val in attrs.items():
                    print(f"*{attr}: {val}")
                print(f"\n{BORDER}")
# --------------------------------------------------




# --------------------------------------------------
# FLASHCARDS
class Flashcards:
    # THIS FUNCTION ACCESS THE DATA OF JSON FILE CONVERTS IT INTO PYTHON DICTIONARY AND LOOPS THROUGH THE DCTIONARY AND CHECKS IF THE SUBJECT HAS A NOTES, IF THE SUBJECT HAS A NOTE IT APPENDS THE SUBJECT TO A LIST CALLED <notes_subj>
    # AND RANDOMIZES THE <notes_subj> AND ASSIGN THE VALUE TO <random_subj> AND LOOPS THROUGH TO TOPICS OF THE SUBJECT AND APPENDS ALL THE TOPICS TO A LIST CALLED <notes_topic>
    # AND RANDOMIZES THE <notes_topic> AND ASSIGN THE VALUE TO <random_topic> AND ASSIGN THE DEFINITION, AND KEYWORD OF THE TOPIC AND RETURNS THE <random_subj, random_topic, random_definition, random_keyword>
    def play_flashcards(self) -> tuple:
        with open(file=NOTES_FILE_NAME, mode="r") as flashcards_json:
            flashcards_json_data = json.load(flashcards_json)
        notes_subj = []
        notes_topic = []
        for subj in flashcards_json_data.keys():
            if len(flashcards_json_data[subj]) != 0:
                notes_subj.append(subj)
        random_subj = rand.choice(notes_subj)
        for topic in flashcards_json_data[random_subj].keys():
            notes_topic.append(topic)
        random_topic = rand.choice(notes_topic)
        random_definition = flashcards_json_data[random_subj][random_topic]["DEFINITION"]
        random_keyword = flashcards_json_data[random_subj][random_topic]["KEYWORD"]
        return random_subj, random_topic, random_definition, random_keyword
    

    # THIS FUNCTION SETS HOW MANY FLASHCARDS 
    def set_flashcards_num(self, flashcards_num: int):
        print(f"{BORDER}\n        SETTINGS\n{BORDER}\n\n    NUMBER OF FLASHCARDS: {flashcards_num}\n\n{BORDER}")
        flashcards_num = int(input("SET NUMBER OF FLASHCARDS: "))
        return flashcards_num
    

    # THIS FUNCTION QUITS THE FLASHCARDS SETTINGS TO THE MAIN MENU OF FLASHCARDS AND ASKS THE USER WHETHER TO QUIT THE FLASHCARDS SETTINGS OR QUIT THE PROGRAM 
    def quit_flashcards_settings(self):
        '''1 = quit, 2 = continue'''
        while True:
            clr_terminal()
            try:
                user_confirmation: int = int(input(f"{BORDER}\n\n    [1] QUIT SETTINGS\n    [2] QUIT PROGRAM\n\n{BORDER}\nINPUT: "))
            except ValueError:
                continue
            if user_confirmation == 1: # QUIT SETTINGS
                return user_confirmation
            elif user_confirmation == 2: # QUIT PROGRAM
                sys.exit()
            else:
                continue
# --------------------------------------------------





# --------------------------------------------------
# HANGMAN
class Hangman:
    # THIS FUNCTION ACCESS THE DATA OF JSON FILE CONVERTS IT INTO PYTHON DICTIONARY AND LOOPS THROUGH THE DCTIONARY AND CHECKS IF THE SUBJECT HAS A NOTES, IF THE SUBJECT HAS A NOTE IT APPENDS THE SUBJECT TO A LIST CALLED <hangman_subj>
    # AND RANDOMIZES THE <hangman_subj> AND ASSIGN THE VALUE TO <random_subj> AND LOOPS THROUGH TO TOPICS OF THE SUBJECT AND APPENDS ALL THE TOPICS TO A LIST CALLED <hangman_topic>
    # AND RANDOMIZES THE <hangman_topic> AND ASSIGN THE VALUE TO <random_topic> AND ASSIGN THE DEFINITION, AND KEYWORD OF THE TOPIC AND RETURNS THE <correct_keyword, random_subj, random_definition>
    def play_hangman(self) -> tuple:
        clr_terminal()
        with open(file=NOTES_FILE_NAME, mode="r") as hangman_json:
            hangman_json_data = json.load(hangman_json)
        hangman_subj: list = []
        for subj in hangman_json_data.keys():
            if len(hangman_json_data[subj]) != 0:
                hangman_subj.append(subj)
        random_subj: str = rand.choice(hangman_subj)
        hangman_topic: list = []
        for topic in hangman_json_data[random_subj]:
            if len(hangman_json_data[random_subj]) != 0:
                hangman_topic.append(topic)
        random_topic: str = rand.choice(hangman_topic)
        correct_keyword: str = hangman_json_data[random_subj][random_topic]["KEYWORD"]
        hangman_definition: str = hangman_json_data[random_subj][random_topic]["DEFINITION"]
        return correct_keyword, random_subj, hangman_definition
    

    # THIS FUNCTION GETS THE USER'S INPUT AND ASKS WHETHER TO SET HANGMAN ROUNDS OR TO QUIT THE HANGMAN SETTINGS
    def get_user_input_hangman_settings(self) -> int:
        '''1: set hangman rounds, 2: quit hangman settings'''
        while True:
            try:
                user_input: int = int(input("INPUT: "))
            except:
                continue
            if user_input <= 2 and user_input >= 1:
                return user_input


    # THIS FUNCITON SETS THE ROUND OF HANGMAN
    def set_hangman_rounds(self):
        while True:
            clr_terminal()
            print(f"{BORDER}\n        SET HANGMAN ROUNDS\n{BORDER}\n\n        HANGMAN ROUNDS: {hangman_rounds}\n\n{BORDER}\nNOTE: TYPE NOTHING IF YOU WANT TO CANCEL THE SETTING OF HANGMAN ROUNDS\n{BORDER}")
            try:
                rounds: int = int(input("INPUT: "))
            except:
                return hangman_rounds
            return rounds
        
    
    # THIS FUNCTION QUITS THE HANGMAN SETTINGS AND ASKS WHETHER TO QUIT THE HANGMAN SETTIGNS OR TO QUIT THE PROGRAM
    def quit_hangman_settings(self) -> None:
        while True:
            clr_terminal()
            print(f"{BORDER}\n\n    [1] QUIT HANGMAN SETTINGS\n    [2] QUIT PROGRAM\n\n{BORDER}")
            try:
                user_input_quit: int = int(input("INPUT: "))
            except:
                continue
            if user_input_quit == 1: # QUIT HANGMAN SETTINGS
                break
            elif user_input_quit == 2: # QUIT PROGRAM
                sys.exit()
            else:
                continue


# THIS FUNCTION CLEARS THE TERMINAL
def clr_terminal() -> None:
    os.system('cls')
    time.sleep(0.5)




# SCHEDULE ORGANIZER
SCHEDULE_ORGANIZER_MAIN_MENU_ITEMS: tuple = ("ADD SCHEDULE", "VIEW SCHEDULE", "CLEAR SCHEDULE", "QUIT")
SUBJECT_TUPLE: tuple = ("ET1", "CPET1L", "ET1L", "PATHFIT1", "GEC1", "CHET", "MATHANA13", "GEC4", "BET1", "CHETL", "NSTP", "CWTS")
TIME_TUPLE = (700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900)
DAY_TUPLE: tuple = ("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY")
SCHEDULES_FILE_NAME = "schedules.json"
schedules: dict = {"MONDAY": {}, "TUESDAY": {}, "WEDNESDAY": {}, "THURSDAY": {}, "FRIDAY": {}, "SATURDAY": {},}
sorted_schedules: dict = {"MONDAY": {}, "TUESDAY": {}, "WEDNESDAY": {}, "THURSDAY": {}, "FRIDAY": {}, "SATURDAY": {},}
start_time_list: dict = {"MONDAY": [], "TUESDAY": [], "WEDNESDAY": [], "THURSDAY": [], "FRIDAY": [], "SATURDAY": []}
foo_schedule_file_name = "schedule_placeholder.json"
schedule_organizer_input: int = 0


# NOTES VARIABLES
NOTES_MAIN_MENU_ITEMS: list = ["ADD NOTES", "VIEW NOTES", "CLEAR NOTES", "QUIT"]
NOTES_FILE_NAME: str = "notes.json"
notess: dict = {"ET1": {}, "CPET1L": {}, "ET1L": {}, "PATHFIT1": {}, "GEC1": {}, "CHET": {}, "MATHANA13": {}, "GEC4": {}, "BET1": {}, "CHETL": {}, "NSTP": {}, "CWTS": {}}
NOTES_PLACEHOLDER_FILE_NAME = "notes_placeholder.json"
notes_input: int = 0


# FLASHCARDS VARIABLE
FLASHCARDS_MAIN_MENU_ITEMS: list = ["PLAY FLASHCARDS", "SETTINGS", "QUIT"]
FLASHCARDS_SETTINGS_MENU_ITEMS: list = ["SET NUMBER OF FLASHCARDS", "QUIT"]
run_flashcards_settings: bool = False
flashcards_num: int = 5
flashcards_input: int = 0

# HANGMAN VARIABLE
HANGMAN_MAIN_MENU_ITEMS: list = ["PLAY HANGMAN", "SETTINGS", "QUIT"]
HANGMAN_SETTINGS_MENU_ITEMS: list = ["SET HANGMAN ROUNDS", "QUIT"]
HANGMAN_MAX_ATTEMPTS: int = 7
hangman_points: int = 0
hangman_attempts: int = 0
hangman_rounds: int = 5
hangman_input: int = 0
HANGMAN_PICS = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']

MAIN_MENU_ITEMS: list = ["SCHEDULE ORGANIZER", "NOTES", "FLASHCARD", "HANGMAN", "QUIT"]

BORDER: str = "----------------------------------"
# --------------------------------------------------
#  MAIN
# def main() -> None:

Schedule_Organizer = ScheduleOrganizer()
Notes_ = Notes()
Flashcards_ = Flashcards()
Hangman_ = Hangman()


try:
    # THIS BLOCK OF CODE ACCES THE DATA OF THE FILE AND IF THE FILE DOESN'T HAVE ANY DATA IT OVERWRITES THE FILE WITH NEW DATA
    with open(file=SCHEDULES_FILE_NAME, mode="r") as schedules_json:
        schedules_json_data = json.load(schedules_json)
    if len(schedules_json_data) == 0:
        with open(file=SCHEDULES_FILE_NAME, mode="w") as schedules_json:
            schedules_json.write(json.dumps(schedules, indent=4))
except json.JSONDecodeError:
    # THIS BLOCK OF CODE CREATES AND WRITES A FILE
    with open(file=SCHEDULES_FILE_NAME, mode="w") as schedules_json:
            schedules_json.write(json.dumps(schedules, indent=4))
            
while True:
    display_welcome_message()
    
    try:
        main_menu_input: int = int(input("INPUT: "))
    except ValueError:
        print("INVALID INPUT, MUST BE A INTEGER")
        continue
    
    if main_menu_input > len(MAIN_MENU_ITEMS) or main_menu_input < 1:
        print("INPUT INVALID OUT OF INDEX")
        continue
    
    while True:
        run_schedule_organizer: bool = False
        run_notes: bool = False
        run_flashcards: bool = False
        run_hangman: bool = False
        
        match main_menu_input:
            case 1:
                display_main_menu_items(array=SCHEDULE_ORGANIZER_MAIN_MENU_ITEMS, title="SCHEDULE ORGANIZER")
                try:
                    schedule_organizer_input: int = int(input("INPUT: "))
                    run_schedule_organizer = True
                except ValueError:
                    break
            case 2:
                display_main_menu_items(array=NOTES_MAIN_MENU_ITEMS, title="NOTES")
                try:
                    notes_input: int = int(input("INPUT: "))
                except ValueError:
                    break
                run_notes = True
                try:
                    with open(file=NOTES_FILE_NAME, mode="x") as notes_json:
                        notes_data = json.dumps(obj=notess, indent=4)
                        notes_json.write(notes_data)
                except FileExistsError:
                    pass
            case 3:
                display_main_menu_items(array=FLASHCARDS_MAIN_MENU_ITEMS, title="FLASHCARDS")
                try:
                    flashcards_input: int = int(input("INPUT: "))
                except ValueError:
                    break
                run_flashcards: bool = True
            case 4:
                display_main_menu_items(array=HANGMAN_MAIN_MENU_ITEMS, title="    HANGMAN")
                try:
                    hangman_input: int = int(input("INPUT: "))
                except ValueError:
                    break
                run_hangman = True
            case 5:
                quit()
        
        # ----------------------------------------------------------------
        # SCHEDULE ORGANIZER
        if run_schedule_organizer == True:
            if schedule_organizer_input == 1: # ADD SCHEDULE
                while True:
                    Schedule_Organizer.add_schedule()
                    Schedule_Organizer.sort_schedule()
                    is_user_done: int = Schedule_Organizer.get_user_done_add_schedule()
                    if is_user_done == 1:
                        break
                    
                    else:
                        continue
                
            elif schedule_organizer_input == 2: # VIEW SCHEDULES
                Schedule_Organizer.view_schedules()
                
            elif schedule_organizer_input == 3: # CLEAR SCHEDULE
                user_input: int = Schedule_Organizer.get_clear_schedule_confirmation()
                if user_input == 1:
                    Schedule_Organizer.clear_schedule()
                    
                else:
                    break
                
            elif schedule_organizer_input == 4: # QUIT
                user_input: int = quit_to_main_menu(title="SCHEDULE ORGANIZER")
                if user_input == 1:
                    break
            
        # ----------------------------------------------------------------
        # NOTES
        if run_notes == True:
            if notes_input == 1: # ADD NOTES
                while True:
                    Notes_.add_notes()
                    is_user_done: int = Notes_.get_user_done_add_notes()
                    if is_user_done == 1:
                        break
                    
                    else:
                        continue
            elif notes_input == 2: # VIEW NOTES
                clr_terminal()
                Notes_.view_notes()
                x = input("PRESS ENTER TO CONTINUE...")
                
            elif notes_input == 3: # CLEAR NOTES
                Notes_.clear_notes()
                print(f"{BORDER}")
                print(f"        NOTES HAVE BEEN CLEARED")
                print(f"{BORDER}")
                time.sleep(1.5)
                
            elif notes_input == 4: # QUIT NOTES
                user_input: int = quit_to_main_menu(title="NOTES")
                if user_input == 1:
                    break
            
        # ----------------------------------------------------------------
        # FLASHCARDS
        run_flashcards_settings: bool = False
        if run_flashcards == True:
            if flashcards_input == 1: # PLAY FLASHCARDS
                clr_terminal()
                for i in range(flashcards_num):
                    flashcards_subj, flashcards_topic, flashcards_definition, flashcards_keyword = Flashcards_.play_flashcards()
                    print(f"{BORDER}")
                    print(f"        PLAYING FLASHCARD")
                    print(f"{BORDER}\n")
                    print(f"    SUBJECT: {flashcards_subj}:")
                    print(f"    TOPIC: {flashcards_topic}:")
                    print(f"    DEFINITION: {flashcards_definition}")
                    print(f"\n{BORDER}")
                    print("INSTRUCTIONS: TYPE THE CORRECT KEYWORD")
                    print(BORDER)
                    print("TO QUIT TYPE 'QUIT'")
                    print(BORDER)
                    user_input_keyword: str = input("INPUT: ")
                    if user_input_keyword == flashcards_keyword:
                        print(f"{BORDER}\n    CORRECT ANSWER!!:>\n{BORDER}")
                        x = input("PRESS ENTER TO CONTINUE")
                    
                    elif user_input_keyword == "QUIT":
                        break
                    
                    else:
                        print(f"{BORDER}")
                        print(f"        PLAYING FLASHCARD")
                        print(f"{BORDER}\n")
                        print(f"    SUBJECT: {flashcards_subj}:")
                        print(f"    TOPIC: {flashcards_topic}:")
                        print(f"    DEFINITION: {flashcards_definition}")
                        print(f"    KEYWORD: {flashcards_keyword}")
                        print(f"\n{BORDER}")
                        x = input("PRESS ENTER TO CONTINUE")
                        continue
                
            elif flashcards_input == 2: # FLASHCARDS SETTINGS
                while True:
                    clr_terminal()
                    print(f"{BORDER}\n        FLASHCARDS SETTINGS\n{BORDER}\n")
                    print(f"    NUMBER OF FLASHCARDS: {flashcards_num}\n\n{BORDER}\n")
                    for num, settings in enumerate(FLASHCARDS_SETTINGS_MENU_ITEMS, start=1):
                        print(f"    [{num}] {settings}")
                    print(f"\n{BORDER}")
                    try:
                        settings_menu_input: int = int(input("INPUT: "))
                    except ValueError:
                        continue

                    if settings_menu_input == 1: # SET FLASHCARDS NUM
                        flashcards_num = Flashcards_.set_flashcards_num(flashcards_num=flashcards_num)
                        user_exit_code: int = 2
                        
                    elif settings_menu_input == 2: # QUIT FLASHCARDS SETTINGS
                        user_exit_code: int = Flashcards_.quit_flashcards_settings()
                        if user_exit_code == 1:
                            break
                        
                    else:
                        continue
                    
            elif flashcards_input == 3: # QUIT 
                user_input: int = quit_to_main_menu(title="FLASHCARDS")
                if user_input == 1:
                    break
        
        # ----------------------------------------------------------------
        # HANGMAN
        if run_hangman == True:
            if hangman_input == 1: # PLAY HANGMAN
                for i in range(hangman_rounds):
                    hangman_keyword, hangman_subj, hangman_definition = Hangman_.play_hangman()
                    while True:
                        clr_terminal()
                        print(f"{BORDER}")
                        print(f"             HANGMAN")
                        print(f"{BORDER}\n")
                        print(f"    POINTS: {hangman_points}")
                        print(f"    USER ATTEMPTS: {hangman_attempts}")
                        print(f"\n{BORDER}")
                        print(f"{HANGMAN_PICS[hangman_attempts]}\n")
                        print(f"    SUBJECT: {hangman_subj}")
                        print(f"    DEFINITION: {hangman_definition}")
                        print(f"\n{BORDER}")
                            
                        if hangman_attempts == HANGMAN_MAX_ATTEMPTS - 1:
                            print(f"{BORDER}\n")
                            print(f"\t    GAME OVER")
                            print(f"\n{BORDER}")
                            print(f"\tYOU GOT {hangman_points} POINTS")
                            print(f"{BORDER}")
                            hangman_attempts = 0
                            x = input("PRESS ENTER TO CONTINUE...")
                            break
                        
                        user_input_keyword: str = input("INPUT: ")
                        if user_input_keyword == hangman_keyword:
                            # clr_terminal()
                            print(f"{BORDER}\n    CORRECT ANSWER!!:>\n{BORDER}")
                            hangman_points+=1
                            hangman_attempts = 0
                            x = input("PRESS ENTER TO CONTINUE...")
                            break
                        
                        else:
                            # clr_terminal()
                            print(f"{BORDER}\n\tSORRY WRONG ANSWER\n{BORDER}")
                            hangman_attempts+=1
                            x = input("PRESS ENTER TO CONTINUE...")
                            
                    if hangman_attempts == HANGMAN_MAX_ATTEMPTS:
                        break
                        
            elif hangman_input == 2: # HANGMAN SETTINGS
                while True:
                    clr_terminal()
                    print(f"{BORDER}")
                    print(f"        HANGMAN SETTINGS")
                    print(f"{BORDER}\n")
                    for num, menu_item in enumerate(HANGMAN_SETTINGS_MENU_ITEMS, start=1):
                        print(f"    [{num}] {menu_item}")
                    print(f"\n{BORDER}")
                    hangman_settings_menu_input: int = Hangman_.get_user_input_hangman_settings()
                    if hangman_settings_menu_input == 1:
                        hangman_rounds = Hangman_.set_hangman_rounds()
                        
                    elif hangman_settings_menu_input == 2:
                        Hangman_.quit_hangman_settings()
                    break
            
            elif hangman_input == 3: # QUIT HANGMAN
                user_exit_code = quit_to_main_menu(title="HANGMAN")
                if user_exit_code == 1:
                    break
            
