import os


def mkdir(path, name):

    folder = os.path.exists(path+name)
    if not folder:
        os.mkdir(path+name)
    else:
        print(f'The folder "{name}" already exists')


