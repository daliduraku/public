import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    nodes = ""
    new_text_type = ""
    if delimiter == "*":
        nodes = old_nodes.split("*")
        new_text_type = text_type_italic
    elif delimiter == "**":
        nodes = old_nodes.split("**")
        new_text_type = text_type_bold
    elif delimiter == "`":
        nodes = old_nodes.split("`")
        new_text_type = text_type_code
    
    text_nodes = []
    for idx, node in enumerate(nodes):
        if idx % 2 == 0:
            text_nodes.append(TextNode(node, text_type_text))
        else:
            text_nodes.append(TextNode(node, new_text_type))
    
    return text_nodes

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    mathces = re.findall(pattern, text)
    return mathces

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )

            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
            
    return new_nodes



def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        
        original_text = old_node.text 
        links = extract_markdown_links(original_text)
        
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            
            original_text = sections[1]
            
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
   
    return new_nodes