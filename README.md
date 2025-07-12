# To-Do App (GUI + Web)

A simple, beginner-friendly To-Do list application built using Python. This project features both a **desktop GUI** built with PySimpleGUI and a **web interface** using Streamlit. It's a great example of integrating file operations, UI libraries, and Python best practices into one cohesive productivity tool.  
(Done in 2023)

## 🚀 Features

- Add, edit, and complete to-do items
- Desktop GUI using **PySimpleGUI**
- Web version built with **Streamlit**
- Real-time clock in the GUI
- To-do list saved to a local text file (`todos.txt`)

## To run the desktop version:

<pre> ```bash python gui.py ``` </pre>

GUI Features:
* Input field to add new items
* Select and edit existing items
* Mark tasks as complete
* Live clock display

## Web App (Streamlit)
To launch the web version:

<pre> ``` bash streamlit run web.py ``` </pre>

Web Features:
* Minimal interface for quick task entry
* Add todos interactively using session state
* Automatically updates the to-do file

## Requirements
Install dependencies:

<pre> ``` pip install PySimpleGUI streamlit ``` </pre>  

## The goal 
* Practicing file I/O in Python
* Understanding state management in GUIs and web apps
* Building interactive Python apps with visual feedback

