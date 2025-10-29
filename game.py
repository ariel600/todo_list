todo_list = ["בננה", "אבטיח"]

def add_task(tasks: list, task: str) -> None:
    tasks.append(task)
    pass

def show_all_tasks(tasks: list) -> None:
    if len(tasks) == 0:
        print("You don't have any tasks yet.")
    else:
        index = 0
        for task in tasks:
            index += 1
            print(f"""{index}. task""")
    pass

def get_user_choice() -> str:
    pass

def main() -> None:
    pass

print(show_all_tasks(todo_list))