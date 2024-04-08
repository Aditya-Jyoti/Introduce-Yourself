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
    with open(introduction_file, "r") as file:
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
    else:
        print("Error: Introduction file does not follow the specified pattern.")
        sys.exit(1)


def validate_pr(directory="."):
    introductions_folder = os.listdir("src/content/introductions")

    for folder in introductions_folder:
        introduction_md_path = f"src/content/introductions/{folder}/introduction.md"
        if os.path.exists(introduction_md_path):
            print(
                f"Success: '{folder}' folder was added in 'src/content/introductions' and contains 'introduction.md'."
            )
            check_introduction_file(introduction_md_path)
        else:
            print(
                f"Error: '{folder}' folder was added in 'src/content/introductions' but does not contain 'introduction.md'."
            )
            sys.exit(0)


if __name__ == "__main__":
    validate_pr()
