with open("E:\dkun05fd.used_txt",  "r") as f:
    res = f.read()
# print(res)
import re

# re.split('[_#|]','this_is#a|test')
content = re.split('http://', res)
print(content)
print(len(content))

list_data = []
for data in content:
    url = 'http://' + data + "\n"
    list_data.append(url)
print(list_data)
with open(r"E:\all_url.used_txt", "w") as f:
    for signal_url in list_data:
        f.write(signal_url)
        print(signal_url)
