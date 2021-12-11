from django.http import HttpResponse
from django.views import View


class ViewWrapper(View):
    usecaseFactory = None

    def get(self, request, question_id: int, question_id2: int):
        member = self.usecaseFactory.get().execute()
        return HttpResponse("You're looking at question.")
