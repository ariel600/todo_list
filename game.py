def add_task(tasks: list, task: str) -> None:
    tasks.append(task)
    pass

def show_all_tasks(tasks: list) -> None:
    if len(tasks) == 0:
        print("עדיין לא הוספת משימה.")
    else:
        index = 0
        for task in tasks:
            index += 1
            print(f"{index}. {task}")
    pass

def get_user_choice() -> str:
    choice = input(
    """
    1. הוספת משימה
    2. הצגת המשימות
    3. מחיקת משימה
    4. עריכת משימה
    5. יציאה
    בחר את האפשרות הרצויה: """
    )
    return choice
