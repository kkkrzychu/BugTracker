bugs = []
priority = ["Low", "Medium", "High"]

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
            bug_priority = input(f"\nWybierz priorytet błędu: "\
                                 f"\n1. {priority[0]}"\
                                 f"\n2. {priority[1]}"\
                                 f"\n3. {priority[2]}")
            bug_description = input("Podaj opis błędu: ")
            bugs.append({"tytul": bug_title, "priorytet": bug_priority, "opis": bug_description})

        

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
            # Tutaj można dodać kod do zakończenia programu    

    else: 
            print("Nieprawidłowa opcja. Spróbuj ponownie.") 