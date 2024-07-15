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

# Retrieve and display all characters from the database
st.write("Personagens no banco de dados:")
characters = get_all_characters()
for char in characters:
    char_id, char_name, race_multiplier, qi_control, pph_base = char
    with st.container():
        st.markdown(f"""
            <div class="character-box">
                <div class="character-header">{char_name}</div>
                <div class="character-value">Multiplicador Racial: {race_multiplier:.2f}</div>
                <div class="character-value">Controle de Qi: {qi_control:.2f}</div>
                <div class="character-value">PPH BASE: {pph_base:.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        if st.button("Remover", key=f"remove_{char_id}"):
            remove_character(char_id)
            st.experimental_rerun()  # Rerun the script to refresh the page and show updated character list
