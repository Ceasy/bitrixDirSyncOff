import os
import ctypes


def check_disk(disk):
    if os.path.exists(disk + ':\\'):
        return True
    else:
        return False


def find_dir(disk, dir):
    for root, dirs, files in os.walk(disk + ':\\'):
        for name in dirs:
            if name == dir:
                print(os.path.join(root, name))
                path = os.path.join(root, name)
                return path
    return None


def dir_move(path, dir, name_dir_backup):
    if path is not None:
        if os.path.exists(os.path.dirname(path) + '\\..\\' + name_dir_backup):
            print(f'Dir "{name_dir_backup}" already exists')
            ctypes.windll.user32.MessageBoxW(0, "Операция прерванна: вы уже переносили папку...", "ERROR", 0)
            return False
        else:
            os.rename(path, os.path.dirname(path) + '\\' + name_dir_backup + '\\' + dir)
            print(f'Dir "{name_dir_backup}" is present')
            return True
    else:
        return False


def create_dir(path, name_dir_backup):
    if path is not None:
        if os.path.exists(path + '\\..\\' + name_dir_backup):
            print(f'"{name_dir_backup}" folder already exists')
            return True
        if not os.path.exists(os.path.dirname(path) + '\\..\\' + name_dir_backup):
            os.mkdir(os.path.dirname(path) + '\\' + name_dir_backup)
            print(f'Create dir "{name_dir_backup}"')
            return True
        else:
            print(f'Dir "{name_dir_backup}" is present')
            return True
    else:
        print('Path is None')
        return False


def main():
    name_dir_backup = 'backup_bdisk'
    for disk in 'xyzc':
        if check_disk(disk):
            print(f'Disk {disk} is present')
            path = find_dir(disk, 'BDisk')
            if create_dir(path, name_dir_backup):
                if dir_move(path, 'BDisk', name_dir_backup):
                    ctypes.windll.user32.MessageBoxW(0, "Готово!", "successful", 0)
        else:
            print(f'Disk {disk} is not present')


if __name__ == '__main__':
    main()
