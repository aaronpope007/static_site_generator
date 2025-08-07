import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    # --- New Unit Tests for LeafNode ---

    # Test case 4: Test to_html for a standard LeafNode with a tag
    def test_leaf_node_to_html(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")

    # Test case 5: Test to_html for a LeafNode with a tag and props
    def test_leaf_node_with_props_to_html(self):
        node = LeafNode("a", "Click me", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me</a>')

    # Test case 6: Test to_html for a LeafNode without a tag (raw text)
    def test_leaf_node_without_tag_to_html(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    # Test case 7: Test that to_html raises a ValueError if the value is missing
    def test_leaf_node_no_value_raises_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    # --- New Unit Tests for ParentNode ---

        # Test case 8: Test to_html for a ParentNode with multiple children
        def test_parent_node_with_multiple_children(self):
            child_node1 = LeafNode("span", "Hello")
            child_node2 = LeafNode("b", "World")
            parent_node = ParentNode("p", [child_node1, child_node2])
            self.assertEqual(parent_node.to_html(), "<p><span>Hello</span><b>World</b></p>")

        # Test case 9: Test to_html for a ParentNode with props
        def test_parent_node_with_props(self):
            child_node = LeafNode("span", "Content")
            parent_node = ParentNode(
                "div", [child_node], {"class": "container", "id": "main"}
            )
            self.assertEqual(
                parent_node.to_html(),
                '<div class="container" id="main"><span>Content</span></div>',
            )

        # Test case 10: Test that to_html raises a ValueError if the tag is missing
        def test_parent_node_no_tag_raises_error(self):
            with self.assertRaises(ValueError):
                parent_node = ParentNode(None, [LeafNode("span", "child")])
                parent_node.to_html()

        # Test case 11: Test that to_html raises a ValueError if children are missing
        def test_parent_node_no_children_raises_error(self):
            with self.assertRaises(ValueError):
                parent_node = ParentNode("div", None)
                parent_node.to_html()

        # Test case 12: Test a complex, nested ParentNode structure
        def test_to_html_nested_parent_nodes(self):
            grandchild_node = LeafNode("a", "Click here", {"href": "https://boot.dev"})
            child_node = ParentNode("p", [grandchild_node])
            parent_node = ParentNode("body", [child_node], {"style": "font-family: sans-serif;"})
            self.assertEqual(
                parent_node.to_html(),
                '<body style="font-family: sans-serif;"><p><a href="https://boot.dev">Click here</a></p></body>',
            )

if __name__ == '__main__':
    unittest.main()
