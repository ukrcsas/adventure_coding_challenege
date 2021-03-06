
from math import floor
import colorama
import time
from colorama import Fore
import pyttsx3
from playsound import playsound



engine = pyttsx3.init()
count_dog = 0
count_treat = 0
count_crisp = 0
count_key =0

def floor_13_map():
    floor_13 = print(Fore.RED +'''
\n *****************************\n
FLOOR 13
                    ----------------
                    |              |
                    | ELEVATOR     |
                    |              |
                    ------|   |-----
                          |   | 
                     -----     ------
                     |LINDSEY's OFFICE|
                     ----------------
\n *****************************\n
''')


def floor_10_map():
    floor_10 = print(Fore.RED +'''
\n *****************************\n
FLOOR 10
                    ----------------
                    |              |
                    | DESK CLUSTER |
                    |              |
---------------     ------|   |-----
|             |           |   | 
|MEETING ROOM |       ----     ----            ---------------
|             |------|  ELEVATORS  | -------- | KITCHEN AREA  |
--------------       -------------             ---------------
\n *****************************\n
''')


def floor_11_map():
    floor_11 = print(Fore.RED +'''
\n *****************************\n
FLOOR 11
                    ----------------
                    |              |
                    | DESK CLUSTER |
                    |              |
---------------     ------|   |-----
|             |           |   | 
|  CANTEEN    |      ----     ----        ---------------
|             |    ------|    | -------- | TREASURE CHECK  |
--------------       -------------        ---------------
\n *****************************\n
''')


def start ():
    print ( "\n *****************************\n")
    print (Fore.LIGHTMAGENTA_EX +"\nWelcome to the Adventure Game!\nLet's get started!\n")
    engine.say("Welcome to the Adventure Game Let's get started!")
    engine.runAndWait()
    print(Fore.LIGHTMAGENTA_EX + "\n *****************************\n")
    print (Fore.CYAN +"Your eyes slowly open and you quickly realise that you are in the Manchester KPMG Office. You scan the room and see that you are alone in the desk cluster on Floor 10.\nThe once vibrant space is now dark, cold and empty with a strange chill to the air.\n")
    print ("You feel your phone buzz in your pocket\nCheck your phone? (yes/no)\n") 
    playsound('telephone.wav')

    ans =  input()
    phone = "ringing"

    while phone == "ringing":
        if ans.upper() == "NO":
            print(Fore.LIGHTRED_EX +"You decide to ignore your phone buzzing, it can't be that urgent and someone else will probably sort out whatever the issue is.\nYou close your eyes and go back to sleep")
            print ("\n *****************************\n")
            print ("GAME OVER - YOUR LAZINESS RESULTED IN THE DOWNFALL OF KPMG")
            playsound('Gameover.mp3')
            break
        elif ans.upper() == "YES":
            print(Fore.GREEN + "\nYou grab your phone from your pocket and see 27 missed calls and 3 unopened messages from Balajee\nYou should probably find out why he is trying to get in contact so urgently.\n \nDo you want to ring him back or read the messages?\n(call balajee/read messages)\n")
            balajee = "one"
            question = input()
            while balajee == "one":
                if question.upper() == "READ MESSAGES":
                    balajee = "two"
                    print(Fore.LIGHTWHITE_EX +"\nYou unlock your phone and look at the messages Balajee has sent you:\n")
                    print("\n[00:37] Sugumaran, Balajee:\nAre you still in the office?! I need your help urgently! PLEASE!!")
                    print("\n[00:38] Sugumaran, Balajee:\nWe evacuated the office after all the strange noises and earthquakes but you were sleeping so soundly no one dared to wake you!")
                    print("\n[00:38] Sugumaran, Balajee:\nLindsey was taken by one of those THINGS. You need to find her and get out of there! We sealed the doors and only Lindsey's pass will becheck able to open them! ")
                    print("\n[00:39] Sugumaran, Balajee:\nDon't forget to check the map on your phone if you get lost!\n")
                elif question.upper() == "CALL BALAJEE":
                    print(Fore.BLUE+"\nYou call Balajee. The phone rings for a couple of minutes but he doesn't pick up. You give up and end the call")
                    print(Fore.BLUE + "Do you want to try and call again or read the messages?(read messages/call again)\n")
                    question2 = input()
                    if question2.upper() == "CALL AGAIN" or question2.upper() == "CALL BALAJEE":
                        engine.say("No answer from Balajee, Please read message instead?")
                        engine.runAndWait()
                        print("\nYou try to call Balajee again but there is still no answer. It seems ringing him is a waste of time. (Call again/read messages)\n")
                        question = input()
                    elif question2.upper() == "READ MESSAGES":
                        balajee = "two"
                        print(Fore.BLUE +"\nYou unlock your phone and look at the messages Balajee has sent you:\n")
                        print(Fore.LIGHTWHITE_EX+"\n[00:37] Sugumaran, Balajee:\nAre you still in the office?! I need your help urgently! PLEASE!!")
                        print("\n[00:38] Sugumaran, Balajee:\nWe evacuated the office after all the strange noises and earthquakes but you were sleeping so soundly no one dared to wake you!")
                        print("\n[00:38] Sugumaran, Balajee:\nLindsey was taken by one of those THINGS. You need to find her and get out of there! We sealed the doors and only Lindsey's pass will be able to open them!")
                        print("\n[00:39] Sugumaran, Balajee\nDon't forget to check the map on your phone if you get lost!\n")
                    else:
                        print(Fore.BLUE +"What are you going to? (call Balajee/read messages)\n")
                        question = input()
                else:
                    print(Fore.BLUE +"\nYou should probably read those messages or try to get in contact with Balajee before you go anywhere. \nWhat are you going to do? (call balajee/read messages)\n")
                    question = input()

            phone = "answered"
            map_check()
        else:
            print("You gonna answer the phone or what? (yes/no)")
            ans = input()

