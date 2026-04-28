import streamlit as st
st.set_page_config(page_title="Griffith Timetable Master", page_icon="🔗")
target_url = "https://griffix.streamlit.app"
st.components.v1.html(
    f"""
    <script type="text/javascript">
        window.parent.location.href = "{target_url}";
    </script>
    """,
    height=0,
)

st.title("Redirecting...")
st.write(f"We are moving you to our new site.")

st.markdown(
    f"""
    <div style="margin-top: 20px;">
        If you aren't redirected automatically, 
        <a href="{target_url}" target="_self">click here to open the site</a>.
    </div>
    """, 
    unsafe_allow_html=True
)
