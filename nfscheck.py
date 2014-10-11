#!/usr/bin/python

# Author    :   Yogesh
# Date      :   5th Oct 2014
# Purpose   :   To check existence of a test file on NFS volume

import os
import subprocess
import sys
import smtplib

OUTPUT = "/root/output.log"
File = "/var/log/messages123"
MAILCONTENT = "/root/mailcontent.txt"
mailflag = 0
Result = os.path.isfile(File)

if Result:
        f2 = open(OUTPUT,"a")
        date = subprocess.call(["date", "+%d-%m-%Y %H:%M:%S"], stdout=f2)
        print >> f2, "The file ", File, "exists!"
else:
        f1 = open(MAILCONTENT,"a")
        date = subprocess.call(["date", "+%d-%m-%Y %H:%M:%S"], stdout=f1)
        print >> f1, "The file doens't exists!"
        mailflag = 1

if mailflag == 1:
        #subprocess.call(["mail", "-s 'NFS mount doesn't exists' -v yogesh.vaishnav@opentext.com -f cloudops5w@cordys.com"])
        SERVER = "localhost"
        FROM = "cloudops5w@cordys.com"
        TO = ["yogesh.vaishnav@opentext.com"] # must be a list
        SUBJECT = "NFS mount doesn't exists"
        TEXT = "The file in NFS mount doesn't exists"
        # Prepare actual message
        message = 'Subject: %s\n\n%s' % (SUBJECT, TEXT)
        # Send the mail
        server = smtplib.SMTP(SERVER)
        server.sendmail(FROM, TO, message)
        server.quit()
