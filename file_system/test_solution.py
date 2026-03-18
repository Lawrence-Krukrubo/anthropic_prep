import unittest
from solution import FileSystem

class TestFileSystemLevel1(unittest.TestCase):
    def setUp(self):
        # This runs before every single test to give you a fresh instance
        self.fs = FileSystem()

    def test_create_and_read_file(self):
        self.assertTrue(self.fs.create_file("doc.txt"))
        self.assertFalse(self.fs.create_file("doc.txt")) # Should return False if it already exists
        
        self.fs.write_to_file("doc.txt", "hello world")
        self.assertEqual(self.fs.read_file("doc.txt"), "hello world")

    def test_missing_file_errors(self):
        # Reading a missing file should raise a ValueError
        with self.assertRaises(ValueError):
            self.fs.read_file("missing.txt")
        
        # Writing to a missing file should raise a ValueError
        with self.assertRaises(ValueError):
            self.fs.write_to_file("missing.txt", "data")

    def test_delete_file(self):
        self.fs.create_file("temp.txt")
        self.assertTrue(self.fs.delete_file("temp.txt"))
        self.assertFalse(self.fs.delete_file("temp.txt")) # Already deleted, should return False
        
        # Ensure it's actually deleted
        with self.assertRaises(ValueError):
            self.fs.read_file("temp.txt")

if __name__ == '__main__':
    unittest.main()