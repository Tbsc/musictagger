import os


def check(filename):
    # get only name without extension to allow checking name without considering image type
    filehead, extension = os.path.splitext(filename)
    if filehead.lower() == "folder":
        print("Renaming to cover" + extension)
        return "cover" + extension

    print("Name is valid")
    return filename
