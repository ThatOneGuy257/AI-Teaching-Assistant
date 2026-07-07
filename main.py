from google_sheets import find_class

def main():
    class_info = find_class("C2")

    print("Teaching Assistant")
    print("------------------")

    print(f"Class: {class_info['Class']}")
    print(f"Current Slide: {class_info['Current Slide']}")
    print(f"Next Class: {class_info['Days']} at {class_info['Time']}")

if __name__ == "__main__":
    main()