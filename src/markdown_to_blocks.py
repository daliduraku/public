import re

def markdown_to_blocks(markdown):
    blank_line_regex = r"(?:\r?\n){2,}"
    
    markdown_strings = re.split(r"(?:\r?\n){2,}", markdown.strip())
    final_markdownstrings = []

    for string in markdown_strings:
        cleaned_string = string.split('\n')
        
        cleaned_lines = []
        for string in cleaned_string:
            cleaned_strings = string.strip()
            cleaned_lines.append(cleaned_strings)
        final_string =  "\n".join(cleaned_lines)
        
        if final_string != "":
            final_markdownstrings.append(final_string)   
        
    
    return final_markdownstrings
    
    
    