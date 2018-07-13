class ListOfCommands(object):
    """docstring for ."""
    def __init__(self):
        self.changeMyName = "change my name"
        self.changeDirectory = "change directory"
        self.allCommands = ["change my name","change directory"]

    def listTheCommands(self):
        print("Here are all possible commands: ")
        for command in self.allCommands:
            print(command)
