from __future__ import print_function

import os.path
import numpy as np

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
# SAMPLE_SPREADSHEET_ID='1peqqPz2FFA1kUzsPIkNK7F5bpgkSTGgV2-p6TBd933w' 
SPREADSHEET_IDS_IN_WEEK_ORDER = ['1wlO0VSE_ZE0Gw9flqciO7fU87XPclArfkI1DsBHIpAo', '1Cor_aDB9fmUKWV4qyRP_9wQ7RIrCdyhF_r0XSanU8FA', '1peqqPz2FFA1kUzsPIkNK7F5bpgkSTGgV2-p6TBd933w', 'binou']
SAMPLE_SPREADSHEET_ID='1Cor_aDB9fmUKWV4qyRP_9wQ7RIrCdyhF_r0XSanU8FA' 
# SAMPLE_RANGE_NAME = 'A1:E'
SAMPLE_RANGE_NAME = 'A:Z'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'creds_googleapi/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    results = []
    sorted_results = []

    for index, spreadsheet_id in enumerate(SPREADSHEET_IDS_IN_WEEK_ORDER):
        try:
            result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                        range=SAMPLE_RANGE_NAME).execute()
            results.append(result)

        except HttpError as err:
            results.append({"values": []})
            print(f"cannot fetch data for week {index + 1}")
            print()
            
    for result in results:
        values = np.array(result.get('values', []))

        if len(values) == 0:
            sorted_results.append([])
            continue

        user_values = values[1:]
        user_values[:, 1] = np.char.lower(user_values[:, 1])
        sorted_results.append(user_values[user_values[:, 1].argsort()])
    

    week1 = np.array(sorted_results[0]) 
    week2 = np.array(sorted_results[1]) 
    week3 = np.array(sorted_results[2]) 
    week4 = np.array(sorted_results[3]) 

    week1 = np.delete(week1, [0, 2, -2, -1], axis=1)
    print(week2)
    all_data = []



if __name__ == '__main__':
    main()