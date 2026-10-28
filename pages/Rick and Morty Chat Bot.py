import streamlit as st
import requests
import google.generativeai as genai

key = st.secrets["key"]
genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=("You answer like a Rick and Morty expert: be funny, sarcastic, and concise. add Rick's signature burp throughout the backstory, be a little rude as well"))

def get_character(name: str):
  resp = requests.get("https://rickandmortyapi.com/api/character/", params={"name": name})
  data = resp.json()
  return data.get("results", [None])[0] if resp.status_code == 200 else None

if "history" not in st.session_state:
  st.session_state.history = []
history = st.session_state.history

st.title("Rick and Morty Expert Chat!")


name_to_load = st.text_input("Character name: ", "Rick Sanchez")
if st.button("Load facts"):
  char = get_character(name_to_load)
  if char:
    facts = (
      f"Name: {char['name']}, Species: {char['species']}, "
      f"Status: {char['status']}, Origin: {char['origin']['name']}, "
      f"Episodes: {len(char['episode'])}"
    )
    history.append({"role": "user", "parts": [f"Character facts:\n{facts}"]})
    st.success(f"Loaded {char['name']}!")
  else:
    st.warning("Character not found.")

msg = st.chat_input("Ask me any Rick and Morty question!")
if msg:
  history.append({"role": "user", "parts": [msg]})
  try:
    reply = model.generate_content(history).text
  except Exception as e:
    reply = f"Gemini error: {e}"
  history.append({"role": "model", "parts": [reply]})

for entry in history[1:]:
  who = "user" if entry["role"] == "user" else "assistant"
  st.chat_message(who).write(entry["parts"][0])



