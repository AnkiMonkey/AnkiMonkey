import os

# Set the path to the folder containing the files
folder_path = r"C:\Users\timon\Downloads\terminologie"

# Change the directory to the folder containing the files
os.chdir(folder_path)

# Loop through all the files in the folder
for filename in os.listdir():
    # Check if the file is a docx, pptx, or txt file
    if filename.endswith(".docx") or filename.endswith(".pptx") or filename.endswith(".txt") or filename.endswith(".pdf"):
        # Split the filename into its base name and extension
        base_name, extension = os.path.splitext(filename)
        # Decapitalize the base name
        new_base_name = base_name.lower()
        # Rename the file with the decapitalized base name and original extension
        os.rename(filename, new_base_name + extension)
print("All file names in the folder have been decapitalized.")

