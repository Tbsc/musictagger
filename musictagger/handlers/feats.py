import re

from musictagger import util
from musictagger import regexhelper


# makes sure that when song has features, feature list starts with "(feat." and ends with ")".
# secondly, it tries to make sure features are separated by commas except the last feature,
# which is separated with an ampersand.
def check(filename):
    if check_correct(filename):
        return filename

    new_filename = filename

    new_filename = check_paranthesesfeat_nodot(new_filename)
    new_filename = check_fdot(new_filename)
    new_filename = check_ftdot(new_filename)
    new_filename = check_bracketsdot(new_filename)
    new_filename = check_brackets(new_filename)
    new_filename = check_bracketsfdot(new_filename)
    new_filename = check_bracketsf(new_filename)
    new_filename = check_featdot(new_filename)
    new_filename = check_feat(new_filename)
    new_filename = check_upperfeatdot(new_filename)

    return new_filename


# checks if feats are already formatted correctly in file, and if so returns true, or false if not.
# unlike other checks, this check IS case sensitive, because only feat in lowercase is valid
def check_correct(filename):
    correct_pattern = re.compile("\(feat\. .*\)")
    if correct_pattern.search(filename):
        print("Features are valid")
        return True
    return False


# check for (feat <feat list>) (ignoring case of feat), essentially adding the dot after feat
def check_paranthesesfeat_nodot(filename):
    nodot_pattern = re.compile("\([fF][eE][aA][tT] .*\)")
    nodot_match = nodot_pattern.search(filename)
    if nodot_match:
        print("Features listed inside (feat ...), changing to (feat. ...)")
        return regexhelper.format_feats(filename, nodot_match, 6, -1)
    return filename


# check for (f. <feat list>) (ignoring case of f.)
def check_fdot(filename):
    fdot_pattern = re.compile("(\([fF]\. .*\))")
    fdot_match = fdot_pattern.search(filename)
    if fdot_match:
        print("Features listed inside (f. ...), changing to (feat. ...)")
        return regexhelper.format_feats(filename, fdot_match, 4, -1)
    return filename


# check for (ft. <feat list>) (ignoring case of ft.)
def check_ftdot(filename):
    ftdot_pattern = re.compile("(\([fF][tT]\. .*\))")
    ftdot_match = ftdot_pattern.search(filename)
    if ftdot_match:
        print("Features listed inside (ft. ...), changing to (feat. ...)")
        return regexhelper.format_feats(filename, ftdot_match, 5, -1)
    return filename


# check for [feat. <feat list>] (ignoring case of feat)
def check_bracketsdot(filename):
    # (?i)(?-i) doesn't work for some reason, so I'm using a character set instead
    bracket_pattern = re.compile("(\[[fF][eE][aA][tT]\. .*\])")
    bracket_match = bracket_pattern.search(filename)
    if bracket_match:
        print("Features listed inside [feat. ...], changing to (feat. ...)")
        return regexhelper.format_feats(filename, bracket_match, 7, -1)
    return filename


# check for [feat <feat list>] (ignoring case of feat)
def check_brackets(filename):
    # (?i)(?-i) doesn't work for some reason, so I'm using a character set instead
    bracket_pattern = re.compile("(\[[fF][eE][aA][tT] .*\])")
    bracket_match = bracket_pattern.search(filename)
    if bracket_match:
        print("Features listed inside [feat ...], changing to (feat. ...)")
        return regexhelper.format_feats(filename, bracket_match, 6, -1)
    return filename


# check for [f. <feat list>] (ignoring case of f.)
def check_bracketsfdot(filename):
    # (?i)(?-i) doesn't work for some reason, so I'm using a character set instead
    bracket_pattern = re.compile("(\[[fF]\. .*\])")
    bracket_match = bracket_pattern.search(filename)
    if bracket_match:
        print("Features listed inside [f. ...], changing to (feat. ...)")
        return regexhelper.format_feats(filename, bracket_match, 4, -1)
    return filename


# check for [f <feat list>] (ignoring case of f)
def check_bracketsf(filename):
    # (?i)(?-i) doesn't work for some reason, so I'm using a character set instead
    bracket_pattern = re.compile("(\[[fF] .*\])")
    bracket_match = bracket_pattern.search(filename)
    if bracket_match:
        print("Features listed inside [f ...], changing to (feat. ...)")
        return regexhelper.format_feats(filename, bracket_match, 3, -1)
    return filename


# check for Feat. <feat list>
def check_featdot(filename):
    # (?i)(?-i) doesn't work for some reason, so I'm using a character set instead
    featdot_pattern = re.compile("(?<!\()([fF][eE][aA][tT]\. )(.*)")
    featdot_match = featdot_pattern.search(filename)
    if featdot_match:
        print("Features listed inside Feat. ..., changing to (feat. ...)")
        return regexhelper.format_feats(filename, featdot_match, 6, -len(util.get_extension(filename)))
    return filename


# check for Feat <feat list>
def check_feat(filename):
    # (?i)(?-i) doesn't work for some reason, so I'm using a character set instead
    feat_pattern = re.compile("(?<!\()([fF][eE][aA][tT] )(.*)")
    feat_match = feat_pattern.search(filename)
    if feat_match:
        print("Features listed inside Feat ..., changing to (feat. ...)")
        return regexhelper.format_feats(filename, feat_match, 6, -len(util.get_extension(filename)))
    return filename


# check for (Feat. <feat list>)
def check_upperfeatdot(filename):
    upperfeatdot_pattern = re.compile("(\(Feat\. (.*)\))")
    upperfeatdot_match = upperfeatdot_pattern.search(filename)
    if upperfeatdot_match:
        print("Features listed inside (Feat. ...), changing to (feat. ...)")
        return regexhelper.format_feats(filename, upperfeatdot_match, 7, -1)
    return filename
