import sqlite3
import streamlit as st



def init_database():
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('characters.db')
    c = conn.cursor()
    # Create a table for characters
    c.execute('''
        CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            character_name TEXT NOT NULL,
            race_multiplier INT NOT NULL,
            qi_control INT NOT NULL,
            pph REAL NOT NULL
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def get_all_characters():
    # Connect to the database
    conn = sqlite3.connect('characters.db')
    c = conn.cursor()

    # Retrieve all characters with their ID
    c.execute('SELECT id, character_name, race_multiplier, qi_control, pph FROM characters')
    characters = c.fetchall()

    # Close the connection
    conn.close()

    return characters

def send_character_to_db(character):
    # Initialize session state variable
    if "message" not in st.session_state:
        st.session_state["message"] = ""

    # Connect to the database
    conn = sqlite3.connect('characters.db')
    c = conn.cursor()

    # Insert the character data into the database
    c.execute('''
        INSERT INTO characters (character_name, race_multiplier, qi_control, pph)
        VALUES (?, ?, ?, ?)
    ''', (character.character_name, character.race_multiplier, character.qi_control, character.base_meditation_points_per_hour))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Update the message
    st.session_state["message"] = f"{character.character_name} enviado para o db."

def remove_character(character_id):
    # Connect to the database
    conn = sqlite3.connect('characters.db')
    c = conn.cursor()

    # Debug: print the character ID being removed
    print(f"Removing character with ID: {character_id}")

    # Delete the character from the database
    c.execute('DELETE FROM characters WHERE id = ?', (character_id,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Update the message
    st.session_state["message"] = "Personagem removido do db."