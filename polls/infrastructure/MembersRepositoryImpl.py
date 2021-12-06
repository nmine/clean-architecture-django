from polls.domain.Member import Member
from polls.domain.MembersRepository import MembersRepository


class MembersRepositoryImpl(MembersRepository):
    def retrieve_member(self, memberId: str) -> Member:
        member = Member('Tom', 'Hanks')
        return member
