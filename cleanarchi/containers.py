from dependency_injector import containers, providers

from polls.infrastructure.MembersRepositoryImpl import MembersRepositoryImpl
from polls.application.usecases.RetrieveMembersUseCase import RetrieveMembersUseCase


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    memberRepository = MembersRepositoryImpl()
    useCase = providers.Factory(
        RetrieveMembersUseCase,
        memberRepository=memberRepository
    )
