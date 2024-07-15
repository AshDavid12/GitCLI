import git

def execute_git_command(command: str):
    try:
        repo = git.Repo('.')  # Assumes you're running this in a Git repository
        result = repo.git.execute(command.split())
        return result
    except Exception as e:
        return str(e)
