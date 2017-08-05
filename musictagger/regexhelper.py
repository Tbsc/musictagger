from musictagger import util


# general method for formatting feats in filename
# filename is obvious
# match is the return of match()ing or search()ing with a pattern
# feats_start is after how many characters does the actual feats list start
# feats_end is an optional argument for ending feats list before end of string
def format_feats(filename, match, feats_start, feats_end=None):
    feats_preformatted = match.string[match.start(0):match.end(0)]
    if feats_end is None:
        feats = feats_preformatted[feats_start:]
    else:
        feats = feats_preformatted[feats_start:feats_end]
    feats_formatted = "(feat. " + feats + ")"
    filename_nofeats = match.string[:match.start(0)]
    # taking only the filename without feats also removes extension, so re-add it manually
    ext = util.get_extension(filename)
    return filename_nofeats + feats_formatted + ext