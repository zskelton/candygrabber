# IMPORTS
import urllib.request
import smtplib
import ssl
import re

# FUNCTIONS
def send_mail(content):
  # Variables
  port = 465
  server = "mailserver"
  user = "sender@sencer.com"
  pasw = "emailpasswd"
  to = "email@email.com"
  subject = "subjectline"
  if content:
    body = "Subject: Good News!\n\nThe licorice half and halfs are now avaiable!"
  else:
    body = "Subject: Sorry, not yet...\n\nThe licorice half and halfs are not avaiable!"
  # Do It!
  try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(server, port, context=context) as server:
      server.login(user, pasw)
      server.sendmail(user, to, body)
      server.quit()
  except Exception as e:
    print("Error: Could not send mail.")
    exit(1)

def check_new(content):
  # Variables
  reg = re.findall(r"<button.*name=\"add\".*<span>.*(Sold out).*<\/span>.*<\/button>", content, re.M | re.I | re.S)
  print(reg)
  # Do It!
  try:
    if reg and reg[0] == "Sold out":
      return False
    else:
      return True
  except:
    print("Error: Could not parse webpage")
    exit(1)

def get_webpage():
  # Variables
  url = "https://licorice.com/products/half-n-half"
  # Do It!
  try:
    content = urllib.request.urlopen(url).read().decode('utf-8')
    return content
  except urllib.error.URLError as e:
    print("Error: Could not open URL" + e)
    exit(1)

# MAIN
def main():
  content = get_webpage()
  result = check_new(content)
  if (result):
    print ("true")
  else:
    print ("false")
  # send_mail(result)
  exit(0)

# RUN
if __name__ == '__main__':
    main()
