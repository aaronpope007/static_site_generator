import os
import shutil

def copy_static(source_path, dest_path):
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    os.mkdir(dest_path)

    items_to_copy = os.listdir(source_path)

    for item in items_to_copy:
        from_path = os.path.join(source_path, item)
        to_path = os.path.join(dest_path, item)

        if os.path.isfile(from_path):
            print(f'from path is {from_path}')
            print(f'to path is {to_path}')
            shutil.copy(from_path, to_path)
        else:
            copy_static(from_path, to_path)
