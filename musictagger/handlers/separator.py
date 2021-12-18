import re


def check(filename, empty_sep_mode):
    """
    Ensures the numbering and title are separated from each other with a dash and not with a dot or not separated at all.
    This assumes numbering is already done, as numbering handler is called before this.
    Setting empty_sep_mode to True makes separators be no characters.
    """

    if not empty_sep_mode:
        if check_correct_dash(filename):
            return filename
    else:
        if check_correct_empty(filename):
            return filename

    new_filename = filename

    new_filename = check_dash(new_filename, empty_sep_mode)
    new_filename = check_empty(new_filename, empty_sep_mode)
    new_filename = check_dot(new_filename, empty_sep_mode)
    new_filename = check_space(new_filename, empty_sep_mode)

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


dash_pattern = re.compile(r"\d\d - .*")
empty_pattern = re.compile(r"^(\d\d[^\d. -].*)|(\d\d \d.*)$")
dot_pattern = re.compile(r"\d\d\. .*")
space_pattern = re.compile(r"\d\d [^-]+")


# checks if separator is correct already
def check_correct_dash(filename):
    # check if it already uses dash separators, if so then end function
    if dash_pattern.match(filename):
        print("Separator is valid")
        return True
    return False


def make_empty_sep(trackno, trackname):
    return trackno + (" " if (trackname[0].isdigit()) else "") + trackname


def make_dash_sep(trackno, trackname):
    trackno + " - " + trackname


def check_dash(filename, empty_sep_mode):
    if empty_sep_mode and dash_pattern.match(filename):
        print("Separator is a dash, replacing with an empty separator")
        trackno = filename[0:2]
        trackname: str = filename[5:]
        return make_empty_sep(trackno, trackname)
    return filename


def check_correct_empty(filename):
    if empty_pattern.match(filename):
        print("Separator is valid")
        return True
    return False


# "12Name.flac" or "12 22.flac"
def check_empty(filename: str, empty_sep_mode):
    if not empty_sep_mode and empty_pattern.match(filename):
        print("Empty separator, replacing with a dash")
        trackno = filename[0:2]
        trackname = filename[2:].lstrip()
        return trackno + " - " + trackname
    return filename


# check if filename uses dots (i.e. "12. Title.flac")
def check_dot(filename, empty_sep_mode):
    if dot_pattern.match(filename):
        print("Separator is a dot")
        trackno = filename[0:2]
        trackname = filename[4:]
        return make_dash_sep(trackno, trackname) if not empty_sep_mode else make_empty_sep(trackno, trackname)
    return filename


# check if filename uses a single space
def check_space(filename, empty_sep_mode):
    if space_pattern.match(filename):
        print("Single space separator")
        trackno = filename[0:2]
        trackname = filename[3:]
        return make_dash_sep(trackno, trackname) if not empty_sep_mode else make_empty_sep(trackno, trackname)
    return filename
