from bug_tracker import add_bug, view_bugs, delete_bug, update_bug

while True:          
 
    print("\n=== Bug Tracker ===\n\n" \
    "1. Dodaj błąd\n" \
    "2. Pokaż błędy\n" \
    "3. Usuń błąd\n" \
    "4. Edytuj błąd\n" \
    "5. Wyjdź\n" \
    "\n"
    "Wybierz opcję: ")

    opcja = input()    

    if opcja == "1":
           add_bug()

    elif opcja == "2":
            view_bugs()

    elif opcja == "3":
           delete_bug()

    elif opcja == "4":
           update_bug()

    elif opcja == "5":
            print("Wyjście z programu...")
            break  

    else: 
            print("Nieprawidłowa opcja. Spróbuj ponownie.") 