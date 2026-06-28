# Task 3: Task Automation with Python - CodeAlpha
# Student ID: CA/DF1/174377
import os
import shutil
import re

def move_jpg_files():
    """Move all .jpg files from one folder to another"""
    source = input("Enter source folder path: ")
    destination = input("Enter destination folder path: ")
    
    # Create destination if it doesn't exist
    if not os.path.exists(destination):
        os.makedirs(destination)
        print(f"Created folder: {destination}")
    
    count = 0
    try:
        for file in os.listdir(source):
            if file.lower().endswith('.jpg'):
                src_path = os.path.join(source, file)
                dst_path = os.path.join(destination, file)
                shutil.move(src_path, dst_path)
                print(f"Moved: {file}")
                count += 1
        print(f"\nTotal {count} .jpg files moved successfully!")
    except Exception as e:
        print(f"Error: {e}")

def extract_emails():
    """Extract all email addresses from a text file"""
    file_path = input("Enter text file path to extract emails from: ")
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Regex pattern for emails
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, content)
        
        if emails:
            print(f"\nFound {len(emails)} email(s):")
            for email in set(emails):  # set() to remove duplicates
                print(f" - {email}")
            
            # Save to file
            with open("extracted_emails.txt", "w") as out:
                for email in set(emails):
                    out.write(email + "\n")
            print("\nEmails saved to 'extracted_emails.txt'")
        else:
            print("No emails found in the file")
            
    except FileNotFoundError:
        print("File not found! Check the path.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("=" * 45)
    print(" CodeAlpha Task 3 - Task Automation")
    print("=" * 45)
    print("1. Move all .jpg files to new folder")
    print("2. Extract email addresses from text file")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice 1/2/3: ")
        
        if choice == '1':
            move_jpg_files()
        elif choice == '2':
            extract_emails()
        elif choice == '3':
            print("Automation complete. Goodbye!")
            break
        else:
            print("Invalid choice. Try 1, 2, or 3")

if __name__ == "__main__":
    main()
