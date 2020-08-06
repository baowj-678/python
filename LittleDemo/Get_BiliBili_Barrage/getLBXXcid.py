import re

with open('LittleDemo/GetBiliBiliBarrage/lbxx.txt',
          mode='r',
          encoding='utf-8') as file:
    text = file.read()
cids = re.findall(r'"cid":([\d]*),"from"', text)
print(cids)

with open('LittleDemo/GetBiliBiliBarrage/lbxx-cid.txt',
          mode='w+',
          encoding='utf-8') as file:
    file.write('\n'.join(cids))
