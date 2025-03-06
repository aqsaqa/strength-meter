import streamlit as st
import re

# Password strength checker function
def check_password_strength(password):
    # Criteria for strong password
    length = len(password) >= 8
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    number = bool(re.search(r'[0-9]', password))
    special_char = bool(re.search(r'[@#$%^&+=]', password))

    # Calculate strength score based on criteria
    score = sum([length, uppercase, lowercase, number, special_char])

    if score == 5:
        return "Very Strong", "green"
    elif score == 4:
        return "Strong", "lightgreen"
    elif score == 3:
        return "Medium", "yellow"
    elif score == 2:
        return "Weak", "orange"
    else:
        return "Very Weak", "red"

# Streamlit UI
st.title("🔒 Password Strength Meter")

# User input for password
password = st.text_input("Enter your password:", type="password")

if password:
    strength, color = check_password_strength(password)
    st.markdown(f"### Password Strength: **{strength}**", unsafe_allow_html=True)
    st.markdown(f'<div style="background-color:{color}; padding:10px; border-radius:5px; color:white;">{strength}</div>', unsafe_allow_html=True)

# Instructions for users
st.write("""
### Tips for creating a strong password:
- Use at least 8 characters.
- Include uppercase and lowercase letters.
- Include at least one number and one special character (@, #, $, etc.).
""")
