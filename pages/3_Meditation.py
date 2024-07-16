import streamlit as st

# Debugging: print the list of selected characters
#st.write("Selected Characters:", st.session_state["selected_characters"])

st.write("# Meditação")

# Slider for selecting a value from 1 to 30
meditation_time = st.slider("Selecione o tempo de meditação em dias(1-30 dias)", min_value=1, max_value=30, step=1)
meditation_time_per_day = st.slider("Selecione o tempo de meditação por dia (1-20h)", min_value=1, max_value=20, step=1)

# Predefined bonuses dictionary with fixed attributes
extra_bonuses = {
    "Pílula de Cultivo (Fraca)": 0.10,
    "Pílula de Cultivo (Média)": 0.25,
    "Plílula de Cultivo (Forte)": 0.5,
    "Incenso de Meditação": 0.05,
    "Incenso de Meditação Potente":0.15
}

selected_characters = st.session_state["selected_characters"]

# Initialize session state for extra bonuses count if it doesn't exist
if "bonus_counts" not in st.session_state:
    st.session_state["bonus_counts"] = {str(char_id): {key: 0 for key in extra_bonuses} for char in selected_characters for char_id in char}

# Function to update bonus counts
def update_bonus_counts(char_id, key, count):
    st.session_state["bonus_counts"][str(char_id)][key] = count

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
                bonus_value = extra_bonuses[key]
                count = st.session_state["bonus_counts"][str(char_id)].get(key, 0)

                col1, col2 = st.columns([3, 1])
                with col1:
                    new_count = st.number_input("Quantidade de Horas com esse bônus", min_value=0, max_value=99, value=count, step=1, key=f"{char_id}_{key}")
                    update_bonus_counts(char_id, key, new_count)
                with col2:
                    st.write(f"{key}")
                    st.write(f"Valor (por hora): {bonus_value}")
                st.markdown("<hr class='solid'>", unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

# Debugging: print the list of selected characters with their bonus counts
# st.write("Updated Selected Characters with Bonus Counts:", st.session_state["bonus_counts"])


st.write("Simulação de Meditação")

for char in selected_characters:
    for char_id, char_info in char.items():
        char_name = char_info["char_name"]
        pph_base = char_info["pph_base"]
        total_meditation_time = meditation_time_per_day*meditation_time
        total_meditation_value = pph_base*total_meditation_time
        character_meditation_bonuses = st.session_state["bonus_counts"][str(char_id)]
        # Iterate over the keys in st.session_state["bonus_counts"][str(char_id)]
        for bonus in character_meditation_bonuses:
            duration = character_meditation_bonuses[bonus]
            if duration<= total_meditation_time:
                total_bonus = duration*extra_bonuses[bonus]
            else:
                total_bonus = duration*total_meditation_time

            total_meditation_value+= total_bonus

        
        with st.container():
            st.markdown(f"""
                        <div style="border: 1px solid #ddd; padding: 10px; margin: 10px 0; border-radius: 5px;">
                            <div style="display: flex; justify-content: space-between;">
                                <div style="font-size: 20px; font-weight: bold;">{char_name}</div>
                                <div style="font-size: 16px;">PPH: {pph_base:.2f}</div>
                            </div>
                            <div style="font-size: 16px;"> Quantidade total de horas de meditação: {total_meditation_time:.0f} {"hora" if total_meditation_time==1 else "horas"}</div>
                            <div style="font-size: 16px;"> Resultado da sessão de meditação: {total_meditation_value:.2f} Pontos</div>
                        </div>
                    """, unsafe_allow_html=True)