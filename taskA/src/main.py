import argparse
import os

def create_argument_parser():
    parser = argparse.ArgumentParser(description = 'GenerateFile creates a random file of a given size')
    parser.add_argument('--filename', nargs = '?', required = True, help = 'The name of the file to create')
    parser.add_argument('--filesize', nargs = '?', required = True, help = 'The size of the file to create in bytes.', type = int)
    return parser

def generate_file(filename, filesize):
    command = 'head -c {0} < /dev/urandom > {1}'.format(filesize, filename);

    print('Generating new random file with:');
    print(command);

    os.system(command);

if __name__ == "__main__":
    parser = create_argument_parser()
    args = parser.parse_args()
    generate_file(args.filename, args.filesize);
