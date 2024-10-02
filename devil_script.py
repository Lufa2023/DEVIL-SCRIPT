import os
import time

# Clear the terminal
os.system('clear')

# Updated ASCII Art for the title
banner = """
\e[1;31m
·············································
:  ____  _     _ _     _       _           :
: / ___|| |__ (_) | __| | ___ | |_         :
: \___ \| '_ \| | |/ _` |/ _ \| __|        :
:  ___) | | | | | | (_| | (_) | |_         :
: |____/|_| |_|_|_|\__,_|\___/ \__|        :
:               By \e[1mXXX LUFA\e[0m         :
·············································
\e[0m
"""
print(banner)

# Get target phone number
print("\n\e[1;36m[?] Target : \e[0m", end="")
phone_number = input()

# Simulate steps with messages
steps = [
    "\e[1;33m[#] Scanning {phone_number}\e[0m",
    "\e[1;33m[#] Exploiting To {phone_number}\e[0m",
    "\e[1;33m[#] Bypass Verify WhatsApp\e[0m",
    "\e[1;32m[#] Success Bypass\e[0m",
    "\e[1;33m[#] Get Verify Code\e[0m",
]

for step in steps:
    print(step.format(phone_number=phone_number))
    time.sleep(2)

# Set the verification code
verify_code = "65568"  # Fixed verification code
print(f"\n\e[1;32m[#] Verify Code : {verify_code}\e[0m")
time.sleep(1)

print("\n\e[1;31m~/CamPhish/HxWhatsApp\e[0m $ ", end="")
