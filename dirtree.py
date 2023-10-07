import os
import threading
import json
import time
from tkinter import messagebox as msg

serverdir = ""
pldirvar = ()
plapppldirvar = ()

def dirthread():
    global servertree, plapppldirvar, pldirvar
    while True:
        try:
            servertree = dirtree(serverdir)
            temp = list(servertree["plugins"].keys())
            temp.remove("*files")
            temp += servertree["plugins"]["*files"]
        except Exception as e:
            msg.showerror(title="Directory Error", message=e)
        try:
            pldirvar = tuple(temp)
        except:pass
        try:
            plapppldirvar = tuple(temp)
        except:pass
        time.sleep(1)

def treethread():
    global servertree
    servertree = dirtree(serverdir)
    with open("dir.json", "w", encoding="utf-8") as f:
        json.dump(servertree, f, indent=4, ensure_ascii=False)
    threading.Thread(target=dirthread, name="directory").start()

def dirtree(root_dir):
    result = {}
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            result[item] = dirtree(item_path)
        else:
            result.setdefault("*files", []).append(item)
    return result
