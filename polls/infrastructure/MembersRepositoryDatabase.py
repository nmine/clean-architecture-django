from polls.domain.Member import Member
from polls.domain.MembersRepository import MembersRepository
from polls.infrastructure.models.models import Question


class MembersRepositoryDatabase(MembersRepository):
    def retrieve_member(self, memberId: str) -> Member:
        Question.objects.all()
        member = Member('Tom', 'Hanks')
        return member
