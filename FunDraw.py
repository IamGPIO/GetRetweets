import time
import random
import sys
from colorama import init, Fore, Style  # Import colorama library

# Function to display ASCII art
def display_ascii_art():
    ascii_art = """


                   (                 *                                        
  *   )   )        )\ )    (       (  `                              (     (  
` )  /(( /(   (   (()/(    )\      )\))(  (       (        (  (      )\    )\ 
 ( )(_))\()) ))\   /(_))( ((_)(   ((_)()\ )\  (   )\  (    )\))(   (((_)  ((_)
(_(_()((_)\ /((_) (_))  )\ _  )\  (_()((_((_) )\ ((_) )\ )((_))\   )\___  )\  
|_   _| |(_(_))   / __|((_| |((_) |  \/  |(_)_(_/((_)_(_/( (()(_) ((/ __|((_) 
  | | | ' \/ -_)  \__ / _ | / _ \ | |\/| || | ' \)| | ' \)/ _` |   | (__/ _ \ 
  |_| |_||_\___|  |___\___|_\___/ |_|  |_||_|_||_||_|_||_|\__, |    \___\___/ 
                                                          |___/                        
                                                  
    """
    bright_orange = Fore.LIGHTRED_EX + Style.BRIGHT
    reset = Style.RESET_ALL
    print(bright_orange + ascii_art + reset)

def load_users(file_path):
    users = []
    max_length = 0
    with open(file_path, 'r') as file:
        for line in file:
            user = line.strip()
            users.append(user)
            max_length = max(max_length, len(user))
            time.sleep(0.05)  # Add a delay of 0.005 seconds between loading each user
            print(user)  # Print each user on a separate line
    return users, max_length

def select_random_user(users, max_length):
    input("Press Enter to select a winner...\n")
    print(Fore.YELLOW + "Rolling through random names for some extra suspense.")
    start_time = time.time()
    while time.time() - start_time < 7:  # Scroll through random names for 7 seconds
        random_user = random.choice(users)
        padded_user = random_user.ljust(max_length)  # Pad the username with spaces to ensure consistent width
        sys.stdout.write("\r" + padded_user)
        sys.stdout.flush()
        time.sleep(0.1)  # Adjust the speed of scrolling here
    sys.stdout.write("\r" + " " * max_length)  # Clear the line
    sys.stdout.flush()
    print("\n\n" + Fore.WHITE + "And the winner" + Style.RESET_ALL + " is...")  # Print "And the" in white and "winner" in yellow
    time.sleep(3)  # Wait for 3 seconds before displaying the winner
    winner = random.choice(users)
    print(Fore.WHITE + Style.BRIGHT + f"Winner: {winner}" + Style.RESET_ALL)  # Print the winner in bright white

def main():
    init()  # Initialize colorama
    display_ascii_art()  # Display ASCII art
    input("Press Enter to continue...\n")  # Wait for user to press Enter before continuing
    
    print("\nWelcome to the TheSoloMiningCo's Janko Program written for the Bitaxe + BitHalo Draw!\n")
    time.sleep(1)  # Wait for 3 sec
    print("This program will select a random winner from all the users who retweeted the 'BitHalo Giveaway' tweet.")
    input("Let's Go....!\n")  # Wait for user to press Enter before continuing
    time.sleep(1)  # Wait for 3 sec
    
    file_path = r"C:\Users\Duncan\Desktop\Get Retweets\Users.txt"
    users, max_length = load_users(file_path)
    
    print(Fore.GREEN + f"\n{len(users)} usernames loaded.\n" + Style.RESET_ALL)  # Print "X Usernames Loaded" in green
    print("Let's select a winner!\n")  # Add a space after printing the "Let's select a winner" message
    
    select_random_user(users, max_length)

    time.sleep(1) # Wait for 3 seconds before displaying the winner
    print("\nThanks for Liking, Following and Retweeting the post on the BitHalo, as designed by myself, IamGPIO.")

    # Keep the program running without closing
    while True:
        pass

if __name__ == "__main__":
    main()
