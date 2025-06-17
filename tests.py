import unittest
from functions.get_files_info import get_files_info, get_file_content, write_file

WORKING_DIRECTORY = "calculator"


class TestGetFilesInfo(unittest.TestCase):
    # def test_get_files_info(self):
    #     def check(directory: str) -> tuple[bool, str]:
    #         result = get_files_info(WORKING_DIRECTORY, directory)
    #         has_error = result.startswith("Error")
    #         return has_error, result
    #
    #     # Test with valid directories
    #     has_error, result = check(".")
    #     self.assertFalse(has_error, "Expected no error for '.', got:\n" + result)
    #     has_error, result = check("pkg")
    #     self.assertFalse(has_error, "Expected no error for 'pkg', got:\n" + result)
    #
    #     # Test with invalid directories
    #     has_error, result = check("/bin")
    #     self.assertTrue(has_error, "Expected an error for '/bin', got:\n" + result)
    #     has_error, result = check("../")
    #     self.assertTrue(has_error, "Expected an error for '../', got:\n" + result)
    #
    # def test_get_file_content(self):
    #     def check(file_path: str) -> tuple[bool, str]:
    #         result = get_file_content(WORKING_DIRECTORY, file_path)
    #         has_error = result.startswith("Error")
    #         return has_error, result
    #
    #     # Test with valid files
    #     has_error, result = check("main.py")
    #     self.assertFalse(has_error, "Expected no error for 'main.py', got:\n" + result)
    #     has_error, result = check("pkg/calculator.py")
    #
    #     # Test with invalid files
    #     has_error, result = check("/bin/cat")
    #     self.assertTrue(has_error, "Expected an error for '/bin/cat', got:\n" + result)

    def test_write_file(self):
        def check(file_path: str, content: str) -> tuple[bool, str]:
            result = write_file(WORKING_DIRECTORY, file_path, content)
            print(result)
            has_error = result.startswith("Error")

            expected = "an error" if has_error else "no error"
            message = f"Expected {expected} for writing to {file_path} {result=}"

            return has_error, message

        # Test writing to a valid file
        has_error, msg = check("lorem.txt", "wait, this isn't lorem ipsum")
        self.assertFalse(has_error, msg)
        has_error, msg = check("pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        self.assertFalse(has_error, msg)

        # Test writing to an invalid file
        has_error, msg = check("/tmp/temp.txt", "this should not be allowed")
        self.assertTrue(has_error, msg)


if __name__ == "__main__":
    unittest.main()
