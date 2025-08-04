import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    # Test case 1: Test props_to_html with multiple properties
    def test_props_to_html_with_props(self):
        node = HTMLNode(
            "a",
            "Click me",
            None,
            {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    # Test case 2: Test props_to_html when props is None
    def test_props_to_html_no_props(self):
        node = HTMLNode("p", "Some text")
        self.assertEqual(node.props_to_html(), "")

    # Test case 3: Test the __repr__ method for correct string representation
    def test_repr_method(self):
        node = HTMLNode(
            "div",
            "Hello",
            children=[HTMLNode("p", "World")],
            props={"class": "container", "id": "main"}
        )
        expected_repr = "HTMLNode(tag='div', value='Hello', children=[HTMLNode(tag='p', value='World', children=None, props=None)], props={'class': 'container', 'id': 'main'})"
        self.assertEqual(repr(node), expected_repr)

if __name__ == '__main__':
    unittest.main()