def map_check():
    checked_map = False
    while checked_map == False:
            print(Fore.BLUE +"\nCheck your map by inputting \"check map\" - try it now\n")
            map_check = input()
            if map_check.upper() == "CHECK MAP":
                playsound('door.wav')
                floor_10_map()
                checked_map = True
            elif map_check.upper() != "CHECK MAP":
                print(Fore.BLUE +"\nYou need to look at your map to see where you are and where to head to next!\n")
            else:
                print(Fore.BLUE +"Check your map you wally! You don't want to get lost")
    floor_10(count_dog, count_treat)

def floor_10(count_dog, count_treat):
    elevator = False
    while elevator == False:
        print("\nWhere are you going next?\n")
        direction = input()
        if direction.upper() == "ELEVATORS":
            print(Fore.BLUE +"\nYou make your way over to the elevators. You stand at in the corridor and think about what to do next - use the elevators or investigate the other rooms?\n(use the elevators/meeting room/kitchen area)\n")
            movement = input()
            if movement.upper() == "USE THE ELEVATORS" and count_dog != 1 and count_treat != 1:
                print(Fore.BLUE +"\nYou're about to use the elevators but then you think you have not investigated the other rooms!\nWhat if there are some important items in them or if someone spent ages coding going into those rooms.\nYou decide not investigating the rest of the floor would be rude and instead think which room you should look in first\n")
            elif movement.upper() == "ELEVATORS" or "ELEVATOR" and count_dog == 1 and count_treat == 1:
                print(Fore.BLUE +"\nContent you have found everything on this floor you --------- ")
                #this is where the other floors/levels need their functions placing 
            elif movement.upper() == "MEETING ROOM":
                meeting_room(count_dog, count_treat)
            elif movement.upper() == "KITCHEN AREA":
                kitchen_area()
        elif direction.upper() == "MEETING ROOM":
            meeting_room(count_treat, count_dog)
        elif direction.upper() == "KITCHEN AREA":
            kitchen_area()
        elif direction.upper() == "ELEVATORS":
            print(Fore.BLUE +"\nYou are already at the elevators\n")
            print(Fore.BLUE +"\nWhere do you want to go next?\n")
            playsound('door.wav')
            direction = input()
        else:
            print(Fore.BLUE +"\n Sorry did you mean - elevators/meeting room/ktichen area?\n")
            playsound('door.wav')
            direction = input()

