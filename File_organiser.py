import os
import shutil

# Pretty Terminal Header Design
import time

def display_banner():
    print("\033[96m=\033[00m" * 60)
    
    print(" " * 18 + "\033[96mFILE ORGANIZER\033[00m")
    
    print("\033[96m=\033[00m" * 60)
    
    print("\033[96mDeveloped by: Sawa Abraham Olanrewaju\033[00m")
    
    print("\033[96m=\033[00m" * 60)
    
    print("\033[96m\nWelcome to the File Organizer Script!\033[00m")
    
    print("\033[96mThis program organizes your files into categorized folders.\n\033[00m")
    
    print("\033[96mCategories: Images, Videos, Documents, Music, Compressed, Uncategorized\n\033[00m")
    
    print("\033[96m=\033[00m" * 60)
    
    time.sleep(1)
    

# Call the banner function at the start of your script
display_banner()

while True:
	try:

		# Define source and destination paths
		path = input('\033[92mEnter path of unordered files:\033[00m' )
		
		destination = input('\033[92mEnter path of the destination:\033[00m ')
		
		# Define categories and their extensions
		categories = {
		    "Images": [".jpg", ".jpeg", ".png", ".gif"],
		    "Videos": [".mp4", ".avi", ".mov"],
		    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
		    "Music": [".mp3", ".wav"],
		    "Compressed": [".zip", ".rar", ".7z"],
		}
		
		if os.path.exists(path)==True:
			break 
		else:
			print('\033[91minvalid path! try again\033[00m')
		
	except Exception as e:
		
		print('Error: ',e)
		continue 
	
# Ensure destination folders exist
for category in categories.keys():
    category_path = os.path.join(destination, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

# Organize files
for file_name in os.listdir(path):
    file_path = os.path.join(path, file_name)

    # Skip if it's a directory
    if os.path.isdir(file_path):
        continue

    # Identify file category
    moved = False
    for category, extensions in categories.items():
        if file_name.lower().endswith(tuple(extensions)):
            dst_path = os.path.join(destination, category, file_name)
            shutil.move(file_path, dst_path)
            
            print(f"\033[93mMoved: {file_path} -> {dst_path}\033[00m")
            moved = True
            break

    # For uncategorized files
    if not moved:
        uncategorized_folder = os.path.join(destination, "Uncategorized")
        
        if not os.path.exists(uncategorized_folder):
        	os.makedirs(uncategorized_folder)
        	dst_path = os.path.join(uncategorized_folder, file_name)
        	shutil.move(file_path, dst_path)
        	print(f"\033[93mMoved to Uncategorized: {file_path} -> {dst_path}\033[00m")