from gspread import authorize
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from sys import exit
import json

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

dt = datetime.now()
dt_date = dt.strftime("%Y-%m-%d")
dt_time = dt.strftime("%H:%M")

score_filepath = "/tmp/score_update"

try:
   with open(score_filepath) as infile:
      row = json.loads(infile.readline())
      # print(f"score={row}")
except Exception as e: 
   print(e)
   exit(1)

if (row[0] == 'drill'):
   sheet_name = 'drills'
elif (row[0] == 'game'):
   sheet_name = 'games'
else:
   print(f"Invalid {score_filepath} line 1: {row}")
   exit(1)

row[0] = dt_time
row.insert(0, dt_date)
#Date,Time,Drill,Drill#,Duration,Average_Score,Average_Speed
values = [row] # values can have multiple rows

# the keys are in a locally stored file
credentials = ServiceAccountCredentials.from_json_keyfile_name("write-drill-scores-tappan-280027e40360.json", scopes)
try:
   file = authorize(credentials)
   sheet = file.open("Drill_Scores_Tappan")
   sheet.values_append(sheet_name, {'valueInputOption': 'USER_ENTERED'}, {'values': values})
except Exception as e: 
   print(e)
   exit(1)
