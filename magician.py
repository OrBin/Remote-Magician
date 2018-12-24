import click
from typing import Union, List
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
              type=click.Path(),
              help='A file containing a remote repository URL in each row.')
@click.option('-s',
              '--settings-file',
              required=True,
              type=click.Path(),
              help='A file settings to use in the given repository/repositories.')
def main(repo: str, repos_file: click.Path, settings_file: click.Path):
    print(repo)
    print(repos_file)
    print(settings_file)


if __name__ == '__main__':
    main()
