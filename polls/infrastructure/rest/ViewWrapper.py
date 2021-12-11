from django.http import HttpResponse

from polls.factories import RetrieveMembersUseCaseFactory


class ViewWrapper:

    def __init__(self, usecaseFactory: RetrieveMembersUseCaseFactory):
        self.usecaseFactory = usecaseFactory

    def detail(self, request, question_id):
        member = self.usecaseFactory.get().execute()
        return HttpResponse("You're looking at question %s." % question_id)
