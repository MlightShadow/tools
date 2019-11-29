def loot(url, elem, action):
    if action == 'src':
        save_src(elem)
    elif action == 'file':
        save_file(elem)
    else:
        save_text(elem)

def save_file(elem):
    print('save file')

def save_src(elem):
    print('save src %s', elem[0])

def save_text(elem):
    print('save text')

if __name__ == '__main__':
    loot('', '')
