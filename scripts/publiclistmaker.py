import fileinput
url =[]
url2=[]
with fileinput.input(files=('userurl.txt')) as f:
    for line in f:
        url.append(line.replace("\n", ""))
for ele in url:
    if ele.strip():
        url2.append(ele)
print(url2)
with open('finaluserurl.txt', 'w') as f:
    print(url2, file=f)
