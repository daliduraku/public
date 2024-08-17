import unittest
import re
from markdown_to_blocks import(
    markdown_to_blocks,
    block_to_block_type,
    start_of_code,
    start_of_headings,
    start_of_line,
    start_of_unordered,
    start_of_paragraph,
    
    
    
)

class TestMarkdown(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line

        * This is a list
        * with items
        
        """
        blocks = markdown_to_blocks(md)
        
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
    
    def test_markdown_to_blocks_newlines(self):
        md = """
        This is **bolded** paragraph




        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line

        * This is a list
        * with items
        """ 
        
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                 "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )   
    def test_block_to_block_types(self):
        #block = "# heading"
        #self.assertEqual(block_to_block_type(block), start_of_headings)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), start_of_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), start_of_line)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), start_of_unordered)
        #block = "1. list\n2. items"
        #self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), start_of_paragraph)    
if __name__ == "__main__":
    unittest.main()      
        
