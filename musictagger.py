import os
import sys
from pathlib import Path

from musictagger import util
from musictagger.handlers import feats
from musictagger.handlers import numbering
from musictagger.handlers import separator
from musictagger.handlers import images
from musictagger.handlers import etc


def main():
    # arguments need to be the program itself and path to album dir (optionally new dir name)
    if not 2 <= len(sys.argv) <= 4:
        print("Usage: {} <album dir> [new dir name] [--empty-sep]".format(sys.argv[0]))
        sys.exit(1)

    rel_path_arg = sys.argv[1]
    path = Path(rel_path_arg).resolve()

    if not path.exists() or not path.is_dir():
        print("Invalid album directory, doesn't exist or not a directory")
        sys.exit(2)

    # if new dir name isn't known yet through arguments, prompt user for it
    if len(sys.argv) == 2 or (len(sys.argv) == 3 and sys.argv[2] == "--empty-sep"):
        old_dirname = path.name
        print("Current name: {}".format(old_dirname))
        new_dirname = input("    New name: ")
        if new_dirname == "":
            new_dirname = old_dirname
        new_path = str(path.parent.absolute()) + "/" + new_dirname
    else:
        new_path = os.path.dirname(path) + "/" + sys.argv[2]

    try:
        os.rename(path, new_path)
    except OSError:
        print("Failed renaming directory; make sure new name doesn't contain any of the following: * < > / \\ ? \" : |")
        sys.exit(2)

    path = Path(new_path).resolve()

    empty_sep_mode = False

    # len 3 can be "prog.py albumdir --empty-sep" or "prog.py albumdir newdir"
    if len(sys.argv) == 3 and sys.argv[2] == "--empty-sep":
        print("Set to empty separator mode")
        empty_sep_mode = True

    # len 4 means that only argv[3] could be --empty-sep
    if len(sys.argv) == 4:
        if sys.argv[3] == "--empty-sep":
            print("Set to empty separator mode")
            empty_sep_mode = True
        else:
            print("Invalid fourth argument, ignoring")

    # try to go through all files in directory, and if they don't exist then the loop just doesnt execute
    for file in path.iterdir():
        util.print_divider()
        filename = file.name
        print(filename)

        # make sure we actually need to do something with this file
        if not util.should_handle_file(file):
            print("Skipping")
            continue

        if util.should_delete(file):
            print("Deleting")
            file.unlink()
            continue

        new_filename = filename

        # if music file, work on it
        if util.filecheck_music(file):
            print("Music file")
            print()
            new_filename = numbering.check(new_filename)
            new_filename = separator.check(new_filename, empty_sep_mode)
            new_filename = feats.check(new_filename)
            new_filename = etc.check(new_filename)
        elif util.filecheck_image(file):
            # if image file, work on it
            print("Image file")
            print()
            new_filename = images.check(new_filename)

        print()
        if new_filename != filename:
            # notify user of change in filename
            print("New filename: " + new_filename)
        else:
            # notify user of no change occurring
            print("No change")

        # after checking everything, rename file
        file.rename(file.with_name(new_filename))
    util.print_divider()


if __name__ == "__main__":
    main()
