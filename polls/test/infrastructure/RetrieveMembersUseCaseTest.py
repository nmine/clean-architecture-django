"""Tests module."""

from django.test import SimpleTestCase
from unittest.mock import MagicMock
from polls.application.usecases.RetrieveMembersUseCase import RetrieveMembersUseCase
from polls.domain.Member import Member
from polls.domain.MembersRepository import MembersRepository


class RetrieveMembersUseCaseTest(SimpleTestCase):

    def test_retrieve_members_useCase(self):
        # Given
        repository = MembersRepository()
        member = Member('test', 'test')
        repository.retrieve_member = MagicMock(return_value=member)
        # WHen
        usecase = RetrieveMembersUseCase(repository)
        result = usecase.execute()
        # Then
        self.assertEqual(result.firstname, "test")
