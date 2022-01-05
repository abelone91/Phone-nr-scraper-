import pyperclip
import re

#create a regex for norwegian phone numbers

phoneNumRegex = re.compile(r"((\+47)?|(\0047)?)\s?(\d+\s?\d+\s?\d+\s?\d+\s?\d+)")
text = pyperclip.paste()
pn_found =  phoneNumRegex.findall(text)
all_pn=[]
for phonenr in pn_found:
    all_pn.append(list(phonenr)[3])
print(all_pn)
