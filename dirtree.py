import os

def dirtree(root_dir):
    result = {}
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            result[item] = dirtree(item_path)
        else:
            result.setdefault("*files", []).append(item)
    return result