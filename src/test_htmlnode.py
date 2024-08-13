import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        children = ["one", "two", "random", "three"]
        props = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HTMLNode("h1", None,children, props)
        
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"' )

    def test_html_noprops(self):
        children = ["one", "two", "three"]
        node = HTMLNode("p", None, children)
        self.assertEqual(node.props_to_html(), "")

    def test_empty_htmlnode(self):
        node = HTMLNode(None, None, None, None)
        self.assertEqual(node.props_to_html(), "")


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def testtwo_to_html(self):
        node = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "This is a paragraph of text.")
        
    def testthree_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')


if __name__ == "__main__":
    unittest.main()