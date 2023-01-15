from gspread import authorize
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("write-drill-scores-tappan-280027e40360.json", scopes)
file = authorize(credentials)
sheet = file.open("Drill_Scores_Tappan")
# sheet = sheet.sheet1
# sheet.update_cell(2, 3, 'Red')

#client = gspread.authorize(credentials)
#sheet = client.open_by_key(spreadsheetId)

#Date,Time,Drill,Drill#,Duration,Average_Score,Average_Speed
values = [[1,2,3,4,5]]
sheet.values_append('drills', {'valueInputOption': 'USER_ENTERED'}, {'values': values})
