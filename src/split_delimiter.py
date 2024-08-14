from textnode import TextNode
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    text_type_text = "text"; text_type_bold = "bold"; text_type_italic = "italic"; text_type_code = "code"; text_type_link = "link"; text_type_image = "image"
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