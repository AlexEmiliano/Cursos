prompt = "\nType Add, Edit, Exit or Show to do list: "
todos = []

while True:
    opc = input(prompt)
    match opc:
        case "add":
            todo = input("Enter your task: ")
            todos.append(todo)
        case "show":
            for iten in todos:
                print(iten)
        case "break" | "exit":
            break
        case "edit":
            number = (int(input("Number of the todo to list: "))) - 1
            print(todos[number])
            todos[number] = input("Type your task: ")
        case _:
            print("Command not found**")
print("bye")