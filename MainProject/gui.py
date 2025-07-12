import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open('todos.txt','w') as file:
        pass # and does nothing - just want to create it :)


sg.theme("LightBlue4")


# we need to connect them to the window otherwise there are floating
clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo") #key is for the tuple dictionary
add_button = sg.Button("Add") #but we need to connect the button the some action otherwise will just close the program
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size = [45,10]) #the size of our list box
edit_button= sg.Button("Edit")

complete_button = sg.Button("Complete")

close_button = sg.Button("Close")

window = sg.Window("My To-Do App",
                   layout=[[clock],[label], [input_box, add_button], [list_box,edit_button, complete_button],
                           [ close_button]],
                   font=("Helvetica",20)) # My to do app is the Title, label is the label
#of our text, and input_box is what appear when we are in the box

# don't want to close the window so use while loop

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%b -%d, %H:%M:%S'))
    match event:
        case "Add":
            todos = functions.get_todos() #read our todos
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value=" ")
        case "Edit":
            try:
                todos=functions.get_todos() #it's a list
                index=todos.index(values['todos'][0])
                todos[index]=values['todo']
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value=" ")
            except IndexError: #let's create  a pop up window
                sg.popup("Please select an item first", font=("Helvetica",20))
        case "Complete":
            try:
                todos=functions.get_todos()
                index=todos.index(values['todos'][0])
                todos.pop(index)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica",20))

        case "Close":
            break

        case sg.WIN_CLOSED:
            break
window.close()


