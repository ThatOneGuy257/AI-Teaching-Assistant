from google_sheets import find_class, update_slides
from ai import ask_ai
from google_docs import write_document


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
    return response
    # print(response)

def handle_command(command):
    COMMANDS = {
        "help": handle_help,
        "brief": handle_brief,
        "update": handle_update
    }
    parts = command.strip().split()
    if not parts:
        return
    command_name = parts[0].lower()

    handler = COMMANDS.get(command_name)
    if handler is None:
        print("Unkown command, please type 'help' to see possible commands")
        return
    handler(parts)

    
def handle_help(parts):
    print("""
          Available Commands:
          Brief C2/C4
          Update C2/C4 <Slide Number>
          Help
          Quit
          """)
    return

def handle_brief(parts):
    if len(parts) != 2:
        print("Usage: brief <class>")
        return
    response = create_teaching_brief(parts[1].upper())
    write_document(response)
    print("Brief uploaded to Google Docs!")
    return

def handle_update(parts):
    if len(parts) != 3:
        print("Usage: update <class> <slide>")
        return
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
    return

    
