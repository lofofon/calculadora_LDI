import streamlit as st

st.write("# Meditação")

# Slider for selecting a value from 1 to 30
meditation_time = st.slider("Select meditation time (1-30)", min_value=1, max_value=30, step=1)

# Example list of selected characters (you should replace this with st.session_state["selected_characters"])
selected_characters = [
    {
        "1": {
            "char_name": "Arashi",
            "pph_base": 1.3200000000000003
        }
    },
    {
        "2": {
            "char_name": "Hanzo",
            "pph_base": 2.3499999999999996
        }
    }
]

# Predefined bonuses dictionary with fixed attributes
extra_bonuses = {
    "bonus_1": {"bonus_value": 5, "duration": 10},
    "bonus_2": {"bonus_value": 3, "duration": 20},
    "bonus_3": {"bonus_value": 7, "duration": 15}
}

# Initialize session state for extra bonuses count if it doesn't exist
if "bonus_counts" not in st.session_state:
    st.session_state["bonus_counts"] = {char_id: {key: 0 for key in extra_bonuses} for char in selected_characters for char_id in char}

# Function to update bonus counts
def update_bonus_counts(char_id, key, count):
    st.session_state["bonus_counts"][char_id][key] = count

# Display each character in a box with their name, PPH, and integer inputs for bonus counts
for char in selected_characters:
    for char_id, char_info in char.items():
        char_name = char_info["char_name"]
        pph_base = char_info["pph_base"]

        with st.container():
            st.markdown(f"""
                <div style="border: 1px solid #ddd; padding: 10px; margin: 10px 0; border-radius: 5px;">
                    <div style="display: flex; justify-content: space-between;">
                        <div style="font-size: 20px; font-weight: bold;">{char_name}</div>
                        <div style="font-size: 16px;">PPH: {pph_base:.2f}</div>
                    </div>
            """, unsafe_allow_html=True)

            # Display integer inputs for each key in extra bonuses
            st.markdown("<hr class='solid'>", unsafe_allow_html=True)
            for key in extra_bonuses:
                bonus_value = extra_bonuses[key]["bonus_value"]
                duration = extra_bonuses[key]["duration"]
                count = st.session_state["bonus_counts"][char_id].get(key, 0)

                col1, col2 = st.columns([2, 1])
                with col1:
                    new_count = st.number_input("Quantidade", label_visibility="hidden" , min_value=0, max_value=99, value=count, step=1, key=f"{char_id}_{key}")
                    update_bonus_counts(char_id, key, new_count)
                with col2:
                    st.write(f"{key}")
                    st.write(f"Valor: {bonus_value}")
                    st.write(f"Duração: {duration})")
                st.markdown("<hr class='solid'>", unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

# Debugging: print the list of selected characters with their bonus counts
st.write("Updated Selected Characters with Bonus Counts:", st.session_state["bonus_counts"])
