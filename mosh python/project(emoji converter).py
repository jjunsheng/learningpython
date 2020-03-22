command = input("> ")
words = command.split(" ")
print(words)

emojis_dictionary = {
    ":)": "happy",
    ":(": "sad",
    ":')": "ugly"
}

output = ""
for word in words:
    output += emojis_dictionary.get(word,word) + " "
print(output)