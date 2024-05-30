import os


def run_tool(tool_name):
    tool_paths = {
        '1': 'AWSAccessKeyIDDecoder/main.py',
        '2': 'AWSBucketChecker/main.py',
        '3': 'GuardDutyConfigurationManipulator/main.py',
        '4': 'SubNSFinder/main.py'
    }

    if tool_name in tool_paths:
        os.system(f'python {tool_paths[tool_name]}')
    else:
        print("Invalid option, please try again.")


def main():
    while True:
        print(r""" ________  ___       ________  ___  ___  ________          _________  ________  ________ _________  ___  ________          
|\   ____\|\  \     |\   __  \|\  \|\  \|\   ___ \        |\___   ___\\   __  \|\   ____\\___   ___\\  \|\   ____\      
\ \  \___|\ \  \    \ \  \|\  \ \  \\\  \ \  \_|\ \       \|___ \  \_\ \  \|\  \ \  \___\|___ \  \_\ \  \ \  \___|      
 \ \  \    \ \  \    \ \  \\\  \ \  \\\  \ \  \ \\ \           \ \  \ \ \   __  \ \  \       \ \  \ \ \  \ \  \         
  \ \  \____\ \  \____\ \  \\\  \ \  \\\  \ \  \_\\ \           \ \  \ \ \  \ \  \ \  \____   \ \  \ \ \  \ \  \____    
   \ \_______\ \_______\ \_______\ \_______\ \_______\           \ \__\ \ \__\ \__\ \_______\  \ \__\ \ \__\ \_______\  
    \|_______|\|_______|\|_______|\|_______|\|_______|            \|__|  \|__|\|__|\|_______|   \|__|  \|__|\|_______|  
                                                                                                                        
                                                                                                                                                                    
    ________  ________   ________  ___           ___    ___ ________  _______   ________   
    |\   __  \|\   ___  \|\   __  \|\  \         |\  \  /  /|\_____  \|\  ___ \ |\   __  \    
    \ \  \|\  \ \  \\ \  \ \  \|\  \ \  \        \ \  \/  / /\|___/  /\ \   __/|\ \  \|\  \   
     \ \   __  \ \  \\ \  \ \   __  \ \  \        \ \    / /     /  / /\ \  \_|/_\ \   _  _\  
      \ \  \ \  \ \  \\ \  \ \  \ \  \ \  \____    \/  /  /     /  /_/__\ \  \_|\ \ \  \\  \| 
       \ \__\ \__\ \__\\ \__\ \__\ \__\ \_______\__/  / /      |\________\ \_______\ \__\\ _\ 
        \|__|\|__|\|__| \|__|\|__|\|__|\|_______|\___/ /        \|_______|\|_______|\|__|\|__|
                                                \|___|/                                       """)
        print("Welcome to Cloud Tactic Analyzer!\n")
        print("Please select the tool you want to run:")
        print("1. AWSAccessKeyIDDecoder")
        print("2. AWSBucketChecker")
        print("3. GuardDutyConfigurationManipulator")
        print("4. SubNSFinder")
        print("5. Exit\n")

        choice = input("Your choice: ")

        if choice == '5':
            print("Exiting...")
            break

        run_tool(choice)

        while True:
            print("\nTool has finished running.\n")
            print("1. Return to Main Menu")
            print("2. Exit\n")

            post_choice = input("Your choice: ")

            if post_choice == '1':
                break
            elif post_choice == '2':
                print("\nExiting...")
                return
            else:
                print("Invalid option, please try again.")


if __name__ == '__main__':
    main()
