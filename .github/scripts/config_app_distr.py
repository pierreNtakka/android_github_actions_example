import os
import sys

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        
def main():
    appDistrAuthFileJson = os.getenv('APP_DISTR_FILE_CONTENT_KEY')
    
    if not appDistrAuthFileJson:
        print("Errore: Assicurati che la variabile d'ambiente APP_DISTR_FILE_CONTENT_KEY sia impostata.")
        sys.exit(1)

    config_dir = 'config'
    create_directory(config_dir)

    file_path = os.path.join(config_dir, 'firebase-app-distr-key.json')

    if appDistrAuthFileJson:
        with open(file_path, 'w') as file:
            file.write(appDistrAuthFileJson)

    os.environ['GITHUB_ACTIONS_EXAMPLE_APP_DISTR_FILE_KEY'] = file_path
    with open(os.getenv('GITHUB_ENV'), 'a') as env_file:
        env_file.write(f"GITHUB_ACTIONS_EXAMPLE_APP_DISTR_FILE_KEY={file_path}\n")


if __name__ == "__main__":
    main()