
todos = []

while True:
    user_action = input("Type add or show or edit")

    match user_action:
        case 'add':
            todo = input("Enter a to do ")
            todos.append(todo)
        case 'show':
            for items in todos:
                print(items)
        case 'edit':
            number = input("Number of the todo edit: ")
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case 'exit':
            break

print("bye")


