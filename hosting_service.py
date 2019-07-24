from enum import Enum


class HostingService(Enum):
    GITHUB = 0
    BITBUCKET = 1
    GITLAB = 2
    pass


def get_hosting_service(repo_url: str):
    # TODO actually validate with regexp
    return HostingService.GITHUB