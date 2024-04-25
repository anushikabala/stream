import streamlit as st

import flowchart as flowchart
# Define your flowchart here

def chatbot():
    current_state = "Start"
    
    while current_state != "End":
        question = flowchart[current_state]["question"]
        options = flowchart[current_state]["options"]
        
        selected_option = st.selectbox(question, options)
        
        current_state = flowchart[current_state]["next"][selected_option]

def main():
    st.title("Chatbot Demo")
    st.write("This is a simple chatbot demo.")
    chatbot()

if __name__ == "__main__":
    main()
