import streamlit as st

# Title of App
st.title("Web Development Lab03")

# Assignment Data 
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Team 07, Web Development - Section B")
st.subheader("Paul Gibson, Meghan Patel")

st.image("Images/Rick&Morty.jpg", width = 1000)

# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Page Name**: Description
#       2. **Page Name**: Description
#       3. **Page Name**: Description
#       4. **Page Name**: Description

st.write("""
Welcome to our Streamlit Web Development Lab03 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. Main: This page describes the purpose of each page (including this one), broh.
2. API Data: This page depicts data from the Rick and Morty API, you can search your favorite character from the Rick and Morty Universe and find specific actibutes about that character, also there is a section where you can compare the populations between two different locations in the universe, broh
3. Character Background: This page uses Google Gemini to have that bot act like Rick Sanchez while descibing the background of the inputed character, broh
4. Google Gemeni: This page uses Google Gemini to have a conversation with a Rick and Morty expert about any character after pulling their information from the API, broh

""")


