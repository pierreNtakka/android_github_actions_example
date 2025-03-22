import os
import requests
import sys

def get_version_id(package_name, version_to_delete, github_token):
    url = f"https://api.github.com/user/packages/maven/{package_name}/versions"
    headers = {
        "Authorization": f"Bearer {github_token}"
    }
    response = requests.get(url, headers=headers)
    
    status_code = response.status_code
    
    if status_code == 200:
        print(f"La release associata al tag {tag_to_delete} è stata trovata.")
        versions = response.json()
    
        for version in versions:
            if version['name'] == version_to_delete:
                return version['id']
        return None 
    else :
        print(f"Errore: La richiesta non è andata a buon fine. Codice di stato: {status_code}")
        return None 
   

def delete_version(package_name, version_id, github_token):
    url = f"https://api.github.com/user/packages/maven/{package_name}/versions/{version_id}"
    headers = {
        "Authorization": f"Bearer {github_token}"
    }
    response = requests.delete(url, headers=headers)
    return response.status_code

def main():
    package_name = os.getenv('PACKAGE_NAME')
    version_to_delete = os.getenv('VERSION_TO_DELETE')
    github_token = os.getenv('GITHUB_TOKEN')

    if not package_name or not version_to_delete or not github_token:
        print("Errore: Assicurati che le variabili d'ambiente PACKAGE_NAME, VERSION_TO_DELETE e GITHUB_TOKEN siano impostate.")
        sys.exit(1)

    version_id = get_version_id(package_name, version_to_delete, github_token)
    
    if version_id:
        print(f"La versione {version_to_delete} esiste, procedo con la cancellazione.")
        status_code = delete_version(package_name, version_id, github_token)
        
        if status_code == 204:
            print(f"La versione {version_to_delete} è stata cancellata con successo.")
        elif status_code == 404:
            print(f"Errore: La versione {version_to_delete} non è stata trovata per la cancellazione.")
            sys.exit(1)
        else:
            print(f"Errore nella cancellazione. Codice di stato: {status_code}")
            sys.exit(1)
    else:
        print(f"La versione {version_to_delete} non esiste, niente da cancellare.")

if __name__ == "__main__":
    main()