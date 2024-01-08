import sys
from pathlib import Path
from clean_folder.scan import sort_folder, unknown, extensions


def start():

    path = Path(sys.argv[1])

    sort_folder(path, path)

    print(f'unknown extensions: {unknown}')
    print(f'known extensions:   {extensions}')


if __name__ == '__main__':
    start()