def floor_11():
    canteen = False
    while canteen == False:
        print(Fore.BLUE +"\nWhere are you going next?\n")
        floor_11_map()
        direction = input()
        if direction.upper() == "CANTEEN":
         canteen_area()
        else:
            print(Fore.BLUE +"\n So you made a bold decision to investigate further you dare devil!")
            investigate()
        
def floor_13(count_key):

    elevetor_open = True
    while elevetor_open == True:
        print(Fore.BLUE +"\nYou can see a single door in front of you?\n You hear Lindsey behind the door asking for help")
        if count_key==1:
            elevetor_open == False
            print(Fore.BLUE +"Lindsey is pleased to see her favourite FL member and her favourite pet Raya")
            print(Fore.BLUE +"\nFinally the quest to find Lindsey is over!!\n")
        else:
            elevetor_open= False
            print(Fore.BLUE +"Sorry you made the wrong choice of tool")
            engine.say("Noooooooooooo")
            engine.runAndWait()
            print (Fore.GREEN+"\n *****************************\n")
            print (Fore.GREEN +"GAME OVER - YOUR FAILED AND RESULTED IN THE DOWNFALL OF KPMG")
            playsound('Gameover.mp3')

        


def kitchen_area():
    count_treat = 0
    in_kitchen = True
    print(Fore.BLUE +"\nYou make your way over to the kitchen area\n")
    print(Fore.BLUE +"\nThe kitchen area is no longer filled with the sweet smell of freshly cooked food and the laughter of content employees.\nInstead spilt tomato soup is splattered over the floor and the lights flicker on and off.\nA chill races down your spine as you realise that only someone who is truly afraid would so carelessly spill their tomato soup.\nCautioulsy, you scan your surroundings.\nInvestigate further? (yes/no)\n ")
    kitchen = input()
    choice = True
    while choice == True:
        if kitchen.upper() == "YES":
            choice = False
            print(Fore.BLUE +"\nYour investigation of the kitchen is successful!\nYou find a box of dog treats and decide to put some in your pocket for a snack later.\nNo one is around to shame you for your addiction to nutritous dog treats - you love how they make your hair thick and shiny.\n")
            count_treat += 1
            print(Fore.BLUE +"\nYou decide further investigation of the kitchen would be fruitless\nWhere to next?\n")
            while in_kitchen == True and count_treat == 1:
                next_move = input()
                print(next_move)
                if next_move.upper() == "CHECK MAP":
                    in_kitchen = False
                    floor_10_map()
                elif next_move.upper() == "KITCHEN AREA":
                    print(Fore.BLUE +"\nYou're already in the kitchen area\n")
                    print(Fore.BLUE +"\nWhere do you want to go next?\n")
                    next_move = input()
                elif next_move.upper() == "MEETING ROOM":
                    in_kitchen = False
                    meeting_room(count_treat, count_dog)
                elif next_move.upper() == "ELEVATORS":
                    in_kitchen = False
                    print("\nYou had over to the elevators\n")
                    floor_10()
                else:
                    print("\nWhere do you want to go next?\n")
                    playsound('door.wav')
                    next_move = input()
        elif kitchen.upper() == "NO":
                    print(Fore.BLUE +"\nYou decide not to investigate. The spilled tomato soup is a dangerous slip hazard so you helpfully put down a sign to prevent any workplace accidents.\n")
                    print(Fore.BLUE +"\nWhere to next?\n")
                    next_move = input()
                    no_investigate = True
                    while no_investigate == True:
                        if next_move.upper() == "KITCHEN AREA":
                            print(Fore.BLUE +"\nYou are already in the kitchen area\n")
                            print(Fore.BLUE +"\nWhere to next?\n")
                            next_move = input()
                        elif next_move.upper() == "MEETING ROOM":
                            meeting_room(count_dog, count_treat)
                            no_investigate = False
                        elif next_move.upper() == "ELEVATORS":
                            floor_10(count_dog, count_treat)
                            no_investigate = False
                        else:
                            print(Fore.BLUE +"\nI didn't quite get that.\n")
                            print(Fore.BLUE +"\nWhere to next?\n")
                            next_move = input()
        else:
            print()

