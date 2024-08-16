from textnode import (
    TextNode,
    text_node_to_html_node
)
from htmlnode import LeafNode
def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")

    print( node )
     








if __name__ == "__main__":
    main()