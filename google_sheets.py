import gspread 
from google.oauth2.service_account import Credentials


# #Connect to Google
# scopes = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive"
# ]
# credentials = Credentials.from_service_account_file(
#     "credentials.json",
#     scopes=scopes
# )

# client = gspread.authorize(credentials)

# # Open spreadsheet
# spreadsheet = client.open("Teaching Assistant Database")

# # Open the Classes tab
# sheet = spreadsheet.worksheet("Classes")

# # Read data
# data = sheet.get_all_records()

# print(data)


def get_classes():
    sheet = get_sheet()
    return sheet.get_all_records()

def get_sheet():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    credentials = Credentials.from_service_account_file(
        "credentials.json",
        scopes = scopes
    )

    client = gspread.authorize(credentials)

    spreadsheet = client.open("Teaching Assistant Database")
    sheet = spreadsheet.worksheet("Classes")
    return sheet

def find_class(class_name):
    classes = get_classes()

    for class_info in classes:
        if class_info["Class"] == class_name:
            return class_info
        
    return None

def update_slides(class_name, slide):
    print("Updating . . .")
    classes = get_classes()
    for index, class_info in enumerate(classes):
        if class_info["Class"] == class_name:
            class_row = index + 2
            sheet = get_sheet()
            old_slide = class_info["Current Slide"]
            sheet.update_cell(class_row, 4, slide)
            return {
                "success": True,
                "old_slide": old_slide,
                "new_slide": slide
            }

    
    return False
    



