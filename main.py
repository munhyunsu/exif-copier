import os
import csv
import subprocess
import shlex
import shutil

FLAGS = _ = None
DEBUG = False


def check_binary(tool_root):
    tool = os.path.join(tool_root, 'exiftool')
    subprocess.run(tool, check=True)
    return tool


def get_exif(csv_path):
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            imagepath = row['ImagePath']
            tags = set(row.keys())
            tags.remove('ImagePath')
            exif = ''
            for tag in tags:
                exif = f'{exif} -{tag}={row[tag]}'
            yield (imagepath, exif)


def main():
    if DEBUG:
        print(f'Parsed arguments {FLAGS}')
        print(f'Unparsed arguments {_}')
    tool = check_binary(FLAGS.exiftool)

    os.makedirs(FLAGS.output, exist_ok=True)
    for imagepath, exif in get_exif(FLAGS.input):
        commands = shlex.split(f'{tool} {imagepath} {exif}')
        if DEBUG:
            print(f'RUN: {commands}')
        subprocess.run(commands)
        shutil.move(imagepath, FLAGS.output)
        shutil.move(f'{imagepath}_original', imagepath)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true',
                        help='The present debug message')
    parser.add_argument('--exiftool', default='./exiftool/',
                        help='The directory for exiftool')
    parser.add_argument('--input', default='./input.csv',
                        help='The input csv (fieldnames: filename,altitude,latitude,longitude,roll,yaw,patch)')
    parser.add_argument('--output', default='./output',
                        help='The output directory')

    FLAGS, _ = parser.parse_known_args()
    DEBUG = FLAGS.debug

    FLAGS.exiftool = os.path.abspath(os.path.expanduser(FLAGS.exiftool))
    FLAGS.input = os.path.abspath(os.path.expanduser(FLAGS.input))
    FLAGS.output = os.path.abspath(os.path.expanduser(FLAGS.output))

    main()

