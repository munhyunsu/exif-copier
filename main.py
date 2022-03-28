import os

FLAGS = _ = None
DEBUG = False


def check_binary():
    pass


def main():
    if DEBUG:
        print(f'Parsed arguments {FLAGS}')
        print(f'Unparsed arguments {_}')


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

