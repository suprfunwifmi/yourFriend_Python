import time
import Friend
import YourFriend
import YourFriendFileManager
import ListOfCommands

friend = Friend.Friend()
yourFriend = YourFriend.YourFriend()
yourFriendFileManager = YourFriendFileManager.YourFriendFileManager()
listOfCommands = ListOfCommands.ListOfCommands()

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
    createYourFriendDirectory = ""

    firstName = friend.askFirstName(raw_input("What is your first name? "))
    surName = friend.askLastName(raw_input("What is your last name? "))
    print("Hi " + friend.firstName +" "+ friend.surName)
    print("")
    yourFriendName = yourFriend.GiveMeAName(raw_input("What is my name? "))
    print("so let's start again " + friend.firstName)
    # createYourFriendDirectory = yourFriendFileManager.CreateYourFriendDirectory(raw_input("Type in a path where would you like to save the data(can start with a C:\)? "))
    # yourFriendFileManager.CreateFriendJson(friend.firstName, friend.surName)
    print("Hi I am " + yourFriend.Name)

def listAllCommands():
    listOfCommands.listTheCommands()



Copyright()
firstInteraction()
listAllCommands()
