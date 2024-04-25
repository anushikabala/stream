import streamlit as st

# Define your flowchart here
flowchart = {
    "Start": {
        "question": "Welcome! Would you like to start?",
        "options": ["Yes_Start", "No_Start"],
        "next": {"Yes_Start": "Option 1", "No_Start": "End"}
    },
    "Option 1": {
        "question": "Option 1: Do you want more information?",
        "options": ["Yes_Option1", "No_Option1"],
        "next": {"Yes_Option1": "Option 2", "No_Option1": "End"}
    },
    "Option 2": {
        "question": "Option 2: Are you sure?",
        "options": ["Yes_Option2", "No_Option2"],
        "next": {"Yes_Option2": "End", "No_Option2": "Option 1"}
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
