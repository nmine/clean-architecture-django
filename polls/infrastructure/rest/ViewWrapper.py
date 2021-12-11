from django.http import HttpResponse
from django.views import View


class ViewWrapper(View):
    usecaseFactory = None

    def get(self, request, *args, **kwargs):
        member = self.usecaseFactory.get().execute()
        return HttpResponse("You're looking at question.")
