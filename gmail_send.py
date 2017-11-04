import smtplib
from email.mime.text import MIMEText
import sys, csv
from time import sleep


class Mailer:
    """This class for sending Gmail """

    def __init__(self, addr_to, subject, body):
        self.password = " "  # Login password
        self.addr_from = " "  # Mail address
        self.addr_to = addr_to
        self.charset = "ISO-2022-JP"
        self.subject = subject
        self.body = body

    def send(self):
        # Mail setting
        msg = MIMEText(self.body.encode(self.charset), 'plain', self.charset)
        msg['Subject'] = self.subject
        msg['From'] = self.addr_from
        msg['To'] = self.addr_to
        # Send email using SMTP
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(self.addr_from, self.password)
        smtp.send_message(msg)
        smtp.close()


def create_mail_body(name):
    body = """
{}


""".format(name)

    return body


def main():
    # Get file name from argument
    filename = sys.argv[1]

    # Read csv file
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        # Skip header
        header = next(reader)

        for row in reader:
            name = row[0]  # name
            email = row[1]  # mail address

            # The content of the mail
            addr_to = email
            subject = "subject"
            body = create_mail_body(name)
            mailer = Mailer(addr_to, subject, body)
            mailer.send()
            sleep(1)


if __name__ == "__main__":
    main()
