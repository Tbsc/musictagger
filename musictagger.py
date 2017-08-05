import os
import sys

from musictagger import util
from musictagger.handlers import feats
from musictagger.handlers import numbering
from musictagger.handlers import separator
from musictagger.handlers import images


def main():
    # arguments need to be the program itself and path to album dir (optionally new dir name)
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Usage: {} <album dir> [new dir name]".format(sys.argv[0]))
        sys.exit(1)

    path = sys.argv[1]

    if not os.path.isdir(path):
        print("Invalid path")
        sys.exit(2)

    # if new dir name isn't known yet through arguments, prompt user for it
    if len(sys.argv) == 2:
        print("Current name: {}".format(os.path.basename(path)))
        new_dirname = input("    New name: ")
        new_path = new_dirname
    else:
        new_path = sys.argv[2]

    try:
        os.rename(path, new_path)
    except OSError:
        print("Failed renaming directory; make sure new name doesn't contain any of the following: * < > / \\ ? \" : |")
        sys.exit(2)

    # try to go through all files in directory, and if they don't exist then the loop just doesnt execute
    for filename in os.listdir(new_path):
        util.print_divider()
        print(filename)

        # make sure we actually need to do something with this file
        if not util.should_handle_file(filename):
            print("Skipping")
            continue

        if util.should_delete(filename):
            print("Deleting")
            os.remove(util.append_path(new_path, filename))

        new_filename = filename

        # if music file, work on it
        if util.filecheck_music(filename):
            print("Music file")
            print()
            new_filename = numbering.check(new_filename)
            new_filename = separator.check(new_filename)
            new_filename = feats.check(new_filename)
        elif util.filecheck_image(filename):
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
        os.rename(util.append_path(new_path, filename), util.append_path(new_path, new_filename))
    util.print_divider()


if __name__ == "__main__":
    main()
