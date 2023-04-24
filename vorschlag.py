import os
import hashlib

def find_duplicates(rootdir):
    # Dictionary to store the file hashes
    hash_dict = {}

    # Iterate through all files in the directory tree
    for subdir, dirs, files in os.walk(rootdir):
        for filename in files:
            filepath = os.path.join(subdir, filename)

            # Skip non-image files
            if not filename.endswith(('.jpg', '.jpeg', '.png')):
                continue

            # Calculate the MD5 hash of the file
            with open(filepath, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()

            # Check if the hash is already in the dictionary
            if file_hash in hash_dict:
                print(f"Duplicate found: {filepath} and {hash_dict[file_hash]}")
            else:
                hash_dict[file_hash] = filepath

if __name__ == '__main__':
    # Specify the root directory to search for duplicates
    rootdir = '/Users/basselsamo/Downloads/testing'

    # Call the find_duplicates function
    find_duplicates(rootdir)