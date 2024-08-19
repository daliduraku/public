

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        if children == None:
            self.children = []
        else:
            self.children = children
        if props == None:
            self.props = {}
        else:
            self.props = props
            
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_string = ""
        for key in self.props:
            props_string += f' {key}="{self.props[key]}"'
        return props_string
    
    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props) 
    
    
    def to_html(self):
        if self.tag == "" and (self.value in ["", None]) and not self.props:
            raise ValueError
        
        if self.tag is None:
            return f"{self.value}"
        
        conca_string = self.props_to_html()
        
        if self.tag != "" and self.value not in ["", None]:
            if self.props:
                return f'<{self.tag}{conca_string}>{self.value}</{self.tag}>'
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            
        elif self.tag != "" and self.value in ["", None]:
            return f"<{self.tag}{conca_string}/>"
        
class ParentNode(HTMLNode):
    def __init__(self,tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)
        
    def to_html(self):
        if self.tag in ["", None]:
            raise ValueError
            
        if len(self.children) == 0:
            raise ValueError("Children is an empty list")
            
        conca_string = self.props_to_html()
        
        # Recursively process each child node
        children_html = "".join([child.to_html() for child in self.children])

        # Build and return the complete HTML string
        return f'<{self.tag}{conca_string}>{children_html}</{self.tag}>'