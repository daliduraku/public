import unittest
import re 
from textnode import TextNode
from split_delimiter import split_nodes_delimiter
from split_delimiter import extract_markdown_images
from split_delimiter import extract_markdown_links

class TestSplitDelimiter(unittest.TestCase):
    
    def test_split_by_delimiter(self):
        input_string = "This is text with a **bolded phrase** in the middle"
        delimiter = "**"
        expected_output = [TextNode("This is text with a ", "text"), TextNode("bolded phrase", "bold"), TextNode(" in the middle", "text"),]
        node = split_nodes_delimiter(input_string, delimiter, "bold")
        self.assertEqual(node, expected_output)
        
    def testtwo_split_by_delimiter(self):
        expected_output = [TextNode("This is text with a ", "text"), TextNode("code block", "code"), TextNode(" word", "text"),]    
        node = split_nodes_delimiter("This is text with a `code block` word", "`", "code")
        self.assertEqual(node, expected_output)

    
class TestExtractImage(unittest.TestCase):
    
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        node = extract_markdown_images(text)
        expected_output = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(node, expected_output)

class TestExtractLinks(unittest.TestCase):
    
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        node = extract_markdown_links(text)
        expected_output = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(node, expected_output)





if __name__ == '__main__':
    unittest.main()