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


class TestFileSystemLevel2(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()

    def test_create_directory_and_file(self):
        # Create a directory
        self.assertTrue(self.fs.create_directory("/docs"))
        self.assertFalse(self.fs.create_directory("/docs")) # Already exists
        
        # Create a file inside the directory
        self.assertTrue(self.fs.create_file("/docs/readme.txt"))
        self.fs.write_to_file("/docs/readme.txt", "Level 2 complete")
        self.assertEqual(self.fs.read_file("/docs/readme.txt"), "Level 2 complete")

    def test_missing_parent_directory(self):
        # Cannot create a file or directory if the parent doesn't exist
        self.assertFalse(self.fs.create_directory("/folders/images")) 
        self.assertFalse(self.fs.create_file("/music/song.mp3"))

    def test_root_directory_always_exists(self):
        # Should be able to create files directly in root
        self.assertTrue(self.fs.create_file("/root_file.txt"))
        
    def test_directory_is_not_a_file(self):
        self.fs.create_directory("/var")
        # Cannot read or write to a directory
        with self.assertRaises(ValueError):
            self.fs.write_to_file("/var", "data")
        with self.assertRaises(ValueError):
            self.fs.read_file("/var")

if __name__ == '__main__':
    unittest.main()