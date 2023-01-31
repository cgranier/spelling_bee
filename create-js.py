# Read the collins.txt file
with open("collins.txt", "r") as wordfile:
    words = [word.strip() for word in wordfile]

# Write the data to collins.js
with open("collins.js", "w") as outfile:
    outfile.write("const collins = [\n")
    for word in words:
        outfile.write(f"  '{word}',\n")
    outfile.write("];\n")