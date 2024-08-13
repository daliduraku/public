import unittest
from htmlnode import HTMLNode


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







if __name__ == "__main__":
    unittest.main()