import unittest
from htmlnode import LeafNode
from textnode import (
    TextNode,
    text_node_to_html_node,
)



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_two(self):
        node = TextNode("This is a text node", "italic", None)
        node2 = TextNode("This is a text node", "italic", "https://www.boot.dev")
        self.assertNotEqual(node, node2)
    
    def test_three(self):
        node = TextNode("This is a text node", "italic", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")    
        self.assertNotEqual(node, node2)

instance_one = TextNode("Example", "bold")

check_one = text_node_to_html_node(instance_one)
assert isinstance(check_one, LeafNode)
assert check_one.tag == "b"

 
    
if __name__ == "__main__":
    unittest.main()