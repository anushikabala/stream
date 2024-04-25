import streamlit as st

# Define your flowchart here
flowchart = {
    "Start": {
        "question": "Welcome! Would you like to start?",
        "options": ["Yes", "No"],
        "next": {"Yes": "Option 1", "No": "End"}
    },
    "Option 1": {
        "question": "Option 1: Do you want more information?",
        "options": ["Yes", "No"],
        "next": {"Yes": "Option 2", "No": "End"}
    },
    "Option 2": {
        "question": "Option 2: Are you sure?",
        "options": ["Yes", "No"],
        "next": {"Yes": "End", "No": "Option 1"}
    },
    "End": {
        "question": "Thank you for using the chatbot!",
        "options": []
    }
}

def chatbot():
    current_state = "Start"
    
    while current_state != "End":
        question = flowchart[current_state]["question"]
        options = flowchart[current_state]["options"]
        
        st.write(question)
        
        for option in options:
            if st.button(option):
                current_state = flowchart[current_state]["next"][option]
                break

def main():
    st.title("Chatbot Demo")
    st.write("This is a simple chatbot demo.")
    chatbot()

if __name__ == "__main__":
    main()
