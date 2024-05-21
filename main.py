import email_work


def main():
    recipients = ['dduckker@ukr.net']
    mail_body = 'Text from Odesa'
    mail_subject = "Hello"
    attachment = 'bug_fix.py'

    email_work.send_mail(
        recipients=recipients,
        mail_body=mail_body,
        mail_subject=mail_subject,
        attachment='bug_fix.py'
    )


if __name__ == '__main__':
    main()
