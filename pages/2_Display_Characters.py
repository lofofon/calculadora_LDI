from pages.dependencias.utils import get_all_characters, remove_character
import streamlit as st

# Add custom CSS for styling
st.markdown("""
    <style>
    .character-box {
        border: 1px solid #ddd;
        padding: 10px;
        margin: 10px 0;
        border-radius: 5px;
    }
    .character-box.selected {
        border-color: green;
    }
    .character-header {
        font-size: 20px;
        font-weight: bold;
    }
    .character-value {
        font-size: 16px;
        margin: 5px 0;
        padding: 5px;
        border: 1px solid #ddd;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for selected characters if it doesn't exist
if "selected_characters" not in st.session_state:
    st.session_state["selected_characters"] = []

# Function to toggle character selection
def toggle_character_selection(char_id):
    if char_id in st.session_state["selected_characters"]:
        st.session_state["selected_characters"].remove(char_id)
    else:
        st.session_state["selected_characters"].append(char_id)

# Retrieve and display all characters from the database
st.write("Personagens no banco de dados:")
characters = get_all_characters()
for char in characters:
    char_id, char_name, race_multiplier, qi_control, pph_base = char
    selected_char = {char_id:{'char_name':char_name, 'pph_base':pph_base}}
    is_selected = selected_char in st.session_state["selected_characters"]
    selected_class = "selected" if is_selected else ""

    with st.container():
        st.markdown(f"""
            <div class="character-box {selected_class}">
                <div class="character-header">{char_name}</div>
                <div class="character-value">Multiplicador Racial: {race_multiplier:.2f}</div>
                <div class="character-value">Controle de Qi: {qi_control:.2f}</div>
                <div class="character-value">PPH BASE: {pph_base:.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        col1, col2 = st.columns([1, 1])

        with col1:
            selected = st.checkbox("Selecionar", value=is_selected, key=f"select_{char_id}")
            if selected and not is_selected:
                st.session_state["selected_characters"].append(selected_char)
                st.rerun()
            elif not selected and is_selected:
                st.session_state["selected_characters"].remove(selected_char)
                st.rerun()
        with col2:
            if st.button("Remover", key=f"remove_{char_id}"):
                remove_character(char_id)
                st.rerun()  # Rerun the script to refresh the page and show updated character list

# Display a button to clear the list of selected characters
if st.button("Clear Selected Characters"):
    st.session_state["selected_characters"] = []
    st.rerun()
