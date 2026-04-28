import streamlit as st

st.set_page_config(page_title="Griffith Timetable Master", page_icon="🔗")
target_url = "https://griffix.streamlit.app"

st.title("We've Moved! 🚀")
st.info("The Griffith Timetable Master is now **Griffix**.")

st.link_button("Go to Griffix", target_url, type="primary", use_container_width=True)
