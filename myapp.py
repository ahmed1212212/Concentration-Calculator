import streamlit as st

def calculate_mass(volume, concentration, molecular_weight):
    # Calculate mass using the formula: mass = volume * concentration * molecular weight
    mass = volume * concentration * molecular_weight
    return mass

def calculate_concentration(volume, concentration, molecular_weight, n, mode):
    # Calculate concentration based on the selected mode (molarity or normality)
    if mode == "Molarity":
        return concentration
    elif mode == "Normality":
        # Calculate normality using the formula: normality = concentration * volume * molecular_weight / n
        normality = concentration * volume * molecular_weight / n
        return normality

def main():
    st.set_page_config(page_title="Concentration Calculator", page_icon=":test_tube:")

    st.title("Concentration Calculator")

    # Information about you
    st.write("""
    ## 
    I am Ahmed Alhilal who is teacher assistant at King Faisal University""")

    st.title("Concentration Calculator")

    # User input fields
    volume = st.number_input("Enter volume (in liters):", min_value=0.0, step=0.1)
    concentration = st.number_input("Enter concentration:", min_value=0.0, step=0.1)
    molecular_weight = st.number_input("Enter molecular weight:", min_value=0.0, step=0.1)
    n_placeholder = "e.g., 1 for monoprotic acids, 2 for diprotic acids, etc."
    n = st.number_input("Enter the number of equivalents in the reaction:", min_value=1, step=1, help=n_placeholder)
    chemical_name = st.text_input("Enter chemical name or formula:")
    solvent_name = st.text_input("Enter solvent name:")
    mode = st.radio("Select concentration mode:", ("Molarity", "Normality"))

    if st.button("Calculate"):
        # Check if all inputs are provided
        if volume != 0 and concentration != 0 and molecular_weight != 0 and n != 0:
            calculated_concentration = calculate_concentration(volume, concentration, molecular_weight, n, mode)
            mass = calculate_mass(volume, calculated_concentration, molecular_weight)
            if mode == "Molarity":
                st.markdown(f"**Mass of solute required to dissolve {mass:.2f} grams of {chemical_name} in {volume:.2f} liters of {solvent_name} at {concentration:.2f} Molarity:**")
            elif mode == "Normality":
                st.markdown(f"**Mass of solute required to dissolve {mass:.2f} grams of {chemical_name} in {volume:.2f} liters of {solvent_name} at {calculated_concentration:.2f} Normality:**")
            st.write(f"{mass:.2f} grams")
        else:
            st.error("Please fill in all fields.")

if __name__ == "__main__":
    main()
