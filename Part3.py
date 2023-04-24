import os
import hashlib
import unittest

class DuplicateFileDetector:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.file_hashes = {}
        self.duplicate_files = []

    def detect_duplicates(self):
        for root, dirs, files in os.walk(self.directory_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_hash = self.get_file_hash(file_path)
                if file_hash in self.file_hashes:
                    self.file_hashes[file_hash].append(file_path)
                    self.duplicate_files.append(file_path)
                else:
                    self.file_hashes[file_hash] = [file_path]

    def get_file_hash(self, file_path):
        with open(file_path, 'rb') as f:
            data = f.read()
            file_hash = hashlib.md5(data).hexdigest()
        return file_hash

    def print_duplicate_files(self):
        if not self.duplicate_files:
            print('No duplicate files found.')
        else:
            print('Duplicate files found:')
            for file_path in self.duplicate_files:
                print(file_path)

class DuplicateDetectorTest(unittest.TestCase):
    currentPath = os.getcwd()
    folderName = 'pictures'
    folderPath = os.path.join(currentPath, folderName)

    def testDupl(self):

        pictures = DuplicateFileDetector(self.folderPath)
        pictures.detect_duplicates()
        self.assertEqual(len(pictures.duplicate_files),6)

if __name__ == '__main__':
    unittest.main()

