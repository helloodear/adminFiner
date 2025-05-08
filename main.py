import requests
from termcolor import colored

# Banner (using raw string to prevent escape sequence warning)
banner = colored(r"""
  ____  _              ____                      _    
 |  _ \| |            |  _ \                    | |   
 | |_) | |_   _  ___  | |_) | ___ _ __ ___   ___| | __
 |  _ <| | | | |/ _ \ |  _ < / _ \ '_ ` _ \ / _ \ |/ /
 | |_) | | |_| |  __/ | |_) |  __/ | | | | |  __/   < 
 |____/|_|\__,_|\___| |____/ \___|_| |_| |_|\___|_|\_\ V 1
 
 Author : Raj Singh
                                                      
 """, 'cyan')

# Function to perform the directory brute-force attack
def find_login_page(url, dir_file):
    try:
        # Open the file with directories to check
        with open(dir_file, 'r') as file:
            directories = file.readlines()
        
        print(banner)
        print(f"[*] Scanning {url} for login pages...\n")

        # Try each directory from the list in dir.txt
        for dir in directories:
            dir = dir.strip()  # Clean up any whitespace or newline characters
            test_url = f"{url}/{dir}"

            try:
                # Send a GET request to the directory
                response = requests.get(test_url)
                
                # Check for successful response
                if response.status_code == 200:
                    print(colored(f"[+] Found: {test_url}", 'green'))
                else:
                    print(f"[-] {test_url} - Status Code: {response.status_code}")

            except requests.RequestException as e:
                # Handle connection errors or timeouts
                print(f"[!] Error connecting to {test_url}: {str(e)}")

    except FileNotFoundError:
        print(f"[!] Error: The file '{dir_file}' was not found.")
    except Exception as e:
        print(f"[!] An unexpected error occurred: {str(e)}")

# Main function
if __name__ == "__main__":
    try:
        target_url = input("Enter the target URL (e.g. http://example.com): ").strip()
        if not target_url.startswith("http"):
            print("[!] Error: Please enter a valid URL starting with http:// or https://")
        else:
            file_name = "dir.txt"  # Replace with the path to your dir.txt file
            find_login_page(target_url, file_name)
    
    except KeyboardInterrupt:
        print("\n[!] Process interrupted by the user.")
