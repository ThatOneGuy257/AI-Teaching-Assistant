from google_sheets import find_class, update_slides
from ai import ask_ai


def create_teaching_brief(class_name):
    class_info = find_class(class_name)

    if class_info is None:
        print("Class not found")
        return
    
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
    print("\nGenerating teaching brief . . .\n")

    response = ask_ai(prompt)
    print(response)

def handle_command(command):
    command = command.strip()
    if command.lower() == "help":
        print("""
              Available Commands:

              Brief C2/C4
              Update C2/C4 *Slide Number*
              Help
              Quit
              """)
        return
    
    parts = command.split()

    if len(parts) == 2 and parts[0].lower() == "brief":
        
        create_teaching_brief(parts[1].upper())
        return
    
    if len(parts) == 3 and parts[0].lower() == "update":
        try:
            slide = int(parts[2])
        except ValueError:
            print("Slide number must be a whole number")
            return
        result = update_slides(parts[1].upper(), slide) 
        if result["success"]:
            print(f"Updated {parts[1].upper()}")
            print(f"Previous Slide: {result['old_slide']}")
            print(f"New slide: {result["new_slide"]}")
            return
        else:
            print("Command not found")
            return
    print("Unknown Command. Type 'help' to see available commands.")






