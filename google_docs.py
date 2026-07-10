from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from pprint import pprint
doc_key = "Insert docs key here"

def get_doc_service():
    scopes = [
        "https://www.googleapis.com/auth/documents",
        "https://www.googleapis.com/auth/drive"
    ]

    credentials = Credentials.from_service_account_file(
        "credentials.json",
        scopes = scopes
    )
    service = build("docs", "v1", credentials=credentials)
    return service

def get_document():
    service = get_doc_service()
    document = service.documents().get(
        documentId=doc_key).execute()
    return document

def clear_document():
    document = get_document()
    content = document["body"]["content"] # This is how we find the end index of the document
    end_index = content[-1]["endIndex"] # We use -1 here because then it returns the last thing in the document
    
    if end_index <= 1: return 
    service = get_doc_service()
    service.documents().batchUpdate(
        documentId=doc_key,
        body={
            "requests":[
                {
                    "deleteContentRange":{
                        "range": {
                            "startIndex": 1,
                            "endIndex": end_index - 1
                        }
                    }
                }
            ]
        }
    ).execute()

def write_document(response):
    service = get_doc_service()
    clear_document()
    service.documents().batchUpdate(
        documentId=doc_key,
        body={
            "requests":[
                {
                    "insertText": {
                        "text": response,
                        "location": {
                            "index": 1
                        }
                    }
                }

            ]
        }
    ).execute()

#This is used for testing
# This was a test to print the title of the google doc to make sure everything
#  # was working properly
# service = get_doc_service()

# document = service.documents().get(
#     documentId="ID GOES HERE").execute() # we use the document id here instead of the name like in a google sheets. 
# print(document["body"]["content"][1]["endIndex"])
# # print(document.keys()) # This shows the dictionary options.
# # print(document["body"])
# print(type(document["body"]["content"][0]))