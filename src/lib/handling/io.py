### RPGOnline
### A Synergy Studios Project

import json

class Database:

    """Saves and retrieves data from a savefile. Holds all the
       data, so another class can pull from it."""

    def __init__(self):

        self.savefile = 'rpgonline-data.json'
        self.backupfile = 'rpgonline-backup.json'

        self.userdata = [] # Username, UserID, 
        self.gamedata = [] # LevelOn,
        self.settings = [] # Game Version

        self.data = {'userdata': self.userdata,
                     'gamedata': self.gamedata,
                     'settings': self.settings,
            }

    def save_to_json(self):

        """Saves the particular file to the json."""

        with open(self.savefile, 'w') as outfile:
            json.dump(self.data, outfile)

    def load_from_json(self):

        """Loads from the file and replaces the data."""

        with open(self.savefile) as jsonfile:
            self.data = json.load(jsonfile)
            
        #self.userdata = self.data[0]
        #self.gamedata = self.data[1]
        #self.settings = self.data[2]

    def clear(self):

        """Clears the database of data."""

        self.userdata = []
        self.gamedata = []
        self.settings = []

        self.data = {'userdata': self.userdata,
                     'gamedata': self.gamedata,
                     'settings': self.settings,
            }

    def refresh_data(self):

        """Refreshes the self.data to what the lists are."""

        self.data = {'userdata': self.userdata,
                     'gamedata': self.gamedata,
                     'settings': self.settings,
            }

    def add_data(self, li, data):

        """Adds data to the database."""

        if li == 'userdata':
            self.userdata = data

        if li == 'gamedata':
            self.gamedata = data

        if li == 'settings':
            self.settings = data

        self.refresh_data()

    def print_data(self):

        """Prints the current data."""

        print(f'Userdata: {self.userdata}')
        print(f'Gamedata: {self.gamedata}')
        print(f'Settings: {self.settings}')



         

