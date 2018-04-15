#!/usr/bin/env python
"""EmailServer class

Establish SMTP server and send emails.
"""
__author__ = 'Tony(Yizhen) Chen'
__version__ = '0.1.0'
__email__ = 'tony@sharedcare.io'

from __future__ import print_function

import smtplib
from smtplib import SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailServer(object):
    """Establish SMTP server and send emails.
    
    The server address is the SMTP server address.
    Most of SMTP servers have authentication methods.
    It may fail to reach SMTP servers 
    if you are using two-factor authentication.

    Attributes:
        from_addr: A string indicates the sender of email
        to_addr: A string indicates the receiver of email
        mail_content: A dictionary indicates message content to send 
                    including subject and body
        SMTP_server: A dictionary indicates address and port of 
                    the smtp server
        userid: A string represents user authentication id of 
                the SMTP server 
        psw: A string represents user authentication password of 
            the SMTP server
    """
    def __init__(self, from_addr, to_addr, mail_content, SMTP_server, userid, psw):
        """Inits PeriodicTask class with given parameters"""
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = mail_content['subject']
        self.body = mail_content['body']
        self.server = SMTP_server['address']
        self.port = SMTP_server['port']
        self.userid = userid
        self.password = psw

    def build_msg(self):
        """Builds the message in specific format"""
        msg = MIMEMultipart()
        msg['From'] = self.from_addr
        msg['To'] = self.to_addr
        msg['Subject'] = self.subject
        msg_body = self.body
        msg.attach(MIMEText(msg_body, 'plain'))
        return msg.as_string()

    def send_email(self):
        """Establishs the SMTP server and sends the email"""
        server = smtplib.SMTP(self.server, self.port)
        server.ehlo()
        server.starttls()
        msg = self.build_msg()
        try:
            server.login(self.from_addr, self.password)
            server.sendmail(self.from_addr, self.to_addr, msg)
            print('Successfully sent email')
        except SMTPException:
            print('Unable to send email')
        finally:
            server.close()

