# Finding Files

import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if path == "" or len(os.listdir(path)) == 0 or suffix == "":
        return []

    path_content = os.listdir(path)
    folders = []
    files = []

    for content in path_content:
        if os.path.isfile(path + "/" + content) and content.endswith(suffix):
            files.append(path + "/" + content)
        else:
            if os.path.isdir(path + "/" + content):
                folders.append(content)

    for folder in folders:
        folder_files = find_files(suffix=suffix, path=path + "/" + folder)
        files.extend(folder_files)

    return files


root_path = os.getcwd() + "/testdir"

print(find_files(suffix="h", path=root_path))
# returns ['t1.h', 'b.h', 'a.h', 'a.h']

print(find_files(suffix="c", path=root_path))
# returns ['t1.c', 'b.c', 'a.c', 'a.c']

print(find_files(suffix="d", path=root_path))
# returns []

print(find_files(suffix="gitkeep", path=root_path))
# returns ['.gitkeep', '.gitkeep']

print(find_files(suffix="", path=root_path))
# returns []

print(find_files(suffix="", path=""))
# returns []