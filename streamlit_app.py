import streamlit as st

# Define your flowchart here
flowchart = {
    "Start": {
        "question": "Please select the issue ....",
        "options": [
            
            "Center Holes",
            "Missing lenses", 
            "Edge defect",
            "Center Unknown",
            "Others"
            ],
        "next": {"Missing lenses": "Option 1", "Center Holes": "End","Edge defect": "End","Center Unknown": "End","Others": "End"}
    },
    "Option 1": {
        "question": "Are Missing Lens more than 5% ?",
        "options": ["Select","Yes", "No"],
        "next": {"Select":"End","Yes": "Option 2", "No": "End"}
    },
    "Option 2": {
        "question": "Do the need full : 1. TOL stable no gaps. 2. Total Tower time < 70 %  ",
        "options": ["Select","Done", "Back"],
        "next": {"Select":"End","Done": "Opt 3", "Back": "Option 1"}
    },
    "Opt 3": {
        "question": "Now Audit images from ALI and estimate the amount of lenses present in the sample.",
        "options": ["Select","Done", "Back"],
        "next": {"Select":"End","Done": "Opt 4", "Back": "Option 2"}
    },
    "Opt 4": {
        "question": "Are there inverted/ off center or folded lense?",
        "options": ["Select","Yes", "No","Back",],
        "next": {"Select":"End","Yes": "Opt 9", "No": "Opt 5","Back": "Opt 3"}
    },
    "Opt 5": {
        "question": "Are there correctly oriented lenses in the audit?",
        "options": ["Select","Yes", "No","Back",],
        "next": {"Select":"End","Yes": "Opt 6", "No": "Opt 7","Back": "Opt 4"}
    },
    "Opt 6": {
        "question": "Complete Lens Edge Focus of ALI Cameras",
        "options": ["Select","Done","Back",],
        "next": {"Select":"End","Done": "Opt 3", "No": "End","Back": "Opt 5"}
    },
    "Opt 7": {
        "question": "Audit confirms missing lenses",
        "options": ["Select","Done","Back",],
        "next": {"Select":"End","Done": "Opt 8", "No": "End","Back": "Opt 5"}
    },
    "Opt 8": {
        "question": "Complete YAS audit to determine if location specific Missing",
        "options": ["Select","Location specific","General Missing",],
        "next": {"Select":"End","Location specific": "Opt 9", "General Missing": "End","Back": "Opt 6"}
    },
    "Opt 9": {
        "question": "Lenses become inverted, folded or off cemter in hydration towers or at transfer LTH",
        "options": ["Select","Proceed","Back",],
        "next": {"Select":"End","Proceed": "End", "No": "End","Back": "End"}
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
        
        selected_option = st.selectbox(question, options)
        
        current_state = flowchart[current_state]["next"][selected_option]

def main():
    st.title("Vision Care")
    st.write("Select the option from the dropdown (currently back option isn't working)")
    chatbot()

if __name__ == "__main__":
    main()
