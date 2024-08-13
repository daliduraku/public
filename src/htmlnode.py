

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