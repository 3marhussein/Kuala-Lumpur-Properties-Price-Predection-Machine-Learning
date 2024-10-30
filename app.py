#!/usr/bin/env python3
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from home import show_home
from predict_page import show_predict_page
from explore_page import show_explore_page
from contactus import show_contact_page
import base64
import hashlib
import sqlite3


# -- start hiding the MainMenu and adding Footer --
hide_menu="""
<style>

footer:after{
     content:'Copyright @Omar Hussein';
     display: block;
     position: relative;
     color: tomato;
     font-size: 1.4em;
}
</style>
"""
st.markdown(hide_menu,unsafe_allow_html=True)

#--end hiding the MainMenu and adding Footer --

@st.cache(allow_output_mutation=True)

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

#--- login_page --
# Security
#passlib,hashlib,bcrypt,scrypt
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

menu = ["Login","SignUp"]
choice = st.sidebar.selectbox("",menu)

if choice == "SignUp":
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password",type='password')

    if st.button("Signup"):
        create_usertable()
        add_userdata(new_user,make_hashes(new_password))
        st.success("You have successfully created a valid Account")
        st.info("Go to Login Section")

elif choice == "Login":
    st.sidebar.subheader("Login Section")

    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password",type='password')
    if st.sidebar.checkbox("Login"):
        create_usertable()
        hashed_pswd = make_hashes(password)

        result = login_user(username,check_hashes(password,hashed_pswd))
        if result:
            st.sidebar.success("Logged In as {}".format(username))

            selected = option_menu(
                menu_title = None,
                options=["Home", "Predict", "Explore", "Contact Us"],
                icons=["house", "building", "globe", "envelope"],
                menu_icon="cast",
                orientation="horizontal"
            )

            if selected == "Predict":
                show_predict_page()
            elif selected == "Explore":
                show_explore_page()
            elif selected == "Home":
                show_home()
            else:
                show_contact_page()
        else:
            st.warning("Incorrect Username/Password")






# # -- start menu option --
#     selected = option_menu(
#         menu_title = None,
#         options=["Home", "Predict", "Explore", "Contact Us"],
#         icons=["house", "building", "globe", "envelope"],
#         menu_icon="cast",
#         orientation="horizontal"
#     )
#
#     if selected == "Predict":
#         show_predict_page()
#     elif selected == "Explore":
#         show_explore_page()
#     elif selected == "Home":
#         show_home()
#     else:
#         show_contact_page()
