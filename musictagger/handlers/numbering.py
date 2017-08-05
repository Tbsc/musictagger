import re


# ensure numbering always consists of at least 2 digits, adding zeros if needed
def check(filename):
    # if numbering is correct, return function with current filename
    if check_correct(filename):
        return filename

    new_filename = filename

    # begin checks
    new_filename = check_single_digit(new_filename)

    return new_filename


# checks if numbering is formatted correctly
def check_correct(filename):
    correct_pattern = re.compile("\d\d.*")
    if correct_pattern.match(filename):
        print("Numbering is valid")
        return True
    return False


# check if numbering is only 1 digit
def check_single_digit(filename):
    single_digit_pattern = re.compile("\d.*")
    if single_digit_pattern.match(filename):
        # just append a 0 before the number
        print("Numbering consists of a single digit, prepending a zero")
        return "0" + filename
    return filename
