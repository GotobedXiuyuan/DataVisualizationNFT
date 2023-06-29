import hashlib
import sys

def generate_hash(file_path):
    with open(file_path, "rb") as f:
        bytes = f.read()
        readable_hash = hashlib.sha256(bytes).hexdigest()
    return readable_hash

if __name__ == "__main__":
    file_path = sys.argv[1]
    print(generate_hash(file_path))
