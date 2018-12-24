# Remote-Magician
A utility for applying default settings (such as default branches, branch protection, etc.) to remote repositories

## Usage
```
Usage: magician.py [OPTIONS]

Options:
  -r, --repo TEXT           A remote repository URL. NOTE: This argument is
                            mutually exclusive with repos_file
  -f, --repos-file PATH     A file containing a remote repository URL in each
                            row. NOTE: This argument is mutually exclusive
                            with repo
  -s, --settings-file PATH  A file settings to use in the given
                            repository/repositories.  [required]
  --help                    Show this message and exit.
```