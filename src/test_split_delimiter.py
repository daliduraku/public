import unittest
import re 
from split_delimiter import (
    split_nodes_delimiter , 
    extract_markdown_images, 
    extract_markdown_links ,
    split_nodes_image,
    split_nodes_link,
)

from textnode import ( TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link, 
) 
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

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        node = extract_markdown_images(text)
        expected_output = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(node, expected_output)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        node = extract_markdown_links(text)
        expected_output = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(node, expected_output)

    def test_split_image_single(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.com/image.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("image", text_type_image, "https://www.example.com/image.png")],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode( "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )


if __name__ == '__main__':
    unittest.main()