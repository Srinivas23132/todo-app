todos=[]
while True:
    user_input=input("Enter action to do like - add, complete, show, edit, exit : ")

    match user_input.strip():
        case 'add':
            todo = input("Enter a todo : ")+"\n"
            with open("todo.txt","r") as file:
                todos = file.readlines()
            todos.append(todo)
            with open("todo.txt","w") as file:
                file.writelines(todos)
        case 'complete':
            with open("todo.txt","r") as file:
                todos = file.readlines()
            for i, todo in enumerate(todos):
                todo=todo.strip("\n")
                print(f"{i + 1}. {todo}")
            print("\n" * 2)
            number = int(input("Enter Index of ToDo to remove : "))
            if number <= len(todos):
                del todos[number - 1]
                file=open("todo.txt","w")
                file.writelines(todos)
                print("Deleting Sucessfull........")
            else:
                print("No Element at index or add values")
        case 'show' | 'display':
            with open("todo.txt", "r") as file:
                todos = file.readlines()
            for i, todo in enumerate(todos):
                todo = todo.strip("\n")
                print(f"{i + 1}. {todo}")
            print()
        case 'edit':
            with open("todo.txt", "r") as file:
                todos = file.readlines()
            for i, todo in enumerate(todos):
                todo = todo.strip("\n")
                print(f"{i+1}. {todo}")
            print()
            number=int(input("Enter Index of ToDo to edit : "))
            if number<=len(todos) :
                edit_value = input(f"Enter value to replace {todos[number - 1]} : ")
                todos[number - 1] = edit_value+"\n"
                with open("todo.txt", "w") as file:
                    file.writelines(todos)
                print("Editing Sucessfull........")
            else:
                print("No Element at index or add values")

        case 'exit':
            break
        case _:
            print("Enter a valid command")
print("BYE !")
