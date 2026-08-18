import json

bugs = []
priorities = ["Low", "Medium", "High"]

def add_bug():
       
       print("Dodawanie błędu")
       bug_id = len(bugs) + 1
       bug_title = input("Podaj tytul błędu: ")

       while True:
              print("\nWybierz priorytet błędu")

              for i, priority in enumerate(priorities, start = 1):
                print(f"{i}. ", priority)

              try:
                     wybor = int(input())

                     if wybor < 1 or wybor > len(priorities):
                            print("Niepoprawny priorytet, spróbuj ponownie")

                     else:
                            bug_description = input("Podaj opis błędu: ")
                            bugs.append({"tytul": bug_title,
                                          "priorytet": priorities[wybor-1], 
                                          "opis": bug_description,
                                          "ID": bug_id
                                          })

                            save_bugs()
                            break

              except ValueError:
                     print("Niepoprawny priorytet, spróbuj ponownie")

def view_bugs():
      
      if not bugs:
            print("Brak nowo zgłoszonych błędów. ")

      else:
            print("Wyświetlanie błędów...")
            for i, bug in enumerate(bugs, start = 1):
                        #print(f"\nBUG #{i}")
                        #print(f"\nBUG #{bug['ID']}")
                        print(f"\nTytuł: {bug['tytul']}")
                        print(f"\nPriorytet: {bug['priorytet']}")
                        print(f"\nOpis: {bug['opis']}")

            #print(bugs)

def save_bugs():
             
       if not bugs:
              print("Brak nowych bugów do zapisania")

       else:
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

bugs = load_bugs()

while True:

    
 
    print("\n=== Bug Tracker ===\n\n" \
    "1. Dodaj błąd\n" \
    "2. Pokaż błędy\n" \
    "3. Wyjdź\n" \
    "\n"
    "Wybierz opcję: ")

    opcja = input()    

    if opcja == "1":
           add_bug()

    elif opcja == "2":
            view_bugs()

    elif opcja == "3":
            print("Wyjście z programu...")
            break  

    else: 
            print("Nieprawidłowa opcja. Spróbuj ponownie.") 