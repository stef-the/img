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
    return diff

if scan('img', 'imglist.json'):
    a = str(int(open('iter.txt', 'r').read())+1)
    os.system('git add .')
    os.system(f'git commit -m img{a}')
    open('iter.txt', 'w').write(a)
    os.system('git push')
