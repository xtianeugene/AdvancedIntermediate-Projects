import shutil, os, datetime

def backup(src, dest_root="backups"):
    stamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    dest = os.path.join(dest_root, f"backup_{stamp}")
    shutil.copytree(src, dest)
    print("Backed up to", dest)

if __name__ == "__main__":
    backup(input("Folder to back up: "))