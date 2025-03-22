import sys

def read_gradle_properties(file_name):
    properties = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                if not line.startswith('#') and '=' in line:
                    key, value = line.strip().split('=', 1)
                    properties[key] = value
    except FileNotFoundError:
        print(f"Errore: Il file {file_name} non è stato trovato.")
        sys.exit(1)
    return properties


def update_gradle_properties(file_name, properties):
    lines = []
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Errore: Il file {file_name} non è stato trovato.")
        return

    with open(file_name, 'w') as file:
        for line in lines:
            if not line.startswith('#') and '=' in line:
                key = line.split('=')[0].strip()
                if key in properties:
                    line = f"{key}={properties[key]}\n"
            file.write(line)