import os

def util_open(name):

    if name=="settings" or name=="setting":
        os.system("gnome-control-center")
        return 1
    elif name=="chrome" or name=="google chrome" or name=="browser" or name=="web browser":
        os.system("google-chrome")
        return 1
    elif name=="firefox" or name=="mozilla" or name=="mozilla firefox":
        os.system("firefox")
        return 1
    elif name=="file" or name=="files":
        os.system("nautilus")
        return 1
    elif name=="terminal" or name=="shell":
        os.system("gnome-terminal")
        return 1
    elif name=="office" or name=="libre office":
        os.system("libreoffice")
        return 1
    else:
        print("else")
        return 0
