from abc import ABC, abstractmethod


class RemoteRepo(ABC):
    def __init__(self, url):
        self.__url = url

    @abstractmethod
    def set_branch_protection(self):
        pass