#!/usr/bin/python3
import requests
import json
from easygui import *

class Simple:
    def __init__(self):
        self.url = "http://worldtimeapi.org/api/timezone/America/Sao_Paulo"
        self.r   = requests.get(self.url)
    
    def hours(self):
        try:
            if (self.r.status_code == 200):
                resp = json.loads(self.r.text)
    
                datetime = resp['datetime']
                splitFormat = datetime.split("T", 1)
                time = splitFormat[1].split(".", 1)

                print(time[0])
                
                tanks_message = '''
                    {}

                    Tank You for usage my program the of Timetible.
                    Ass: Anonymous
                '''.format(time[0])

                msgbox(tanks_message, "Timetable of the Brasilian")

            else:
                print("Server {} not found".format(self.url))

        except Exception as err:
            print(err)

if __name__ == "__main__":
    Simple = Simple()
    Simple.hours()
