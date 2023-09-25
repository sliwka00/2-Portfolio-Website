import streamlit as st
import pandas as pd

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

col3, empty_col,col4 =st.columns([1.5,0.5,1.5])   # dodajemy pustą kolumnę o wymiarach 0.5 , żeby była przerwa między col3 i col 4

df=pd.read_csv('data.csv',sep=";")
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write(f"[Source code]({row['url']})")      # 'Source code' pojawi się hiperlink z tą nazwą, po kliknięciu przeniesie do adresu w nawiasie np. adres repo github
with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row['image'])
        st.write(f"[Source code]({row['url']})")