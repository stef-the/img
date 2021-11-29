import json, os, time, subprocess

def scan(folder, jsonf):
    global add
    a, diff, add = json.loads(open(jsonf, 'r').read()), False, False

    for i in os.listdir(folder):
        if not i in a:
            os.rename(f'{folder}/{i}', f'{folder}/{len(os.listdir(folder))-1}.png')
            a.append(f'{len(os.listdir(folder))-1}.png')
            diff = True

            print(f'- NUM URL -\nhttps://raw.githubusercontent.com/stef-the/img/master/img/{len(os.listdir(folder))-1}.png')
            subprocess.run("pbcopy", universal_newlines=True, input=f'https://raw.githubusercontent.com/stef-the/img/master/img/{len(os.listdir(folder))-1}.png')
            add = True

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

        if add:
            os.system(f'''osascript -e 'display alert "Screenshot Posted" message "Your screenshot the {a}th one. It has been posted to your clipboard."\'''')

    else:
        print('nothing at ' + str(time.time()))
    
    time.sleep(1)