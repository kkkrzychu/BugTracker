import json

def save_bugs(bugs):
              
              with open("Bugs.txt", "w") as f:
                     json.dump(bugs, f)

def load_bugs():
       
       try:      
              with open("Bugs.txt") as f:
                     bugs_json = f.read()
                     bugs_parsed = json.loads(bugs_json)
       except FileNotFoundError: 
                     return []

       return bugs_parsed 
