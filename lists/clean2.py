with open("vulns.txt", 'r') as r:
    lists = r.read()


lists = lists.replace("http://","")

with open("vulns.txt","w") as w:
    w.write(lists)
