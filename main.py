import streamlit as st
st.write("<h1>Hello world</h1>",unsafe_allow_html=True)
#ing colour of text
st.write("<h1 style='color: red;'>hello world</h1>",unsafe_allow_html=True)
#uploading file
st.file_uploader("upload file")
#upload image
#upload video
st.video("https://www.youtube.com/watch?v=MkLhijus3vg")

