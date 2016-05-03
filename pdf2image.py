import os
import sys
from PythonMagick import Image


def main():
    # os.environ["MAGICK_HOME"] = r"path_to_ImageMagick"

    if len(sys.argv) == 1:
        dirpath = '.'
    else:
        dirpath = sys.argv[1]

    for path in os.listdir(dirpath):
        if not os.path.isfile(path) or not path.endswith('.pdf'):
            continue
        print('Converting file {} ...'.format(path))
        file = os.path.join(dirpath, path)
        to = file.replace(".pdf", ".png")

        p = Image()
        p.density('1080')
        p.read(os.path.abspath(file))
        p.write(os.path.abspath(to))

if __name__ == '__main__':
    main()