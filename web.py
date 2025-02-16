import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your <b>productivity</b>.",  #can use <h1> </h1> inside parenthesis to make big font like title
         unsafe_allow_html=True)

#Could add textbox here without issues

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()                  #Instructor used st.experimental_rerun()

st.text_input(label="Enter a todo:", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')
#streamlit run web.py