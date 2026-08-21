from storage import save_bugs, load_bugs

bugs = []
priorities = ["Low", "Medium", "High"]

def add_bug(): 
       
       print("Dodawanie błędu")

       bug_title = input("Podaj tytul błędu: ")
       bug_priority = choose_priority()
       bug_description = input(" Podaj opis błędu ")
       bug_id = get_next_ID()

       bugs.append({"tytul": bug_title,
                    "priorytet": bug_priority,
                    "opis": bug_description,
                    "ID": bug_id 
                     })

       save_bugs(bugs)

def view_bugs():
      
      if not bugs:
            print("Brak błędów. ")

      else:
            print("Wyświetlanie błędów...")
            for bug in bugs:
                        print(f"\nBUG #{bug['ID']}")
                        print(f"\nTytuł: {bug['tytul']}")
                        print(f"\nPriorytet: {bug['priorytet']}")
                        print(f"\nOpis: {bug['opis']}")            

def delete_bug():

       found = False
       
       try:
              ID_to_delete = int(input("Podaj ID błędu do usunięcia lub wybierz 0 aby anulować: "))

              if ID_to_delete == 0:
                     return
              else:
                     for bug in bugs:
                            if bug["ID"] == ID_to_delete:
                                   bugs.remove(bug)
                                   save_bugs(bugs)
                                   found = True
                                   break

                     if not found:
                            print(f"Nie znaleziono buga o id {ID_to_delete}")
       
       except ValueError:
              print("Niepoprawny ID błędu")       

def update_bug():

       found = False

       try:
              id_to_update = int(input("Podaj ID buga do edycji lub wybierz 0 aby anulować: "))

              if id_to_update == 0:
                     return

              else:
                     for bug in bugs:
                            if bug["ID"] == id_to_update:
                                   
                                   bug["tytul"] = input("Nowy tytuł: ")
                                   bug["priorytet"] = choose_priority()                                   
                                   bug["opis"] = input("Nowy opis: ")
                                   found = True
                                   save_bugs(bugs)
                                   break

                     if not found:
                            print(f"Nie znaleziono buga o ID {id_to_update}")


       except ValueError:
              print("Niepoprawny ID")

def get_next_ID():

       existing_IDs = []

       for bug in bugs:
              existing_IDs.append(bug["ID"])

       if not existing_IDs:
              return 1

       bug_id = max(existing_IDs) + 1

       return bug_id

def choose_priority():
       while True:
              print("\nWybierz priorytet: ")
       
              for i, priority in enumerate(priorities, start = 1):
                     print(f"{i}. ", priority)
       
              try:
       
                     wybor = int(input())
       
                     if wybor < 1 or wybor > len(priorities):
                            print("Niepoprawny priorytet")                                                 
       
                     else:
                            return priorities[wybor-1]
                                   
                                                        
              except ValueError:
                     print("Niepoprawny priorytet")

bugs = load_bugs()