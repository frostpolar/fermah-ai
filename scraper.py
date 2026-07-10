import requests
import re
from bs4 import BeautifulSoup

url="https://fermah.xyz"
"https://fermah.xyz/froben"
"https://fermah.xyz/kernel"
"https://docs.fermah.xyz"
"https://fermah.xyz/careers"
"https://fermah.xyz/blog"

response=requests.get(url)

soup=BeautifulSoup(
    response.text,
    "html.parser"
)

for tag in soup([
    "script",
    "style",
    "nav",
    "footer"
]):
    tag.decompose()

text=soup.get_text(
    separator="\n"
)

lines=[]

for line in text.splitlines():

    cleaned=line.strip()

    if len (cleaned) > 2:
        if not cleaned.startswith("/"):
          lines.append(cleaned)

final_text="\n".join(lines)

final_text = re.sub(
    r'\n+',
    '\n',
    final_text
)

with open(
    "knowledge.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(final_text)

print(
    "knowledge saved"
)