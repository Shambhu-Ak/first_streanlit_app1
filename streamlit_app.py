import streamlit
streamlit.title("WELCOME TO CAPGEMINI")
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



my_fruit_list = pandas.read_csv("C:\Users\SASHOKAK\Desktop\uni-lab-files.s3.us-west-2.amazonaws.com_dabw_fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
