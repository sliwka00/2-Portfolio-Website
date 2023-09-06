import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/img.jpg")

with col2:
    st.title("Paweł Śliwa")
    content = """
    Hi, I am Paweł! bla, bla, bla.
    ....
    ......
    ..........\n
    ..............
    """
    st.info(content)

content2="""
Below you can find some of the apps i have built in Python.
"""
st.write(content2)