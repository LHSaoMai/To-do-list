from MainProject.functions import get_todos, write_todos
import time
now = time.strftime("%b, %d - %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit or complete: ")
    user_action = user_action.strip() #if nothing in the strip we delete the space

    if user_action.startswith('add'):
        todo=user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n') #to append our to :)

        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        #new_todos=[]
        #for item in todos:
         #   new_item = item.strip('\n')
          #  new_todos.append(new_item)

        for index, item in enumerate(todos): #otherwise it will be in a list
            item = item.strip('\n')
            print(f"{index+1} -{item}")

    elif user_action.startswith('edit'):
       try:
            number = int(user_action[5:])
            number = number-1

            todos = get_todos()
            print('Here is the todos existing', todos)

            new_todo=input('Change what you want') + '\n'
            todos[number] = new_todo

            print('Here is jow it will be', todos)

            write_todos(todos)

       except ValueError:
           print("Your command is not valid")
           continue


        #change=input('what is the new value ? ')
        #todos.__setitem__(number,change)
    elif user_action.startswith('complete'):
        try:
            nbr_complete = int(user_action[9:])-1

            todos = get_todos()

            todo_to_removed = todos[nbr_complete].strip('\n')
            todos.pop(nbr_complete)

            write_todos(todos)


            message = f"Todo {todo_to_removed} was removed from the list"
            print(message)
        except ValueError:
            print("Not valid index")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("The command is not valid")