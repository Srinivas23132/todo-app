todos=[]
while True:
    user_input=input("Enter action to do like - add, complete, show, edit, exit : ")
    user_input=user_input.strip()
    if user_input.startswith("add"):
        todo = user_input[4:]+"\n"
        with open("todo.txt","r") as file:
            todos = file.readlines()
        if todo=="\n" or " \n":
            todos.append(todo)
        with open("todo.txt","w") as file:
            file.writelines(todos)
        log = ""
        with open("log.txt", "r") as file:
            log = file.read()
        with open("log.txt","w") as file:
            file.write(log+f"Added new Todo {todo}\n")


    elif user_input.startswith('complete'):

        try:

            with open("todo.txt", "r") as file:

                todos = file.readlines()

            if not todos:
                raise IndexError("The to-do list is empty. Nothing to delete.")

            # Extract the number and validate

            user_number = user_input[9:].strip()

            if not user_number.isdigit():
                raise ValueError("Invalid input. Please enter a valid task number.")

            number = int(user_number)

            if number <= 0 or number > len(todos):
                raise IndexError(f"Invalid task number: {number}. It must be between 1 and {len(todos)}.")

            del_ele = todos.pop(number - 1)

            with open("todo.txt", "w") as file:

                file.writelines(todos)

            log = ""

            with open("log.txt", "r") as file:

                log = file.read()

            print(f"Deleting Successful... Element '{del_ele.strip()}' deleted.")

            with open("log.txt", "w") as file:

                file.write(log + f"Deleting Successful... Element '{del_ele.strip()}' deleted\n")


        except ValueError as value_error:

            print(f"Error: {value_error}")

            with open("log.txt", "a") as file:

                file.write(f"Error: {value_error}\n")
            continue


        except IndexError as index_error:

            print(f"Error: {index_error}")

            with open("log.txt", "a") as file:

                file.write(f"Error: {index_error}\n")
            continue


    elif user_input.startswith('show'):
        with open("todo.txt", "r") as file:
            todos = file.readlines()
        for i, todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{i + 1}. {todo}")
        print()


    elif user_input.startswith('edit'):
        try:
            with open("todo.txt", "r") as file:
                todos = file.readlines()

            if not todos:
                raise IndexError("The to-do list is empty. Nothing to edit.")

            # Extract the number and validate
            user_number = user_input[5:].strip()
            if not user_number.isdigit():
                raise ValueError("Invalid input. Please enter a valid task number.")

            number = int(user_number)

            if number <= 0 or number > len(todos):
                raise IndexError(f"Invalid task number: {number}. It must be between 1 and {len(todos)}.")

            old_value = todos[number - 1].strip()
            edit_value = input(f"Enter value to replace '{old_value}': ").strip()

            if not edit_value:
                raise ValueError("Edited value cannot be empty.")

            todos[number - 1] = edit_value + "\n"

            with open("todo.txt", "w") as file:
                file.writelines(todos)

            print(f"Editing Successful... Edited todo from '{old_value}' to '{edit_value}'.")

            with open("log.txt", "a") as file:
                file.write(f"Editing Successful... Edited todo from '{old_value}' to '{edit_value}'\n")

        except ValueError as value_error:
            print(f"Error: {value_error}")
            with open("log.txt", "a") as file:
                file.write(f"Error: {value_error}\n")

        except IndexError as index_error:
            print(f"Error: {index_error}")
            with open("log.txt", "a") as file:
                file.write(f"Error: {index_error}\n")

    elif user_input.startswith('exit'):
        break
    else:
        log = ""
        with open("log.txt", "r") as file:
            log = file.read()
        print("Enter a valid command")
        with open("log.txt", "w") as file:
            file.write(log+"Enter a valid command\n")
print("BYE !")
