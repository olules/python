import argparse

def file_parser(input_file, output_file=''):
    print(f'Processing {input_file}')
    print('Finished Processing')
    if output_file:
        print(f'Creating {output_file}')

def main():
    parser = argparse.ArgumentParser('File Parser')
    parser.add_argument('--infile', help='Input files')
    parser.add_argument('--out', help='Output file')
    args = parser.parse_args()
    if args.infile:
        file_parser(args.infile, args.out)
if __name__ == '__main__':
    main()
        
    