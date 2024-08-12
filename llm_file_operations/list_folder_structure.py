import os

def list_directory_structure(startpath):
    for root, dirs, files in os.walk(startpath):
        if '.git' in dirs:
            dirs.remove('.git')
        if '.hg' in dirs:
            dirs.remove('.hg')
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{sub_indent}{f}")

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))
    print("Project structure:")
    list_directory_structure(project_root)