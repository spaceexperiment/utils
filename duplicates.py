import os
import sys
import md5
from pprint import pprint
from collections import defaultdict


if len(sys.argv) < 2:
    print 'please enter a dir'
    sys.exit()
path = sys.argv[1]


def md5_file(file_path, block_size=2**20 * 60):
    """ return md5 hash of a file, 2**20 is 1mb """
    m = md5.new()
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(block_size)
            if not chunk:
                break
            m.update(chunk)
    return m.digest()


file_sizes = defaultdict(list)
for root, dirs, filenames in os.walk(path):
    for filename in filenames:
        file_path = os.path.join(root, filename)
        file_sizes[os.path.getsize(file_path)].append(file_path)
# list of files with one or more equel file size
file_sizes = [x for x in file_sizes.values() if len(x) > 1]

files = defaultdict(list)
for paths in file_sizes:
    for path in paths:
        key = md5_file(path)
        files[key].append(path)
files = [x for x in files.values() if len(x) > 1]

for duplicates in files:
    print '\n\n_________________________________________'
    pprint(duplicates)
    print '_________________________________________'

print '\n%s files with atleast one duplicate\n' % len(files)
