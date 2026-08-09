

bugs = []
priorities = ["Low", "Medium", "High"]


def add_bug():
       
       print("Dodawanie błędu")
       bug_title = input("Podaj tytul błędu: ")

       while True:
              print("\nWybierz priorytet błędu")

              for i, priority in enumerate(priorities, start = 1):
                print(f"{i}, ", priority)

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
     '''               
        print("Dodawanie błędu ")
        bug_title = input("Podaj tytul bledu: ")

        while True:                
                
                print("\n Wybierz priorytet błędu:")

                for i, priority in enumerate(priorities, start = 1):                       
                       print (f"{i}. ", priority)

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

'''

    elif opcja == "2":
            if not bugs:
                   print("Brak zgłoszonych błędów.")

            else:
                print("Wyświetlanie błędów...")
                for i, bug in enumerate(bugs, start=1):
                        print(f"\nBUG #{i}")
                        print(f"\nTytuł: {bug['tytul']}")
                        print(f"\nPriorytet: {bug['priorytet']}")
                        print(f"\nOpis: {bug['opis']}")        

    elif opcja == "3":
            print("Wyjście z programu...")
            break  

    else: 
            print("Nieprawidłowa opcja. Spróbuj ponownie.") 