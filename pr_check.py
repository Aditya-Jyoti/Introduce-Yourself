import os
import sys
import re

def check_introduction_file(introduction_file):
    """
    Check if the contents of the introduction.md file follow the specified pattern.

    Args:
        introduction_file (str): Path to the introduction.md file.
    """
    if not os.path.exists(introduction_file):
        print(f"Error: '{introduction_file}' does not exist.")
        sys.exit(1)

    # Read the contents of the introduction.md file
    with open(introduction_file, 'r') as file:
        introduction_content = file.read()

    # Define the pattern to match
    pattern = r"""
        ^---\n           # Start of YAML front matter
        name:\s*(.*?)\n  # Capture group for the name field
        interests:\s*(.*?)\n  # Capture group for the interests field
        description:\s*(.*?)\n  # Capture group for the description field
        github:\s*(.*?)\n  # Capture group for the github field
        image:\s*(.*?)\n  # Capture group for the image field
        ---$            # End of YAML front matter
    """
    # Compile the regex pattern
    regex = re.compile(pattern, re.MULTILINE | re.DOTALL | re.VERBOSE)

    # Match the pattern against the introduction content
    match = regex.match(introduction_content)

    # Check if the pattern matches
    if match:
        print("Success: Introduction file follows the specified pattern.")
        # Extract captured groups for further processing if needed
        name, interests, description, github, image = match.groups()
        print("Name:", name)
        print("Interests:", interests)
        print("Description:", description)
        print("GitHub:", github)
        print("Image:", image)
    else:
        print("Error: Introduction file does not follow the specified pattern.")
        sys.exit(1)

def validate_pr(directory="."):
    introductions_folder = os.path.join(directory, "src", "content", "introductions")

    try:
        before_folders = set(os.listdir(introductions_folder))

        os.system(f'git checkout origin/main -- {introductions_folder}')

        after_folders = set(os.listdir(introductions_folder))
        added_folders = after_folders - before_folders

    except Exception as e:
        print(f"Error: Unable to retrieve folder information: {e}")
        sys.exit(1)

    if added_folders:
        for folder in added_folders:
            folder_path = os.path.join(introductions_folder, folder)
            introduction_md_path = os.path.join(folder_path, "introduction.md")
            if os.path.exists(introduction_md_path):
                print(f"Success: '{folder}' folder was added in 'src/content/introductions' and contains 'introduction.md'.")
                check_introduction_file(introduction_md_path)
            else:
                print(f"Error: '{folder}' folder was added in 'src/content/introductions' but does not contain 'introduction.md'.")
                sys.exit(1)
    else:
        print("Error: No folders were added in 'src/content/introductions'.")
        sys.exit(1)

if __name__ == "__main__":
    validate_pr()
