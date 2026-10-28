import streamlit as st
import requests
import google.generativeai as genai
import os

key = st.secrets["key"]
st.title("Rick and Morty Character Analysis with Gemini")
st.write("""Have Rick Sanchez descibe the backstory of your selected character!""")

genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash")

def get_character_data(name):
  url = f"https://rickandmortyapi.com/api/character/?name={name}"
  response = requests.get(url).json()
  if "results" in response:
    return response["results"][0]
  return None

character_name = st.text_input("Enter a Rick and Morty character name: ", "Rick Sanchez")

narration_style = st.selectbox("Select narration style:", ("Rick Sanchez", "Regular Narrator"))

if st.button("Generate Backstory"):
  char_data = get_character_data(character_name)
  if char_data:
    try:
      first_ep_url = char_data["episode"][0]
      ep_response = requests.get(first_ep_url).json()
      first_ep_name = ep_response["name"]
    except:
      first_ep_name = "an unknown episode"
    if narration_style == "Rick Sanchez":
      narration_instruction = "Make it sound like a Rick Sanchez is descibing this characetrs background, make it funny, weird, and fitting to the Rick and Morty universe."
    else:
      narration_instruction = "Write a detailed and factual backstory for this character in a neutral narrator tone."
    prompt = f"""
      Write a detailed and imaginative background story for this Rick and Morty character: 
      Name: {char_data['name']}
      Species: {char_data['species']}
      Gender: {char_data['gender']}
      Status: {char_data['status']}
      Origin: {char_data['origin']['name']}
      First appeared in: {first_ep_name}
      Episodes appeared in: {len(char_data['episode'])}
      {narration_instruction}
    """
    try:
      response = model.generate_content(prompt)
      st.subheader("Generated Backstory")
      st.write(response.text)
    except Exception as e:
      st.error(f"Failed to generate backstory: {e}")

  else:
    st.warning("Character not found. Try a different name!")




