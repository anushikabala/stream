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
