import re


# ensures the numbering and title are separated from each other with a dash and not with a dot or not separated at all
# this assumes numbering is already done, as numbering handler is called before this
def check(filename):
    if check_correct(filename):
        return filename

    new_filename = filename

    new_filename = check_dot(new_filename)
    new_filename = check_space(new_filename)

    if new_filename == filename:
        print("Separator isn't valid, but no action could be done.")
        print("Do you want to give the file a new name manually?")
        response = input("(Y/N) > ")
        if response.lower() == "y":
            print("Enter new filename, EXCLUDING extension!")
            print("If the song has any features, you don't need to fix them.")
            new_filename = input("Enter new filename, EXCLUDING extension >")
        elif response.lower() == "n":
            print("Skipping separator check for this file.")

    return new_filename


# checks if separator is correct already
def check_correct(filename):
    # check if it already uses dash separators, if so then end function
    dash_pattern = re.compile("\d\d - *")
    if dash_pattern.match(filename):
        print("Separator is valid")
        return True
    return False


# check if filename uses dots (i.e. "12. Title.flac")
def check_dot(filename):
    dot_pattern = re.compile("\d\d\. *")
    if dot_pattern.match(filename):
        print("Separator is a dot, replacing with a dash")
        trackno = filename[0] + filename[1]
        trackname = filename[3:]
        return trackno + " -" + trackname
    return filename


# check if filename uses a single space
def check_space(filename):
    space_pattern = re.compile("\d\d .*")
    if space_pattern.match(filename):
        print("No separator, inserting a dash")
        trackno = filename[0] + filename[1]
        trackname = filename[2:]
        return trackno + " -" + trackname
    return filename
