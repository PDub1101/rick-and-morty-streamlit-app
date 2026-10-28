import streamlit as st
import requests

def header_section():
  st.title('Rick and Morty API Data')

def get_character_data(name):
  response = requests.get(f"https://rickandmortyapi.com/api/character/?name={name}")
  if response.status_code == 200:
    data = response.json()
    return data['results'] if data['results'] else None
  return None

header_section()

def main():
  st.header("Character Information")
  character_name = st.text_input("Enter a Rick and Morty character name:", "Rick Sanchez")
  if character_name:
    characters = get_character_data(character_name)
    if characters:
      if len(characters) > 1:
        selected_char = st.selectbox("Multiple characters found. Slect one:", [char['name'] for char in characters])
        character = next(char for char in characters if char['name'] == selected_char)
      else:
        character = characters[0]
      st.image(character['image'], caption=character['name'], width=300)
      info_options = {
          "Status": character['status'],
          "Species": character['species'],
          "Type": character['type'] if character['type'] else "N/A",
          "Gender": character['gender'],
          "Origin": character['origin']['name'],
          "Episodes": f"Appears in {len(character['episode'])} episodes"
      }
      selected_info = st.selectbox("Select information to display:", list(info_options.keys()))
      st.write(info_options[selected_info])
    else:
      st.error("Character not found. Please try another name.")
main()

st.markdown("---")

def get_all_locations():
        locations = set()
        page = 1
        while True:
            response = requests.get(f"https://rickandmortyapi.com/api/location?page={page}")
            if response.status_code != 200:
                break
            data = response.json()
            for location in data['results']:
                locations.add(location['name'])
            if not data['info']['next']:
                break
            page += 1
        return sorted(locations)

def get_location_population(location_name):
        response = requests.get(f"https://rickandmortyapi.com/api/location/?name={location_name}")
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                return len(data['results'][0]['residents'])
        return 0

def location_comparison():
  st.header("Location Population Comparison")
  locations = get_all_locations()
  col1, col2 = st.columns(2)
  with col1:
    location_1 = st.selectbox("Select location 1:", locations, index=0)
  with col2:
    location_2 = st.selectbox("Select location 2:", locations, index=1)
  if st.button("Compare Populations"):
    with st.spinner("Counting Characters..."):
      population_1 = get_location_population(location_1)
      population_2 = get_location_population(location_2)
      chart_data = {"Locations": [location_1, location_2], "Character Count": [population_1, population_2]}
      st.bar_chart(data=chart_data, x="Locations", y="Character Count", height=400, use_container_width=True)
      st.write(f"**{location_1}**: {population_1} characters")
      st.write(f"**{location_2}**: {population_2} characters")
      if population_1 > population_2:
        st.success(f"{location_1} has more characters than {location_2}")
      elif population_2 > population_1:
        st.success(f"{location_2} has more characters than {location_1}")
      else:
        st.info("Both locations have the same number of characters")
location_comparison()

st.markdown("---")


  
  




      
        
