"""
Enables all raw objects in a specified folder
"""

import sys, os, argparse, shutil, re

metatag_regex = re.compile(r'!NO[A-Z]+:?!')
#metatag_regex2 = re.compile(r'NO[A-Z]+:?!')
COUNT = 0
#l1 = []
#l2 = []

def printf(*args):
    sys.stdout.write(''.join([str(a) for a in args]))
    sys.stdout.flush()

def process_file(filename):
    printf('Processing %s... ' % filename)
    path = os.path.join(args.raw, filename)
    f = open(path)
    contents = f.read()
    f.close()
    if metatag_regex.search(contents) is not None:
        printf('replacing... ')
        matches = metatag_regex.findall(contents)
        #matches = [s.string[s.start():s.end()] for s in metatag_regex.finditer(contents)]
        #matches2 = ['!' + s.string[s.start():s.end()] for s in metatag_regex2.finditer(contents)]
        printf(matches)
        global COUNT, l1, l2
        COUNT += len(matches)
        #l1.extend(matches)
        #l2.extend(matches2)
        printf('done.\n')
    else:
        printf('no change required.\n')

parser = argparse.ArgumentParser()
parser.add_argument('--raw', help='The raw folder to modify', required=True)
parser.add_argument('--backup', required=False, default=None,
    help='A folder to copy the raws to before modification (optional)')
args = parser.parse_args()

if not os.path.exists(args.raw):
    print('Error: Raw folder does not exist')
    sys.exit()

if args.backup is not None:
    if os.path.exists(args.backup):
        print('Error: Backup folder already exists')
        sys.exit()
    printf('Backing up raws... ')
    shutil.copytree(args.raw, args.backup)
    printf('done.\n')

for f in os.listdir(args.raw):
    if f.endswith('.txt'):
        process_file(f)
    #break
print(COUNT)
#print(set(l2) | set(l1))
