import json

bugs = []
bugs_json = []
bugs_parsed = []
priorities = ["Low", "Medium", "High"]

def add_bug():
       
       print("Dodawanie błędu")
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
                              bugs.append({"tytul": bug_title, "priorytet": priorities[wybor-1], "opis": bug_description})
                              break

              except ValueError:
                     print("Niepoprawny priorytet, spróbuj ponownie")

def view_bugs():
      
      if not bugs:
            print("Brak zgłoszonych błędów. ")

      else:
            print("Wyświetlanie błędów...")
            for i, bug in enumerate(bugs, start = 1):
                        print(f"\nBUG #{i}")
                        print(f"\nTytuł: {bug['tytul']}")
                        print(f"\nPriorytet: {bug['priorytet']}")
                        print(f"\nOpis: {bug['opis']}")

def save_bugs():
             
       if not bugs:
              print("Brak bugów do zapisania")

       else:
              with open("Bugs.txt", "w") as f:
                     bugs_json = json.dumps(bugs)
                     f.write(str(f"{bugs_json}\n"))
                     f.close()

def load_bugs():    
       
       with open("Bugs.txt") as f:
              bugs_json = f.read()
              bugs_parsed = json.loads(bugs_json)
              bugs = bugs_parsed
              print(bugs)

while True:    

    print("\n=== Bug Tracker ===\n\n" \
    "1. Dodaj błąd\n" \
    "2. Pokaż błędy\n" \
    "3. Zapisz błędy\n"
    "4. Wyjdź\n" \
    "\n"
    "Wybierz opcję: ")

    opcja = input()    

    if opcja == "1":
           add_bug()

    elif opcja == "2":
            load_bugs()
            view_bugs()

    elif opcja == "3":
           save_bugs()

    elif opcja == "4":
            print("Wyjście z programu...")
            break  

    else: 
            print("Nieprawidłowa opcja. Spróbuj ponownie.") 