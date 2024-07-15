# cli.py
import click
from nlp_helper import get_git_command
from git_commands import execute_git_command
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

@click.command()
@click.argument('input_text', nargs=-1)
def cli(input_text):
    prompt = " ".join(input_text)
    git_command = get_git_command(f"Translate this to a Git command: {prompt}")
    #click.echo(f"Executing: {git_command}")
    result = execute_git_command(git_command)
    #click.echo(result)

if __name__ == '__main__':
    cli()
