import os
from pathlib import Path


# prints a simple divider to console using dashes
def print_divider():
    print("-------------------------------------------------------")


# checks the file's extensions and returns true if it's .flac, .mp3, .jpg or .png.
def should_handle_file(file: Path):
    return filecheck_music(file) or filecheck_image(file) or should_delete(file)


# checks if the given file is a music file
def filecheck_music(file: Path):
    extension = file.suffix
    return extension == ".flac" or extension == ".mp3"


# checks if the given file is an image
def filecheck_image(file: Path):
    extension = file.suffix
    return extension == ".jpg" or extension == ".jpeg" or extension == ".png"


def append_path(path, filename):
    return path + "/" + filename


# checks if the given file is a file that should be deleted (ie .m3u)
def should_delete(file: Path):
    return file.suffix == ".m3u"


# returns only the file's extension
def get_extension(filename):
    return os.path.splitext(filename)[1]


# returns the name of the file, excluding the extension
def get_filehead(filename):
    return os.path.splitext(filename)[0]
