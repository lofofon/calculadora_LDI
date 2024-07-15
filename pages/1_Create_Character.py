import streamlit as st
from pages.dependencias.character import Character
from pages.dependencias.utils import send_character_to_db


st.write("Criação de personagem")

character_name = st.text_input(label="Escreva o nome do personagem")
character_race_multiplier = st.number_input(label="Insira o multiplicador racial do personagem", min_value=1, step=1, max_value=10)
character_qi_control = st.number_input(label="Insira valor do controle de Qi do personagem", min_value=1, step=1, max_value=10)

character = Character(character_name=character_name, race_multiplier=character_race_multiplier, qi_control=character_qi_control)


if st.button(label="Adicionar Personagem"):
    send_character_to_db(character)

# Display the message
st.write(st.session_state["message"])