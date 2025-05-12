"""
This script reiniatilizes this repository by removing exsiting files and create new project files.
"""
import toml
import os




if __name__ == "__main__":
    project_name = input("Enter project name: ")
    author_name = input("Enter author name: ")
    author_email = input("Enter author email: ")
    overwrite = input("Overwrite existing files? (y/n): ")

    pyproject_file = os.path.join(os.path.dirname(__file__), "pyproject.toml")
    with open(pyproject_file, "r") as file:
        pyproject = toml.load(file)
    pyproject["project"]["name"] = project_name
    pyproject["project"]["author"] = author_name
    pyproject["project"]["email"] = author_email

    pyproject["project"]["dependencies"] = []
    pyproject["tool"]["setuptools"]["packages"]["find"]["include"] = [f"{project_name}*"]
    pyproject["tool"]["setuptools"]["packages"]["find"]["exclude"] = ["tests*"]
    

    if overwrite.lower() == "n":
        print("Current project settings:")
        print(toml.dumps(pyproject))
        print("\nExiting without overwriting files.")
        exit()

    with open(pyproject_file, "w") as file:
        toml.dump(pyproject, file)

    src_dir = os.path.join(os.path.dirname(__file__), "src")   
    os.rename(os.path.join(src_dir, "example_package"), os.path.join(src_dir, project_name))
    os.chdir(os.path.join(src_dir, project_name))
    files_to_remove = ["counts.py", "plotting.py"]
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)
            print(f"Removed {file}")
        else:
            print(f"{file} does not exist")
    
    test_dir = os.path.join(os.path.dirname(__file__), "test")
    files_to_remove = ["test_counts.py", "test.txt"]
    for file in files_to_remove:
        if os.path.exists(os.path.join(test_dir, file)):
            os.remove(os.path.join(test_dir, file))
            print(f"Removed {file}")
        else:
            print(f"{file} does not exist")

