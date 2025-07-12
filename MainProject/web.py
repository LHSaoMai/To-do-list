import streamlit as st # streamlit library to create webapp and can also create data dashboard
import functions

todos = functions.get_todos()
def add_todo():
    todo =st.session_state['new_todo'] + '\n' #key our text input widget
    # session_state is a sort of dictionary (it is a session text type not really a dictionarry
    # and this coontain pair of data of the user - and the dictionnary is update
    todos.append(todo )
    functions.write_todos(todos)
    #when the user click on enter and the function is call


st.title("My Todo App")
st.subheader("This is my todo app")
st.write('This app is to increase your productivity')

st.checkbox('Buy grocery')
st.checkbox('Throw the trash')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Add a new todo...', on_change = add_todo, key='new_todo') #label is a require argument and it will write something
#on_change = and it's a call back function and also create a custum function
#on change function : and it's a call back on the function : add_todo

st.session_state