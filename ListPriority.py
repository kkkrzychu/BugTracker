priorities = ["Low", "Medium", "High"]

while True:

    try:
        wybor = int(input("Podaj numer: "))
        if wybor not in [1,2,3]:
                print("niepoprawny priorytet, jeszcze raz")
        
        else:
            print(priorities[wybor-1])
            break
    except ValueError:
        print("niepoprawny priorytet, jeszcze raz")