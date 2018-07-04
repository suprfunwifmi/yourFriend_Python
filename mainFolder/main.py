import time
import Friend
import YourFriend

friend = Friend.Friend()
yourFriend = YourFriend.YourFriend()
def Copyright():
    copyright = [
        "========================================================================================================",
        "                                     YourFriend                                                         ",
        "                                         by                                                             ",
        "                                     Jason Millsom                                                      ",
        "                               @Copyright Jason Millsom                                                 ",
        "========================================================================================================"
    ]
    for x in copyright:
        time.sleep(0.25)
        print(x)

def firstInteraction():
    firstName = ""
    surName = ""
    yourFriendName = ""


    firstName = friend.askFirstName(raw_input("What is your first name? "))
    surName = friend.askLastName(raw_input("What is your last name? "))
    print("Hi " + friend.firstName +" "+ friend.surName)
    print("")
    yourFriendName = yourFriend.GiveMeAName(raw_input("What is my name? "))
    print("so let's start again " + friend.firstName)
    print("Hi I am " + yourFriend.Name)



Copyright()
firstInteraction()
