from csv_reader import read_contact
from template_loader import load_template
from message_builder import personalised_email
from email_sender import send_email

    
def main():
    list_contacts = read_contact()
    template = load_template()

    for contact in list_contacts:
        message = personalised_email(template, contact)
        success = send_email(contact,message)

        if success:
            print(f"✅ Email sent to {contact['Email']}")
        else:
            print(f"❌ Email failed for {contact['Email']}")

if __name__ == "__main__":
    main()