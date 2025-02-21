while True:
    user_input=input("Enter action to do like - add, complete, show, edit, exit : ")

    match user_input.strip():
        case 'add':
            file=open("../todo_app/members.txt", "r")
            todos=file.readlines()
            file.close()
            member = input("Enter name to add : ") + "\n"
            todos.append(member)
            file = open("../todo_app/members.txt", "w")
            file.writelines(todos)
            file.close()
        case 'exit':
            break;