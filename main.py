from google_sheets import find_class
from ai import ask_ai

def create_teaching_brief(class_name):
    # Get class information
    class_info = find_class(class_name)

    if class_info is None:
        return "Class not found"

    # Create a prompt for the AI
    prompt = f"""
    You are a teaching assistnat helping a programming instructor.

    Createa a short teaching brief for today's class/

    Class information:
    - Class: {class_info['Class']}
    - Schedule: {class_info['Days']} at {class_info['Time']}
    - Current Slide: {class_info['Current Slide']}
    
    Include:
    1. What the teacher should focus on.
    2. Possible student struggles
    3. A suggested warm up activity for the first 10 minites of class (Blooket, riddles, would you rather questions)
    4. Any reminders

    Keep it concise and pratical
    """

    # Ask AI
    response = ask_ai(prompt)
    return response

def main():
    #class_info = find_class("C2")
    print("Teaching Assistant")
    print("------------------")
    
    brief = create_teaching_brief("C2")
    print(brief)
    # print(f"Class: {class_info['Class']}")
    # print(f"Current Slide: {class_info['Current Slide']}")
    # print(f"Next Class: {class_info['Days']} at {class_info['Time']}")

if __name__ == "__main__":
    main()