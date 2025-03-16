import streamlit as st
from Dashboard import show_support
from utils import show_footer

def chat():
    st.title("Dental Scheduling System")
    st.markdown("## 🚧 Under Development...")
    st.markdown("The appointment scheduling feature is coming soon")

    st.divider()
    show_support()

chat()
show_footer()
