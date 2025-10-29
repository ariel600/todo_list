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

def delete_task(tasks: list, index: int) -> bool:
    if tasks.pop(index -1):
        return True
    return False

def edit_task(tasks: list, index: int, new_task: str) -> bool:
    if index > len(tasks):
        return False
    show_all_tasks(tasks)
    tasks[index - 1] = new_task
    return True