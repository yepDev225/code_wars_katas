import os
import subprocess

def init_git():

    # Initialize a new git repository
    if not os.path.exists('.git'):
        subprocess.run(['git', 'init'], check=True)
        print("Initialized a new git repository.")
    else:
        print("Git repository already initialized.")

def add_files_to_git():
    # Add all files to the git repository
    subprocess.run(['git', 'add', '.'], check=True)
    print("Added all files to the git repository.")

def commit_changes(commit_message):
    # Commit changes with a provided commit message
    try:
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        print(f"Committed changes with message: '{commit_message}'")
    except subprocess.CalledProcessError as e:
        print(f"Failed to commit changes: {e}")

def set_remote(remote_url, remote_name='origin'):
    # Set the remote repository URL
    try:
        subprocess.run(['git', 'branch', '-M', "main"], check=True)
        subprocess.run(['git', 'remote', 'add', remote_name, remote_url], check=True)
        print(f"Set remote '{remote_name}' to {remote_url}.")
    except subprocess.CalledProcessError:
        print(f"Remote '{remote_name}' already exists. Updating URL.")
        subprocess.run(['git', 'remote', 'set-url', remote_name, remote_url], check=True)
        print(f"Updated remote '{remote_name}' to {remote_url}.")

def push_to_remote(remote_name='origin', branch_name='main'):
    # Push changes to the remote repository
    try:
        subprocess.run(['git', 'push', '-u', remote_name, branch_name], check=True)
        print(f"Pushed changes to {remote_name}/{branch_name}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to push changes: {e}")