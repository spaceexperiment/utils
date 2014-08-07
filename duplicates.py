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


files = defaultdict(list)
for root, dirs, filenames in os.walk(path):
    for filename in filenames:
        file_path = os.path.join(root, filename)
        key = md5_file(file_path)
        files[key].append(file_path)

duplicates = 0
for k, v in files.items():
    if len(v) > 1:
        duplicates += 1
        pprint(v)

print '\n%s files with atleast one duplicate\n' % duplicates
