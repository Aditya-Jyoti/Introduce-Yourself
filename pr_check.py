import os
import sys

def check_pr_added_folders(directory="."):
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
            print(f"Success: '{folder}' folder was added in 'src/content/introductions'.")
    else:
        print("Error: No folders were added in 'src/content/introductions'.")
        sys.exit(1)

if __name__ == "__main__":
    check_pr_added_folders()
