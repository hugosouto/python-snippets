def convert_to_codes(input_numbers):
    numbers = input_numbers.split(',')
    codes = ['1' + str(number).zfill(9) for number in numbers]
    output_codes = "'" + "','".join(codes) + "'" # Add quotes around each code
    return output_codes

# Read the file
with open('snippets-python/functions/input/integers_in_line.txt', 'r') as file:
    content = file.read()

# input_numbers = "299426,239400,10839,271836,227649,64831,1000136999"
input_numbers = content
output_codes = convert_to_codes(input_numbers)
# Replace the comma followed by a line break with just a comma
# content = content.replace(',\n', ',')
print("OUTPUT:", output_codes)

# Write the content back to the file
with open('snippets-python/functions/output/codes_in_line.txt', 'w') as file:
    file.write(output_codes)
