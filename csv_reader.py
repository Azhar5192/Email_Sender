## read the csv file and print names and email
import csv

def read_contact():
    contacts = []
    with open("Name_Email.csv") as f:
        reader = csv.DictReader(f)
        for contact in reader:
            contacts.append(contact)
    return contacts