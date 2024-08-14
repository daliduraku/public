import unittest
from textnode import TextNode
from main import text_node_to_html_node
from htmlnode import LeafNode


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
 
 
    
if __name__ == "__main__":
    unittest.main()