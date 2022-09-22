# access24.py
"""
What files have been accessed during the last 24 hours?
"""

import os
import time


def get_accessed(start_dir, since=24):
    """Return the full names of all files changed within the last
    24 hours or the time in hours given with `since`.
    """
    if not os.path.exists(start_dir):
        raise ValueError('no such directory:', start_dir)
    if since <= 0:
        raise ValueError('Value for `since` must be positive.')
    time_stamp = time.time() - (since * 3600)
    found = []
    for root, _dir_names, file_names in os.walk(start_dir):
        for file_name in file_names:
            # some files are not real files
            full_name = os.path.join(root, file_name)
            try:
                atime = os.path.getatime(full_name)
            except OSError:
                print('not found', file_name)
            if atime >= time_stamp:
                found.append(full_name)
    return found

if __name__ == '__main__':

    def test():
        """Try on `tmp`.
        """
        found = (get_accessed(os.path.join(os.path.expanduser('~'), 'tmp')))
        for file_name in found:
            print(file_name)
        print('found:', len(found), 'files', \
        'that were changed within the last 24 hours.')

test()
