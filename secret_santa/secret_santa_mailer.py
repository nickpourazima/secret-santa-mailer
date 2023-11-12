import base64
import json
import os
import random
from email.message import EmailMessage
import smtplib

class SecretSantaMailer:
    def __init__(self, sender_json, participants_json):
        with open(sender_json, 'r') as sender_file:
            sender_info = json.load(sender_file)

        self.sender_email = sender_info[0]["sender_email"]
        self.google_form_link = sender_info[0]["google_form"]
        self.app_password = sender_info[0]["app_password"]

        with open(participants_json, 'r') as json_file:
            self.participant_data = json.load(json_file)

    def send_email(self, recipient_email, subject, message_body):
        try:
            # Create an SMTP_SSL instance with the Gmail SMTP server
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

            # Log in using your Gmail username and app password
            smtp_server.login(self.sender_email, self.app_password)

            # Create the EmailMessage
            message = EmailMessage()
            message.set_content(message_body)
            message["To"] = recipient_email
            message["From"] = self.sender_email
            message["Subject"] = subject

            # Send the email
            smtp_server.send_message(message)

            print(f'Message sent to {recipient_email}.')
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Quit the SMTP server
            smtp_server.quit()

    def generate_and_send_assignments(self):
        random.shuffle(self.participant_data)
        assigned_recipients = set()
        participant_assignments = []

        for giver in self.participant_data:
            recipient = random.choice(self.participant_data)

            # Ensure the recipient is not from the same group as the giver
            while recipient['group'] == giver['group'] or recipient['name'] in assigned_recipients:
                recipient = random.choice(self.participant_data)

            assigned_recipients.add(recipient['name'])

            subject = 'Official Secret Santa Gift Exchange Assignment'
            message_body = f"Hello {giver['name']},\n\nIt's that special time of year, and you've been chosen as this year's Secret Santa! Your mission is to bring joy and surprises to a loved one. Your assigned recipient is {recipient['name']}.\n\n"
            message_body += f"To make this holiday even more magical, please take a moment to fill out our Secret Santa Gift Preference Form:\n{self.google_form_link}\n\n"
            message_body += "Let the festive fun begin!\n\nWarm wishes,\nYour Secret Santa Organizer"

            # Send the email to the giver
            if giver['email']:
                self.send_email(giver['email'], subject, message_body)
            else:
                print(f"No valid email found for {giver['name']}.")

            participant_assignments.append({
                "Giver": giver['name'],
                "Recipient": recipient['name']
            })

        # Uncomment to save the participant assignments to a JSON file
        with open('participant_assignments.json', 'w') as output_file:
            json.dump(participant_assignments, output_file, indent=4)

if __name__ == "__main__":
    mailer = SecretSantaMailer('sender.json', 'participants.json')
    mailer.generate_and_send_assignments()
