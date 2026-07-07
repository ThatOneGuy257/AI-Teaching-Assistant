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

    return sheet.get_all_records()

def find_class(class_name):
    classes = get_classes()

    for class_info in classes:
        if class_info["Class"] == class_name:
            return class_info
        
    return None

# #Test it
# my_class = find_class("C2")

# print(my_class)



