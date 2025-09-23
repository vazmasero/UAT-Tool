import os

exclude_dirs = {".venv", "__pycache__", ".git", "docs"}


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        level = root.replace(startpath, "").count(os.sep)
        indent = " " * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = " " * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")


with open("estructura.txt", "w") as f:
    import sys

    sys.stdout = f
    list_files(".")
