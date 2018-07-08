f = open('words.txt','r',encoding='utf-8')
lines=[]
while True:
    line = f.readline()
    lines.append(line.strip('\n'))
# 零长度指示 EOF
    if len(line) == 0:
        break
# 关闭文件
f.close()
ab = {}
# 添加一对键值—值配对
for it in lines:
    if it in ab:
        ab[it]+=1
    else:
        ab[it]=1
print(sorted(ab.items(),key=lambda e:e[1],reverse=True)[0:10:1])
