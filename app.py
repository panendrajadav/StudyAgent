import streamlit as st
from agent import ask_ai

st.set_page_config(page_title="Physics & Chemistry AI Tutor", page_icon="🧪")

st.title("🧪 Physics & Chemistry Problem Solver")
st.write("Ask any Physics or Chemistry problem, and the AI tutor will help you step-by-step!")

query = st.text_area("Enter your question here:")

if st.button("Solve"):
    if query:
        with st.spinner("Solving..."):
            response = ask_ai(query)
            st.success("Here's the solution:")
            st.write(response)
    else:
        st.warning("Please enter a question first.")
