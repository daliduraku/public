import re

# creating a tuple with the startwith
start_of_headings = ("# ", "## ", "### ", "#### ", "##### ", "###### ",)
start_of_code ="```"
start_of_line = ">"
start_of_unordered = ("* ", "- ")
start_of_paragraph = "paragraph"

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

# function takes a string in as the form single block of markdown text
def block_to_block_type(markdown):

    # checking 
    if markdown.startswith(start_of_headings):
        return "heading"
    
    # spliting the string into lines
    lines = markdown.splitlines()
    
    if lines[0].startswith(start_of_code) and lines[-1].endswith("```"):
            return "code"
    
    # checking uniformity 
    all_quote = all(line.startswith(start_of_line) for line in lines)

    if all_quote:
        return "quote"

     # checking uniformity 
    all_unordered = all(line.startswith(start_of_unordered) for line in lines)

    if all_unordered:
        return "unordered_list"
    
    current_number = 1
    is_ordered = True
    for line in lines:
        if line.startswith(f"{current_number}. "):
            current_number += 1
        else:
            is_ordered = False
            break
    
    if is_ordered:
        return "ordered_list"
    else:
        return "paragraph"
    