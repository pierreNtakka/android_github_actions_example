import os
import sys
import argparse
from gradle_utils import read_gradle_properties
from gradle_utils import update_gradle_properties

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        
def main():
    parser = argparse.ArgumentParser(description='Configure App Distribution Key')
    parser.add_argument('--appDistrAuthFileJson', type=str, help='The App Distribution Auth File JSON')
    args = parser.parse_args()

    appDistrAuthFileJson = args.appDistrAuthFileJson

    config_dir = 'config'
    create_directory(config_dir)

    file_path = os.path.join(config_dir, 'firebase-app-distr-key.json')

    if appDistrAuthFileJson:
        with open(file_path, 'w') as file:
            file.write(appDistrAuthFileJson)

    # Imposta la variabile d'ambiente per il percorso del file
    os.environ['GITHUB_ACTIONS_EXAMPLE_APP_DISTR_FILE_KEY'] = file_path
    with open(os.getenv('GITHUB_ENV'), 'a') as env_file:
        env_file.write(f"GITHUB_ACTIONS_EXAMPLE_APP_DISTR_FILE_KEY={file_path}\n")


if __name__ == "__main__":
    main()