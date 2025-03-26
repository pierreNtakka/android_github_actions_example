import os
import shutil

def delete_directory(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"Directory {path} rimossa con successo.")
    else:
        print(f"La directory {path} non esiste.")

def unset_environment_variable(var_name):
    if var_name in os.environ:
        os.environ.pop(var_name)
        print(f"Variabile d'ambiente {var_name} rimossa con successo.")
    else:
        print(f"La variabile d'ambiente {var_name} non è impostata.")

def main():
    # Esempio di utilizzo
    directory_to_delete = 'config'
    env_var_to_unset = 'GITHUB_ACTIONS_EXAMPLE_APP_DISTR_FILE_KEY'

    delete_directory(directory_to_delete)
    unset_environment_variable(env_var_to_unset)

if __name__ == "__main__":
    main()