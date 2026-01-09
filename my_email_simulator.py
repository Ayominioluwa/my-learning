import datetime
class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()
    def send_email(self, receiver, title, body):
        email = Email(sender=self, receiver=receiver, title=title, body=body)
        receiver.inbox.receive_email(email)
        print(f"\nEmail sent from {self.name} to {receiver.name} successfully!")
    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.check_inbox()
    def read_email(self, index):
        self.inbox.read_email(index)
    def delete_email(self, index):
        self.inbox.delete_email(index)
class Email:
    def __init__(self, sender, receiver, title, body):
        self.sender = sender
        self.receiver = receiver
        self.title = title
        self.body = body
        self.read = False
        self.timestamp = datetime.datetime.now()
    def mark_as_read(self):
        self.read = True
    def __str__(self):
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] | From: {self.sender.name} | Title: {self.title} | Time: {self.timestamp.strftime('%H:%M')}"

class Inbox:
    def __init__(self):
        self.emails = []
    def receive_email(self, email):
        self.emails.append(email)
    def check_inbox(self):
        if not self.emails:
            print("Inbox is empty")
            return
        print("\nYour Emails:")
        for i, email in enumerate(self.emails, 1):
            print(f"{i}. {email}")
            return
    def read_email(self, index):
        if not self.emails:
            print("Inbox is empty")
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print("Invalid index!")
            return
        email = self.emails[actual_index]
        print("\n--- Email ---")
        print(f"From: {email.sender.name}")
        print(f"Received: {email.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f"Title: {email.title}")
        print(f"Body:\n{email.body}")
        print("------------\n")
        email.mark_as_read()
    def delete_email(self, index):
        if not self.emails:
            print("Inbox is empty")
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print("Invalid index!")
            return
        del self.emails[actual_index]
        print("Email successfully deleted!")