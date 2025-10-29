import game

todo_list = []

def main() -> None:
    while True:
        coice = game.get_user_choice()
        if coice == "1": 
            task = input("מה המשימה שתרצה להוסיף? ")
            game.add_task(todo_list, task)
            print("המשימה התווספה לרשימת המשימות.")
        elif coice == "2":
            game.show_all_tasks(todo_list)
        elif coice == "3":
            print("אנחנו עובדים על זה.")
        elif coice == "4":
            print("אנחנו עובדים על זה.")
        elif coice == "5":
            break
        else:
            print("לא הצלחנו לזהות את הבקשה.")
            
        
if __name__ == "__main__":
    main()