import os
import pathlib
import shutil

# Dictionary containing file formats and their corresponding folder names
fileFormat = {
    "Web": [".html5", ".html", ".htm", ".xhtml"],
    "Picture": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", ".heif", ".psd"],
    "Video": [".avi", ".mkv", "..flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    "Document": [".oxps", ".epub", ".pages", ".docx", ".txt", ".pdf", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", "docn", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Compressed": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
}

# Extract folder names and file extensions from the fileFormat dictionary
folders_name_list = list(fileFormat.keys())
file_extension_list = list(fileFormat.values())

# Print the lists for reference
print(file_extension_list)
print(folders_name_list)

# Iterate over files in the current directory
for file in os.scandir():
    # Get file name and extension
    fileName = pathlib.Path(file)
    fileFormatType = fileName.suffix.lower()
    
    src = str(fileName)  # Source file path
    dest = "Other"  # Default destination folder
    
    # Skip files without extensions
    if fileFormatType == "":
        print(f"{src} has no file format")
        continue
    
    moved = False  # Flag to track if the file has been moved
    
    # Iterate over the file formats and corresponding folders
    for i, formats in enumerate(file_extension_list):
        if fileFormatType in formats:
            folder = folders_name_list[i]  # Get the corresponding folder
            print(folder)
            
            # Create the folder if it doesn't exist
            if not os.path.isdir(folder):
                os.mkdir(folder)
            dest = folder
            
            # Check if a file with the same name exists in the destination folder
            dest_file = os.path.join(dest, fileName.name)
            if os.path.exists(dest_file):
                # Rename the file being moved
                dest_file = os.path.join(dest, fileName.stem + "_1" + fileName.suffix)
                print(f"A file with the same name already exists. Renaming {fileName.name} to {os.path.basename(dest_file)}")
            
            # Move the file to the destination folder
            shutil.move(src, dest_file)
            moved = True
            break
    
    # If the file format is not found, move it to the 'Other' folder
    if not moved:
        if not os.path.isdir("Other"):
            os.mkdir("Other")
        print(f"{src} moved to {dest}!")
        shutil.move(src, os.path.join(dest, fileName.name))

print("File organizer completed")
input("\nPress enter to EXIT")

