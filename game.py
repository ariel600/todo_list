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

def delete_task(tasks: list, index: int):
    if index > len(tasks):
        print("המשימה לא נמצאת.")
        return
    if tasks.pop(index - 1):
        print("המשימה נמחקה.")
        return
    print("לא מצאנו את המשימה שברצונך למחוק.")
    return

def edit_task(tasks: list, index: int, new_task: str):
    if index > len(tasks):
        print("לא ניתן לערוך את המשימה, המשימה לא נמצאה.")
        return
    show_all_tasks(tasks)
    tasks[index - 1] = new_task
    print("המשימה שונתה בהצלחה.")
    return