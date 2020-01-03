import gspread
from oauth2client.service_account import ServiceAccountCredentials

# define which APIs will be accessed
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# add credentials received from Google API Console
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'foo.json', scope)

# authorize access with credentials
authorizedRemote = gspread.authorize(credentials)

worksheet = authorizedRemote.open('Test').sheet1

payload = open("results.txt").readlines()
payload = [s.rstrip('\n') for s in payload]

# worksheet.append_row()

for i in payload:
    record = i.split(', ')
    record1 = record[0]
    record2 = record[1]
    print('Sending results for ' + record1)
    worksheet.append_row(['{}'.format(record1), '{}'.format(record2)])
    # print(i)

print("Finished updating worksheet")
