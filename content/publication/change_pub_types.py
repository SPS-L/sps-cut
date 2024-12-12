import os

def update_publication_types(file_path):
    # Define replacements as a dictionary
    replacements = {
        'publication_types = ["1"]': 'publication_types = ["paper-conference"]',
        'publication_types = ["2"]': 'publication_types = ["article-journal"]',
        'publication_types = ["4"]': 'publication_types = ["report"]',
        'publication_types = ["6"]': 'publication_types = ["chapter"]',
        'publication_types = ["7"]': 'publication_types = ["thesis"]',
    }

    # Read and update the file content
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Replace the lines based on the dictionary
    with open(file_path, 'w') as file:
        for line in lines:
            updated_line = line
            for old, new in replacements.items():
                if old in line:
                    updated_line = line.replace(old, new)
                    break  # No need to check other replacements
            file.write(updated_line)

def process_subdirectories():
    # Get the current directory
    current_dir = os.getcwd()

    # Iterate through all subdirectories in the current directory
    for root, dirs, files in os.walk(current_dir):
        for directory in dirs:
            index_md_path = os.path.join(root, directory, 'index.md')
            # Check if index.md exists in the subdirectory
            if os.path.isfile(index_md_path):
                print(f"Updating {index_md_path}...")
                update_publication_types(index_md_path)

if __name__ == "__main__":
    process_subdirectories()
    print("All updates completed.")
