import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from gsheetsdb import connect

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    {
        "type": "service_account",
        "project_id": "pet-entry-form",
        "private_key_id": "8ec0af7a983ee702c473564aa572f54d4cbc7d75",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDEg0ogpp0i+ris\nooRrKJkL9CBuu+it2w90YNaelfy9RyiEcHbaUCiuLyN3wXkI1uclXlNuCCFwhQjk\noOkarnMNtMGPDtZiHrQrAi12YucxKn7pCX+s4sqArwqRJW2sy72CE9FQQy8wjNTz\nKTvuagbEjrubIF0rTJN+w8FgORwCGuU3I3SAMf0CwCc9m/1ez9jzlks+Xt7zzMDT\nHkUW/0X2QgsT2E+bRC4ZJ3lmjiPf6m05hN50NKIPAkQi2XkbC2au0hXgbjDfvmCN\nxJw4f3uia6vnJWLYSHBKP5w+6e9d9SQcge50OMp7+wAW9MCEZvpay5NUqxUXby6z\n8rgBWwHBAgMBAAECggEAE+0yN5Rdi737uvmxzsHrnwQuw7vHMNXtP8JQEP2phrHw\nAFn9G08UiPEbuhmCwew0vRvO/vHRHj1HNRPB/2QgI4woMm7xOzrczx2l6YLG6bvi\n6ZN+gFPw79KQEj7G28Y/HbEPwQFHCDfHoi6UtqzGqejFSkoiWHEn5atI8Q5pcicF\nJ79u2XJy687CQUNp8OMqPAQXCor5/0qilCImSBLRBbePWhgY2OBnAWO7fr/hnqEi\nNWY1p1nlL1Y5VSaebEDxu1CtslQQo5K/zgZov7UJ5uIYP4IonylaHnpOLKSdJ6TL\ninhx7gzopeL9523wnNJ69j7rkBoWLbtcOtFyeQnLCQKBgQD/Revik13PTlFeJ5KD\n6COXrUG/4n6hudNI3T7bV0OZqKeBhytxcV+ju/tljsgssnEpBPzWrYamdwdUDQhY\n9nJqX6uOK/esuyJEDTD+YvE+YjWVvrrVuAKGlr3cDpxn432KgG4Nc9PUnuRdu2t+\nL4o+mFr1PDnnO+Vmg4RbLVZoBQKBgQDFEokUWNV5XzvWWy2UzYRv/s0UFrVcvyQZ\nOUcoLObLix7gxwAAUI88xM6qVLmkuGAZLK0MW5/OIN9tJxiU48UJUdm8RLMc77kV\ntjXwYg3+ih3P/ErhhB+5+oaPZvR0Q90eU/vTWHZsMVm/haC3sukvOLBNY/CobFyA\nIFdahHWLjQKBgBIAzmgGWKFcNqTbSZv/7TKvR2nPAXtKbbo/0EUL3HqjyFx8OfYg\nNsyHX22EKl3sn8pyzZoeVta6okutN59+kgcqhCDcvPTzpbEC9SebtsPdjUXoU6jq\n91KiovU4GpPBGYOBF0Hfn1rpcdWieCxIEgnkGNYezz6dnMokEFuV0Pg5AoGAFMga\nmoGvqUfoqHce/GUbxS+qcqbeYzRo2xwWK99oSyiVjgCOOHpGUJM0c/PRS9SBlcYH\nTZlP5c3DoeAQkIrgWVY/TsIz3SZOb0Kyt3Gvphrsf+VMBDIJonQPwomJ18TcSXlz\nwdq/SjN+EltGEnkUa/1fYhna4/fhXUWL0KjNOHUCgYEA4kbdOzgkkBCX0qdh7ztl\nlz5z2LtO9CyL4X3oZo4XXb9qXE3HTl4a/H9tFRatiJvmYIgEjKJ6PkMCxO3N+2uw\nYNhmAiVmYqKUcQ6iw/h8g8+d7oqZ6qLIGE0fwLMxfcQRrZ8DlHJrO7oFQGw+oJ/j\nM+ZkqF3hsPmqbl+N5sVQBjY=\n-----END PRIVATE KEY-----\n",
        "client_email": "gsheets-python-access@pet-entry-form.iam.gserviceaccount.com",
        "client_id": "102715758211200158863",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/gsheets-python-access%40pet-entry-form.iam.gserviceaccount.com"
    },
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ]
)

conn = connect(credentials=credentials)

# Perform SQL query on the Google Sheet.
sheet_url = "https://docs.google.com/spreadsheets/d/11Fcm58YPDnmPbGKW1TmdmSh1xH8rReUax_AaUvuZtoE/edit#gid=0"
rows = conn.execute(f'SELECT * FROM "{sheet_url}"')

# Convert to pandas DataFrame
df = pd.DataFrame(rows)

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
    st.text_area("Please describe your experience with pets:")

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
    # Here you would typically process the form data, 
    # perhaps adding it to your Google Sheet or database
    st.success("Thank you for submitting your application! We will review it and get back to you soon.")

# Display current adoptions
st.header("Current Adoptions")
st.dataframe(df)

# Footer
st.markdown("---")
st.write("© 2024 Pet Adoption Center. All rights reserved.")
