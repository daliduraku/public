from textnode import TextNode
from htmlnode import LeafNode
def main():
    dummy_var = TextNode("This is a text node", "bold", "https://www.boot.dev")
    
    #print(dummy_var)
    
def text_node_to_html_node(text_node):
    
    text_type_text = "text", text_type_bold = "bold", text_type_italic = "italic", text_type_code = "code", text_type_link = "link", text_type_image = "image"
    text_node_dict = {
        
        text_type_text: "text",
        text_type_bold: "bold",
        text_type_italic: "italic",
        text_type_code: "code",
        text_type_link: "link",
        text_type_image: "image" 
    }
    
    if text_node not in text_node_dict:
        raise Exception
        
    if text_node == text_node_dict[text_type_text]:
        return LeafNode(None, text_node, None, None)
    elif text_node == text_node_dict[text_type_bold]:
        return LeafNode("b", text_node, None, None)
    elif text_node == text_node_dict[text_type_italic]:
        return LeafNode("i", text_node, None, None)
    elif text_node == text_node_dict[text_type_code]:
        return LeafNode("code", text_node, None, None)
    elif text_node == text_node_dict[text_type_link]:
        return LeafNode("a", text_node.text, None, {"href": text_node.url})
    else:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})    








if __name__ == "__main__":
    main()