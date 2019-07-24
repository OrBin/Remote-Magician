import click
from typing import Union, List

from hosting_service import get_hosting_service
from not_required_if import NotRequiredIf


@click.command()
@click.option('-r',
              '--repo',
              #required=True,
              cls=NotRequiredIf,
              not_required_if='repos_file',
              type=str,
              help='A remote repository URL.')
@click.option('-f',
              '--repos-file',
              #required=True,
              cls=NotRequiredIf,
              not_required_if='repo',
              type=click.Path(exists=True),
              help='A file containing a remote repository URL in each row.')
@click.option('-s',
              '--settings-file',
              required=True,
              type=click.Path(exists=True),
              help='A file settings to use in the given repository/repositories.')
def main(repo: str, repos_file: str, settings_file: str):
    if repo:
        repos = [repo]
    else:
        with open(repos_file, 'r') as file:
            repos = [line.rstrip() for line in file.readlines()]

    repo_to_hosting_service = {repo: get_hosting_service(repo) for repo in repos}

    for repo, hosting_service in repo_to_hosting_service.items():
        print(repo, hosting_service)



if __name__ == '__main__':
    main()
