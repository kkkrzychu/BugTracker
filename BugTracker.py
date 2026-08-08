bugs = []
priorities = ["Low", "Medium", "High"]

while True:

    print("\n=== Bug Tracker ===\n\n" \
    "1. Dodaj błąd\n" \
    "2. Pokaż błędy\n" \
    "3. Wyjdź\n" \
    "\n"
    "Wybierz opcję: ")

    opcja = input()    

    if opcja == "1":
            
        print("Dodawanie błędu ")
        bug_title = input("Podaj tytul bledu: ")



        while True:                
                i = 1
                print("\n Wybierz priorytet błędu:")
                '''
                bug_priority = input(f"\nWybierz priorytet błędu: "\
                        f"\n1. {priorities[0]}"\
                        f"\n2. {priorities[1]}"\
                        f"\n3. {priorities[2]}")
                '''

                for priority in priorities:                       
                       print (f"{i}. ", priority)
                       i = i + 1

                try:
                        wybor = int(input())

                        '''
                        if bug_priority not in priorities: 
                                print("Niepoprawny priorytet")  
                        '''
                        if wybor not in [1,2,3]:
                               print("Niepoprawny priorytet, spróbuj ponownie")

                        else:                
                                
                                bug_description = input("Podaj opis błędu: ")
                                bugs.append({"tytul": bug_title, "priorytet": priorities[wybor-1], "opis": bug_description})
                                break

                except ValueError:
                       print("Niepoprawny priorytet, spróbuj ponownie")

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