import time

# Clear the terminal screen (this works in most systems)
def clear_screen():
    print("\033[H\033[J", end="")

# Custom ASCII Art Banner for "DEVIL"
def print_banner():
    print("\033[1;31m")  # Red color
    print("  oVo")
    print("  XXX")
    print(" XXXXX")
    print(" XXXXX")
    print("  XXX")
    print("   V")
    print("   DEVIL")
    print("\033[0m")  # Reset color

    # Subtitle
    print("\033[1;36mBY XXX LUFA\033[0m")  # Cyan color

# Main function to simulate the process
def main():
    clear_screen()
    print_banner()

    # Get target phone number
    phone_number = input("\n\033[1;36m[?] Target : \033[0m")

    # Simulate steps with messages
    print(f"\033[1;33m[#] Scanning {phone_number}\033[0m")
    time.sleep(2)

    print(f"\033[1;33m[#] Exploiting To {phone_number}\033[0m")
    time.sleep(3)

    print("\033[1;33m[#] Bypassing WhatsApp Verification\033[0m")
    time.sleep(2)

    print("\033[1;32m[#] Success: Bypass Complete\033[0m")
    time.sleep(1)

    print("\033[1;33m[#] Retrieving Verification Code...\033[0m")
    time.sleep(2)

    # Fixed verification code
    verify_code = "567973"
    print(f"\033[1;32m[#] Verification Code: {verify_code}\033[0m")
    time.sleep(1)

    # Final prompt
    print("\n\033[1;31m~/DEVIL_Script\033[0m $ ")

if __name__ == "__main__":
    main()
