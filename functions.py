import os
import subprocess


def newFolder(path, nameofile):
    os.system('cd "{}"'.format(path))
    os.system("mkdir {}".format(nameofile))
    print("Project folder created...")

def newFile(path, name, ending):
    make = 'cd "{}" ; touch {}.{}'.format(path, name, ending)

    os.system(make)
    print("File created...")

def CopytoCLIP(path):
    subprocess.run("pbcopy", universal_newlines=True, input=path)
    print("Path copied to clipboard...")

def openTE(editor, path):
    open = 'open -a "{}" {}'.format(editor, path)
