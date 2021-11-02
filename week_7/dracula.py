import requests
import re
url = 'https://www.gutenberg.org/files/345/345-h/345-h.htm'
r = requests.get(url)
text = r.text
filename = 'izbicki.html'


text = text.replace("Dracula", "<strong>Izbicki</strong>")
text = text.replace("D&nbsp;R&nbsp;A&nbsp;C&nbsp;U&nbsp;L&nbsp;A",
                    "I&nbsp;Z&nbsp;B&nbsp;I&nbsp;C&nbsp;K&nbsp;I")
text = text.replace("DRACULA", "<strong>IZBICKI</strong>")
text = text.replace('Bram Stoker', 'Herbert Lohmus')
text = text.replace('Bram &nbsp; Stoker', 'Herbert &nbsp; Lohmus')


text = re.sub(r"\bCount\b", "Professor", text)
text = re.sub(r"\bcount\b", "professor", text)
text = re.sub(r"\bCOUNT\b", "PROFESSOR", text)
text = re.sub(r"\bCounts\b", "Professors", text)
text = re.sub(r"\bcounts\b", "professors", text)
text = re.sub(r"\bCOUNTS\b", "PROFESSORS", text)


with open(filename, 'w', encoding='utf-8') as f:
    f.write(text)
