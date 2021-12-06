from polls.domain.Member import Member
from polls.domain.MembersRepository import MembersRepository


class RetrieveMembersUseCase:
    def __init__(self, memberRepository: MembersRepository):
        self.memberRepository = memberRepository

    def execute(self) -> Member:
        return Member('sdq', 'qsd')
