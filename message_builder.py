# personalised email
def personalised_email(template,contact):
    personalised_mess = template.replace("{name}", contact["Name"])
    return personalised_mess