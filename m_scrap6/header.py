import csv
headers = ['LastName','Status','Number','City','AdmissionDate','Address','Phone','Fax','Email','Website','Speciality','Link']

with open('output.csv', 'w', newline='', encoding="utf-8") as output_file:
    dict_writer = csv.DictWriter(output_file, headers)
    dict_writer.writeheader()  

print("header writed to file")