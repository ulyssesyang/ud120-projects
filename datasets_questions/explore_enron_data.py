#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print('enron_data length:', len(enron_data))
enron_data_features = (enron_data.values()[0]).keys()
print('enron_data features number:', len(enron_data_features),enron_data_features)

POI_p = []
for person in enron_data:
    if enron_data[person]["poi"]==1:
        POI_p.append(person)

print('enron_data poi number:', len(POI_p))

for person in enron_data:
    if ("Prentice").upper() in person:
        print(person,"total_stock_value:",enron_data[person]["total_stock_value"])
        
for person in enron_data:
    if ("Wesley").upper() in person:
        print(person,"from_this_person_to_poi:",enron_data[person]["from_this_person_to_poi"])

for person in enron_data:
    if ("Skilling").upper() in person:
        print(person,"exercised_stock_options:",enron_data[person]["exercised_stock_options"])

for person in enron_data:
    if ("Lay").upper() in person or ("Skilling").upper() in person or ("Fastow").upper() in person:
        print(person,"total_payments:",enron_data[person]["total_payments"])

# for person in enron_data:
#     for feature in enron_data_features:
#         # print(person,feature,enron_data[person][feature])
#         if enron_data[person][feature] == 'NaN':
#             print(person,feature,enron_data[person][feature])

p_salary = []
p_email = []
p_noTotalPayment = []
poi_noTotalPayment = []
for person in enron_data:
    for feature in enron_data_features:
        if feature == 'salary' and enron_data[person][feature] != 'NaN':
            p_salary.append(person)
        if feature == 'email_address' and enron_data[person][feature] != 'NaN':
            p_email.append(person)
        if feature == 'total_payments' and enron_data[person][feature] == 'NaN':
            p_noTotalPayment.append(person)
        if feature == 'total_payments' and enron_data[person]["poi"]==1 and enron_data[person][feature] == 'NaN':
            poi_noTotalPayment.append(person)
print("persons have salary:",len(p_salary))
print("persons have email:",len(p_email))
print("persons have no total_payments:",len(p_noTotalPayment),1.0*len(p_noTotalPayment)/len(enron_data))
print("poi have no total_payments:",len(poi_noTotalPayment),1.0*len(poi_noTotalPayment)/len(POI_p))

poi_names_txt = open("../final_project/poi_names.txt", "r")
all_lines = poi_names_txt.read().split('\n')
print('enron_data all_lines:',len(all_lines), all_lines)
poi_names_lines = []
for line in all_lines:
    if len(line)>0 and line[1]=='y':
        poi_names_lines.append(line)
print('enron_data poi_names:',len(poi_names_lines), poi_names_lines)