def meeting_room(count_treat, count_dog):
    print("\nYou make your way over to the meeting room\n")
    in_meeting_room = True
    while in_meeting_room == True and count_treat == 0:
            print(Fore.BLUE +"\nAs you approach you the door to the meeting room you find a dog collar on the floor and you hear barking coming from the room.\nAs you enter room the noise gets quieter.\nIf only you had something to entice the dog to come to you...")
            print("\nWhere do you want to go next?")
            meeting_room_move = input()
            if meeting_room_move.upper() == "CHECK MAP":
                floor_10_map()
                in_meeting_room = False
            elif meeting_room_move.upper() == "KITCHEN AREA":
                kitchen_area()
                #in_meeting_room = False
            elif meeting_room_move.upper() == "MEETING ROOM":
                print("\nYou are already in the meeting room\n")
                print(Fore.BLUE +"Where are you going next?\n")
            elif meeting_room_move.upper() == "ELEVATORS":
                floor_10(count_dog,count_treat)            
            else:
                print("\nPick a place to go next\n")
    while in_meeting_room == True and count_treat == 1:
        print(Fore.BLUE +"\nAs you approach the meeting room snacking on your delicious dog treats, a dog runs up to you and sits politely at your feet.\nLicking its lips clearly interested in the bitesize goodies you picked up in the kitchen.")
        count_dog += 1

        print("\nYou decide to take the dog with you.\nYou delicately pick it up and place it caringly in your KPMG backup.\nResolute you have everything from this floor you head over to the elevators\n")
        playsound('Dog.wav')
        time.sleep(5)
        floor_11()

def investigate():
    count_key=0
    choice = False
    print("\nYou find a couple of miscellaneous things on the table\n")
    print("\n 1.Screw Driver\n2.Key\n3.Thor's Hammer\n4.Axe")
    option= input()
    if option.upper()=="KEY":
        count_key+=1
        floor_13(count_key)
    else:
        print("Ok good choice. Let's continue a quest to find Lindsey")
        floor_13(count_key)


    

def canteen_area():
    count_crisp=0
    print("\nYou make your way over to the canteen area\n")
    print("\nYou are very hungry and despite having no money,you pick up the delicious crisp over there\n")
    count_crisp += 1
    print("\n Time is ticking and our FL leader is still not visible\n Do you want to go to the next floor  or investgate other room?\n(NEXT FLOOR/INVESTIGATE)\n")
    canteen=input()
    choice = True
    while choice == True:
        if canteen.upper() == "NEXT FLOOR":
            choice = False
            floor_13(count_key)
            break
        else:
            canteen.upper() == "INVESTIGATE"
            choice = False 
            investigate()

def floor_13(count_key):
    item = False
    while item == False:
        if count_key == 0:
            print(Fore.LIGHTRED_EX+"\nYou selected the wrong item! You cannot continue without the key. You have failed in your quest to find Lindsey, your actions have resulted in the downfall of KPMG\n")
            playsound('Gameover.mp3')
            exit()
        else:
            item = True
            floor_13_map()
            engine.say("Yessssssssssssssssss")
            engine.runAndWait()
            print(Fore.GREEN+"\nYou have found the key to free Lindsey! If you act quickly you may be eligible for a promotion\n")
            print("\n")
            playsound('Win.mp3')
            exit()


start()