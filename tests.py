import unittest
from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):
    def has_error(self, directory: str) -> bool:
        working_directory = "calculator"
        result = get_files_info(working_directory, directory)
        print(result)
        return result.startswith("Error: ")

    def test_get_files_info(self):
        self.assertFalse(
            self.has_error("."), "Expected no error for current directory '.'"
        )
        self.assertFalse(self.has_error("pkg"), "Expected no error for directory 'pkg'")
        self.assertTrue(
            self.has_error("/bin"), "Expected an error for directory '/bin'"
        )
        self.assertTrue(self.has_error("../"), "Expected an error for directory '../'")


if __name__ == "__main__":
    unittest.main()
