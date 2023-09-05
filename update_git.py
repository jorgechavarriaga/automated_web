#!/usr/bin/env python3

from git import Repo


def update_github_repo(repo_path, commit_message):
    try:
        repo = Repo(repo_path)
        repo.git.add("--all")
        repo.index.commit(commit_message)
        origin = repo.remote(name="origin")
        origin.push()
#        print("Repository updated successfully.")
        return True
    except Exception as e:
#        print("An error occurred:", str(e))
        return False



#if __name__ == "__main__":
#    repository_path = "/ruta/a/tu/repositorio"
#    commit_msg = "Actualización automática"

#    update_github_repo(repository_path, commit_msg)
