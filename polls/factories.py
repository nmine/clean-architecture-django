from polls.application.usecases.RetrieveMembersUseCase import RetrieveMembersUseCase
from polls.infrastructure.MembersRepositoryDatabase import MembersRepositoryDatabase


class MemberRepositoryDatabaseFactory(object):

    @staticmethod
    def get():
        return MembersRepositoryDatabase()


class RetrieveMembersUseCaseFactory(object):

    @staticmethod
    def get():
        return RetrieveMembersUseCase(MemberRepositoryDatabaseFactory.get())
