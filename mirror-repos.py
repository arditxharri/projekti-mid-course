import subprocess
import os

def mirror_repository(source_repo_url, destination_repo_url):
    """Mirrors a repository from one location to another.

    Args:
        source_repo_url: The URL of the source repository.
        destination_repo_url: The URL of the destination repository.
    """

    # Create a temporary directory.
    tmp_dir = os.path.join(os.getcwd(), "tmp")
    os.makedirs(tmp_dir, exist_ok=True)

    # Clone the source repository to the temporary directory.
    subprocess.call(["git", "clone", "--mirror", source_repo_url, tmp_dir])

    # Add the destination repository as a remote.
    subprocess.call(["git", "remote", "add", "destination-repo", destination_repo_url], cwd=tmp_dir)

    # Push all changes to the destination repository.
    subprocess.call(["git", "push", "--mirror", "destination-repo"], cwd=tmp_dir)

    # Remove the temporary directory.
    subprocess.call(["rm", "-rf", tmp_dir])


if __name__ == "__main__":
    source_repo_url = input("Enter the source repository URL: ")
    destination_repo_url = input("Enter the destination repository URL: ")

    mirror_repository(source_repo_url, destination_repo_url)
