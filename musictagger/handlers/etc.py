
def check(filename):
    new_filename = filename

    new_filename = check_backquote(new_filename)

    return new_filename


def check_backquote(filename):
    if "Â´" in filename:
        print("Replaced invalid backquote character with quote character")
        return filename.replace("Â´", "'")
    return filename
