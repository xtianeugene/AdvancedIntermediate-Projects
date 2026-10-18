import json, os, hashlib, getpass

FILE = "vault.json"
SALT = "u_reg_2024"

def hash_master(pw):
    return hashlib.sha256((SALT + pw).encode()).hexdigest()

def load():
    return json.load(open(FILE)) if os.path.exists(FILE) else {"master": None, "entries": {}}

def save(v):
    json.dump(v, open(FILE, "w"), indent=2)

def main():
    v = load()
    if not v["master"]:
        v["master"] = hash_master(getpass.getpass("Set master password: "))
        save(v)
        print("Master set.")
    elif hash_master(getpass.getpass("Master password: ")) != v["master"]:
        print("Wrong password.")
        return
    while True:
        c = input("1. Add 2. View 3. Quit: ")
        if c == "1":
            site = input("Site: ")
            v["entries"][site] = getpass.getpass("Password: ")
            save(v)
        elif c == "2":
            print(v["entries"].get(input("Site: "), "Not found"))
        else:
            break

if __name__ == "__main__":
    main()