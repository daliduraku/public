import re

def markdown_to_blocks(markdown):
    blank_line_regex = r"(?:\r?\n){2,}"
    
    markdown_strings = re.split(blank_line_regex, markdown.strip())
    final_markdownstrings = []
    for string in markdown_strings:
        if string != "":
            final_markdownstrings.append(string)
        
    
    return final_markdownstrings
    
    
    