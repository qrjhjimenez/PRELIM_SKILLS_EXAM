import csv
import json
from os import write

file = './covid_cases.json'
with open(file) as data_file:
    retrieving = json.loads(data_file.read())

record_list = retrieving['records']
covid_cases = open('retrieved_data.csv','w')
output = csv.writer(covid_cases)

x = 0
for records in record_list:
    if x == 0:
        header = records.keys()
        output.writerow([records["dateRep"],records["cases"],records["countriesAndTerritories"],records["deaths"]])