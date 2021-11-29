import json, os
def scan(folder, jsonf):
    a, diff = json.loads(open(jsonf, 'r').read()), False

    for i in os.listdir(folder):
        if not i in a:
            a.append(i)
            diff = True

    for i in a:
        if not i in os.listdir(folder):
            a.remove(i)
            diff = True

    open(jsonf, 'w').write(json.dumps(a))

scan('img', 'imglist.json')