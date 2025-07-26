import os
def write_python_file(file_name, content):
    try:
        with open(file_name, "w") as file:
            file.write(content)
        return file_name
    except Exception as e:
        print(f"Error writing description file {file_name}: {e}")

def write_description_file(file_name, description, name):
    try:
        with open(file_name, "w") as file:
            file.write(name + "\n\n")
            file.write(description)
        return file_name
    except Exception as e:
        print(f"Error writing description file {file_name}: {e}")

def create_directory(directory_name):
    try:
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
    except OSError as e:
        print(f"Error creating directory {directory_name}: {e}")

def regroup_fils_by_name(file, directory):
    """
    Regroup the files of current directory that have a same name (split by extension)
    in the directory that have a same name.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    if os.path.isfile(file):
        os.rename(file, os.path.join(directory, file))
    else:
        print(f"{file} is not a file.")