"""Tests module."""

from django.test import SimpleTestCase
from unittest.mock import MagicMock
from polls.application.usecases.RetrieveMembersUseCase import RetrieveMembersUseCase
from polls.domain.Member import Member
from polls.domain.MembersRepository import MembersRepository


class IndexTests(SimpleTestCase):

    def test_index_no_results(self):
        repository = MembersRepository()
        member = Member('test', 'test')
        repository.retrieve_member = MagicMock(return_value=member)
        useCase = RetrieveMembersUseCase(repository)
        result = useCase.execute()
        self.assertEqual(result.firstname, "test")
