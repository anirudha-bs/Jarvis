import os

def util_open(name):

    if name=="settings":
        os.system("gnome-control-center")
        return 1
    elif name=="chrome":
        os.system("google-chrome")
        return 1
    elif name=="firefox":
        os.system("firefox")
        return 1
    elif name=="file manager" or name=="files":
        os.system("nautilus")
        return 1
    elif name=="terminal":
        os.system("gnome-terminal")
        return 1
    else:
    	return 0
