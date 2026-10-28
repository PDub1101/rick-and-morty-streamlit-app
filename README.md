# Rick & Morty AI Assistant & Universe Explorer

An interactive multi-page [Streamlit](https://streamlit.io/) web application combining the **Rick and Morty REST API** with **Google Gemini AI** for character exploration, location comparisons, dynamic backstory generation, and an in-character AI chatbot.

![App Banner](Images/Rick&Morty.jpg)

---

## Features

1. **Character Information & Location Explorer** (`pages/API Data.py`)
   - Search for any character from the Rick and Morty universe via the public REST API.
   - View detailed attributes including status, species, origin, episode counts, and character artwork.
   - Compare resident populations across different locations in the universe with interactive bar charts.

2. **AI Backstory Generator** (`pages/Character_Backgrounds.py`)
   - Leverages Google Gemini to generate imaginative origin stories and character backgrounds.
   - Select between "Rick Sanchez" narration (witty, sarcastic, burping) or a traditional documentary narrator.

3. **In-Character Chat Bot** (`pages/Rick and Morty Chat Bot.py`)
   - Real-time conversational AI tuned with system instructions to respond like an authentic Rick and Morty lore expert.
   - Pre-loads character context and facts directly from the API to ground the conversation.

---

## Tech Stack

- **Framework**: [Streamlit](https://streamlit.io/)
- **LLM / AI**: Google Gemini (`google-generativeai`)
- **API**: [The Rick and Morty API](https://rickandmortyapi.com/)
- **Language**: Python 3.10+

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/rick-and-morty-streamlit-app.git
cd rick-and-morty-streamlit-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your Gemini API Key
Create a `.streamlit/secrets.toml` file (or copy the example file):
```bash
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

Edit `.streamlit/secrets.toml` and provide your Google Gemini API key:
```toml
key = "your_actual_gemini_api_key_here"
```

### 4. Run the app
```bash
streamlit run main.py
```
Open your browser to `http://localhost:8501`.
