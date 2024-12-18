import os

def process_index_md(folder_path):
    # Walk through the folder and subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file == "index.md":
                file_path = os.path.join(root, file)
                process_file(file_path)

def process_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        doivar = None
        new_content = []
        plus_count = 0

        for line in lines:
            if 'doi = "' in line:
                # Extract DOI value
                doivar = line.split('doi = "')[1].split('"')[0]
            
            if line.strip() == "+++":
                plus_count += 1

            new_content.append(line)

            # Stop adding content after the second '+++'
            if plus_count == 2:
                break

        if doivar:
            new_content.append("\n")
            new_content.append("{{< rawhtml >}}\n")
            new_content.append(f'<a href="https://plu.mx/plum/a/?doi={doivar}" class="plumx-details"></a>\n')
            new_content.append("{{< /rawhtml >}}\n")

            with open(file_path, "w", encoding="utf-8") as file:
                file.writelines(new_content)

            print(f"Processed: {file_path}")
        else:
            print(f"DOI not found in: {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder: ").strip()
    process_index_md(folder_path)
