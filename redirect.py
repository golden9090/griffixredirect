import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Griffith Timetable Master", page_icon="🔗")
target_url = "https://griffix.streamlit.app"

st.markdown(
    f'<meta http-equiv="refresh" content="0;url={target_url}">',
    unsafe_allow_html=True
)

st.title("Redirecting...")
st.write("We are moving you to the new Griffix site.")

st.markdown(
    f"""
    <div style="margin-top: 20px;">
        If you aren't redirected automatically, 
        <a href="{target_url}" target="_self">click here to open the site</a>.
    </div>
    """, 
    unsafe_allow_html=True
)
