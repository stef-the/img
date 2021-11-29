import json, os, time

def addToClipBoard(text):
    command = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(command)

def scan(folder, jsonf):
    a, diff = json.loads(open(jsonf, 'r').read()), False

    for i in os.listdir(folder):
        if not i in a:
            os.rename(f'{folder}/{i}', f'{folder}/{len(os.listdir(folder))-1}.png')
            a.append(f'{len(os.listdir(folder))-1}.png')
            diff = True

            print(f'- NUM URL -\nhttps://raw.githubusercontent.com/stef-the/img/master/img/{len(os.listdir(folder))-1}.png')
            addToClipBoard(f'https://raw.githubusercontent.com/stef-the/img/master/img/{len(os.listdir(folder))-1}.png')

    for i in a:
        if not i in os.listdir(folder):
            a.remove(i)
            diff = True

    open(jsonf, 'w').write(json.dumps(a))
    return diff

while True:
    if scan('img', 'imglist.json'):
        a = str(int(open('iter.txt', 'r').read())+1)
        os.system('git add .')
        os.system(f'git commit -m img{a}')
        open('iter.txt', 'w').write(a)
        os.system('git push')

    else:
        print('nothing at ' + str(time.time()))
    
    time.sleep(1)