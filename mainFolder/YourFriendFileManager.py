import os
import json

class YourFriendFileManager:

    def __init__(self):
        self.pathValidation = False
        self.path = ""
        self.folder = ""
        self.file = ""

    def CreateFriendJson(self, firstName, surName):
        self.file = "friend.txt"
        self.path = self.folder + self.file
        jsonFile = open("friend.txt", "w")
        data = {}
        data["friend"] = []
        data["friend"].append({
            "firstName": firstName,
            "surName": surName
        })

        with open(jsonFile, "w") as outfile:
            json.dump(data, outfile)



    def CreateYourFriendDirectory(self, path):
        self.pathValidation = False
        while self.pathValidation is False:
            self.folder = "YourFriend"
            if os.path.exists(path):
                if os.path.exists(path + self.folder):
                    self.path = path + self.folder
                    print(self.path + " already exists")
                else:
                    self.path = path + self.folder
                    os.makedirs(self.path)
                    print(self.path + " has been created")
                    print("all files will be created and managed by me")
                    print("")
                    print("If you wish to change anything, just tell me and I'll change it")
                self.pathValidation = True
            else:
                print(path + " this does not exist")
                self.pathValidation = False
