tasks = []
next_id = 1


def add_task(text):
    global next_id
    tasks.append({"id": next_id, "text": text, "done": False})
    print(f"Sarcina #{next_id} a fost adăugată.")
    next_id += 1


def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            print(f"Sarcina #{task_id} a fost marcată ca rezolvată.")
            return
    print(f"Eroare: sarcina #{task_id} nu există.")


def delete_task(task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            print(f"Sarcina #{task_id} a fost ștearsă.")
            return
    print(f"Eroare: sarcina #{task_id} nu există.")


def list_tasks():
    if not tasks:
        print("Lista de sarcini este goală.")
        return
    print("Sarcini:")
    for task in tasks:
        status = "[x]" if task["done"] else "[ ]"
        print(f"  {task['id']}. {status} {task['text']}")


def main():
    print("Aplicație TODO List")
    print("Comenzi: add <text>, done <id>, delete <id>, list, exit")
    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            print()
            break
        if not line:
            continue
        parts = line.split(maxsplit=1)
        command = parts[0].lower()
        if command == "exit":
            print("La revedere!")
            break
        elif command == "add":
            if len(parts) < 2:
                print("Eroare: lipsește textul sarcinii. Folosește: add <text>")
            else:
                add_task(parts[1])
        elif command == "done":
            if len(parts) < 2:
                print("Eroare: lipsește ID-ul. Folosește: done <id>")
            else:
                try:
                    task_id = int(parts[1])
                except ValueError:
                    print("Eroare: ID-ul trebuie să fie un număr.")
                    continue
                mark_done(task_id)
        elif command == "delete":
            if len(parts) < 2:
                print("Eroare: lipsește ID-ul. Folosește: delete <id>")
            else:
                try:
                    task_id = int(parts[1])
                except ValueError:
                    print("Eroare: ID-ul trebuie să fie un număr.")
                    continue
                delete_task(task_id)
        elif command == "list":
            list_tasks()
        else:
            print(f"Comandă necunoscută: {command}")


if __name__ == "__main__":
    main()
