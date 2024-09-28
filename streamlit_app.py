import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Set up the connection
conn = st.connection("gsheets", type=GSheetsConnection)

# Read the data from the Google Sheet
df = conn.read(worksheet="PET", ttl=5)

# Streamlit app
st.title("🐶🐱 Pet Adoption Application 🐰🐦")
st.write("Welcome to our Pet Adoption Application! Fill out the form below to apply for adopting a pet.")

# Application Form
st.header("Adoption Application Form")

name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
address = st.text_area("Home Address")

pet_type = st.selectbox("What type of pet are you interested in adopting?", 
                        ["Dog", "Cat", "Rabbit", "Bird", "Other"])

if pet_type == "Other":
    other_pet = st.text_input("Please specify the type of pet:")

experience = st.radio("Do you have experience with pets?", ["Yes", "No"])

if experience == "Yes":
    pet_experience = st.text_area("Please describe your experience with pets:")

home_type = st.selectbox("What type of home do you live in?", 
                         ["House", "Apartment", "Condo", "Other"])

own_rent = st.radio("Do you own or rent your home?", ["Own", "Rent"])

if own_rent == "Rent":
    landlord_approval = st.checkbox("I have approval from my landlord to have a pet")

household_members = st.number_input("How many people live in your household?", min_value=1, value=1)

children = st.checkbox("Are there children under 18 in your household?")

if children:
    children_ages = st.text_input("Please list the ages of children:")

current_pets = st.checkbox("Do you currently have any pets?")

if current_pets:
    current_pet_details = st.text_area("Please provide details about your current pets:")

vet_info = st.text_input("If you have a preferred veterinarian, please provide their name and contact information:")

reason = st.text_area("Why do you want to adopt a pet?")

# Submit button
if st.button("Submit Application"):
    # Create a new row with the form data
    new_row = pd.DataFrame([{
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Address": address,
        "Pet Type": pet_type if pet_type != "Other" else other_pet,
        "Experience": experience,
        "Pet Experience": pet_experience if experience == "Yes" else "",
        "Home Type": home_type,
        "Own/Rent": own_rent,
        "Landlord Approval": "Yes" if own_rent == "Rent" and landlord_approval else "No",
        "Household Members": household_members,
        "Children": "Yes" if children else "No",
        "Children Ages": children_ages if children else "",
        "Current Pets": "Yes" if current_pets else "No",
        "Current Pet Details": current_pet_details if current_pets else "",
        "Vet Info": vet_info,
        "Reason": reason
    }])
    
    # Append the new row to the Google Sheet
    conn.append(worksheet="PET", data=new_row)
    
    st.success("Thank you for submitting your application! We will review it and get back to you soon.")

# Display current adoptions
st.header("Current Adoptions")
st.dataframe(df)

# Footer
st.markdown("---")
st.write("© 2024 Pet Adoption Center. All rights reserved.")
