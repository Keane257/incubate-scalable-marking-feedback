from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

import json

with open('output/q1_labelled.json') as f:
    q1_data = json.load(f)

q1_dict = q1_data[0]['boundingBox']['boundingBoxes']
q1 = len(q1_dict)

with open('output/q2_labelled.json') as f:
    q2_data = json.load(f)

q2_dict = q2_data[0]['boundingBox']['boundingBoxes']
q2 = len(q2_dict)

with open('output/q3_labelled.json') as f:
    q3_data = json.load(f)

q3_dict = q3_data[0]['boundingBox']['boundingBoxes']
q3 = len(q3_dict)

import pandas as pd
# intialise data of lists. 
data = {'Question':['Q1', 'Q2', 'Q3'], 
        'Marks':[q1, q2, q3]} 
  
# Create DataFrame 
df = pd.DataFrame(data) 
  
df.to_csv('output.csv')

drive = GoogleDrive(gauth)
file1 = drive.CreateFile()
file1.SetContentFile('output.csv')
file1.Upload()
