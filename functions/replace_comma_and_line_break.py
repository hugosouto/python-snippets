# Read the file
with open('snippets-python/functions/input/text_with_commas.txt', 'r') as file:
    
    content = file.read()

# Replace the comma followed by a line break with just a comma
content = content.replace(',\n', ',')

# Write the content back to the file
with open('snippets-python/functions/output/text_with_commas.txt', 'w') as file:
    file.write(content)
