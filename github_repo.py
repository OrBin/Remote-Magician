from remote_repo import RemoteRepo


class GithubRepo(RemoteRepo):
    def set_branch_protection(self):
        raise NotImplementedError()
