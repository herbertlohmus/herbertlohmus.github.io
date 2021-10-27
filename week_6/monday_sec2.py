#print('Hello World!')

with open('week_6/blurb', 'r', encoding='utf16') as f:
    text = f.read()

with open('week_6/blurb_out', 'w', encoding='utf8') as f:
    f.write(text.upper())

print(text)
