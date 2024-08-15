import re
from textnode import TextNode
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    text_type_text = "text"; text_type_bold = "bold"; text_type_italic = "italic"; text_type_code = "code"; 
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
    text_type_image = "image"
    text_type_text = "text"
    nodes_no_img = []
    new_nodes = []

    for node in old_nodes:
        images = extract_markdown_images(node.text)
        
        if not images:
            nodes_no_img.append(node)
        
        else:
            for image_alt, image_link in images:
                sections = node.text.split(f"![{image_alt}]({image_link})", 1)

                if sections[0]:
                    new_nodes.append(TextNode(sections[0], text_type_text))
                
                new_nodes.append(TextNode(f"![{image_alt}]({image_link})", text_type_image))
                
                if len(sections) > 1 and sections[1]:
                    new_nodes.append(TextNode(sections[1], text_type_text))
    
    return new_nodes
        
         
    
    