import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    """
    This test suite contains various unit tests for the extract_title function.
    """

    def test_simple_case(self):
        """
        Tests a simple markdown string with a single H1 header.
        """
        markdown = "# Hello World"
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_content_before_header(self):
        """
        Tests a markdown string that has content before the H1 header.
        The function should still correctly find the header.
        """
        markdown = "Some intro text.\n\n# Main Title\n\nMore content here."
        self.assertEqual(extract_title(markdown), "Main Title")

    def test_no_header(self):
        """
        Tests a markdown string that does not contain an H1 header.
        The function is expected to raise an Exception.
        """
        markdown = "A document without a title."
        with self.assertRaisesRegex(Exception, 'This document needs a header: #'):
            extract_title(markdown)

    def test_header_with_extra_whitespace(self):
        """
        Tests a markdown string where the H1 header has extra whitespace
        before or after the text. The function should correctly trim it.
        """
        markdown = "#    A Titled Document   "
        self.assertEqual(extract_title(markdown), "A Titled Document")

    def test_empty_string(self):
        """
        Tests an empty markdown string. It should raise an exception
        as it has no header.
        """
        markdown = ""
        with self.assertRaisesRegex(Exception, 'This document needs a header: #'):
            extract_title(markdown)

    def test_only_whitespace(self):
        """
        Tests a markdown string that only contains whitespace. It should
        raise an exception as there is no header.
        """
        markdown = "   \n\n"
        with self.assertRaisesRegex(Exception, 'This document needs a header: #'):
            extract_title(markdown)

    def test_header_without_space(self):
        """
        Tests for a header that's missing the space after the hash.
        Your current function is designed to fail gracefully on this.
        """
        markdown = "#NoSpaceHere"
        with self.assertRaisesRegex(Exception, 'This document needs a header: #'):
            extract_title(markdown)

if __name__ == '__main__':
    unittest.main()
