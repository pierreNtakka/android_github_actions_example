import os
import requests
import sys

def get_release_id(tag_to_delete, github_repository, github_token):
    url = f"https://api.github.com/repos/{github_repository }/releases/tags/{tag_to_delete}"
    headers = {
        "Authorization": f"Bearer {github_token}"
    }
    response = requests.get(url, headers=headers)
    
    status_code = response.status_code
    if status_code == 200:
        print(f"La release associata al tag {tag_to_delete} è stata trovata.")
        releases = response.json()

        if 'id' in releases:
            return releases['id']
        else:
            print(f"Errore: Nessun ID trovato per il tag {tag_to_delete}.")
        return None
    
    else:
        print(f"Errore: La release associata al tag {tag_to_delete} non è stata trovata.")
        return None

def delete_release(github_repository, release_id, github_token):
    url = f"https://api.github.com/repos/{github_repository}/releases/{release_id}"
    headers = {
        "Authorization": f"Bearer {github_token}"
    }
    response = requests.delete(url, headers=headers)
    return response.status_code



def main():
    git_hub_repository = os.getenv('GITHUB_REPOSITORY')
    tag_to_delete = os.getenv('TAG_TO_DELETE')
    github_token = os.getenv('GITHUB_TOKEN')

    if not git_hub_repository or not tag_to_delete or not github_token:
        print("Errore: Assicurati che le variabili d'ambiente GITHUB_REPOSITORY, TAG_TO_DELETE e GITHUB_TOKEN siano impostate.")
        sys.exit(1)

    release_id = get_release_id(tag_to_delete, git_hub_repository, github_token)
    
    if release_id:
        print(f"La release associata al tag {tag_to_delete} esiste, procedo con la cancellazione.")
        status_code = delete_release(github_token, release_id, github_token)
        
        if status_code == 204:
            print(f"La release associata al tag {tag_to_delete} è stata cancellata con successo.")
        elif status_code == 404:
            print(f"Errore: La release associata al tag {tag_to_delete} non è stata trovata per la cancellazione.")
            sys.exit(1)
        else:
            print(f"Errore nella cancellazione. Codice di stato: {status_code}")
            sys.exit(1)
    else:
        print(f"La release associata al tag {tag_to_delete} non esiste, niente da cancellare.")

    #Non è necessario è solo per avere un esempio di output. 'a' sta per append, quindi aggiunge alla fine del file.
    with open(os.getenv('GITHUB_OUTPUT'), 'a') as output_file:
        output_file.write(f"release_deleted=true\n")


if __name__ == "__main__":
    main()