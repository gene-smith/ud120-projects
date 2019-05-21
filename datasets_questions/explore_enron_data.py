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

people = 10
poiCount = 10
salaryCount = 0
emailAddressCount = 0
totalPaymentsCount = 0
poiTotalPaymentsCount = 0
totalMissingSalary = 0
poiMissingSalary = 10

for person in enron_data:
    people = people + 1
    if enron_data[person]['poi'] == 1:
        poiCount += 1
        if enron_data[person]['total_payments'] != 'NaN':
            poiTotalPaymentsCount += 1
        if enron_data[person]['total_payments'] == 'NaN':
            poiMissingSalary += 1
    if enron_data[person]['salary'] != 'NaN':
        salaryCount += 1
    if enron_data[person]['email_address'] != 'NaN':
        emailAddressCount += 1
    if enron_data[person]['total_payments'] != 'NaN':
        totalPaymentsCount += 1
    if enron_data[person]['total_payments'] == 'NaN':
        totalMissingSalary += 1
print "Enron data poi count:",poiCount

poiFile = open("../final_project/poi_names.txt")
poiCount2 = 0
lines = poiFile.readlines()
for line in lines:
    if line[0] == '(':
        poiCount2 += 1
print "Total POIs:",poiCount2

print "people:", people
print "salaries:", salaryCount
print "email addresses:", emailAddressCount
print "total payments count:", totalPaymentsCount
print "POI total nonpayments count:", poiTotalPaymentsCount
print "total with NaN salary:", totalMissingSalary
print "percent people without total payments:", float(people - totalPaymentsCount)/float(people)
print "percent POIs without total payments:", float(poiCount - poiTotalPaymentsCount)/float(poiCount)


# import pickle
#
# enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#
# poi_count=0
# salary_count=0
# email_count=0
# count_poi=0
# count_nan=0
# total_missing_payments=0
#
# for k,v in enron_data.items():
#     if v["poi"] == True:
#         poi_count +=1
# print "total number of POIs :", poi_count
# print "total number of fields:", len(enron_data["SKILLING JEFFREY K"])
# print "total value of James Prentice's stock:", enron_data["PRENTICE JAMES"]["total_stock_value"]
# print "total number of emails from Wesley Colwell to POIs:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
# print "value of stock options for Jeffrey K Skilling:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
# print "total payments for Jeffrey K Skilling:", enron_data["SKILLING JEFFREY K"]["total_payments"]
# print "total payments for Kenneth Lay       :", enron_data["LAY KENNETH L"]["total_payments"]
# print "total payments for Andrew Fastow     :", enron_data["FASTOW ANDREW S"]["total_payments"]
#
# for person in enron_data:
#     if enron_data[person]['salary'] != 'NaN':
#         salary_count +=1
# print "total number of employees with salary entry  :", salary_count
#
# for email in enron_data:
#     if enron_data[email]['email_address'] != 'NaN':
#         email_count +=1
# print "total number of employees with email addresses  :", email_count
#
# for missing_payments in enron_data:
#     if enron_data[missing_payments]['total_payments'] == 'NaN':
#         total_missing_payments +=1
# print "total number of employees without total payments listed  :", total_missing_payments
# print "percentage of employees without payment info :", float(total_missing_payments) / len(enron_data)
#
# for missing_payments2 in enron_data:
#     if enron_data[missing_payments2]['poi'] == True:
#         count_poi += 1
#         if enron_data[missing_payments2]['total_payments'] == "NaN":
#             count_nan += 1
# print "total number of POIs with missing total payments :", count_poi
# print "percentage of POIs compared to entire listed :", float(count_poi)/(poi_count)

# name_data = open("../final_project/poi_names.txt", "r")
# poi_count=0
# for person_interest in enron_data:
#     if enron_data[person_interest]['poi']
#     count +=1
# print "poi names:", count
