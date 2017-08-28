from django.test import TestCase
from .models import Problem
import problem.models as pm

class TestProblem(TestCase):

    @classmethod
    # sets up data for the whole test suite.
    def setUpTestData(cls):
        cls.p1 = Problem.objects.create(title='P1 title', description="P1 description")
        cls.p2 = Problem.objects.create(title='P2 title', description="P2 description")
        cls.p3 = Problem.objects.create(title='P3 title', description="P3 description")

    # tests db insertion.
    def test_db_insertion(self):
        self.assertIs(1, self.p1.id)

    # tests if p2 gets the next id available after p1.
    # Note that if we do not save p2, then it does not have an id and test would fail.
    def test_db_incremental_id(self):
        self.assertEqual(2, self.p2.id)

    # tests if a modification in fields updates the db.
    def test_db_field_modification(self):
        Problem.objects.filter(id=self.p1.id).update(title='P1 new title')
        self.p1.refresh_from_db()
        self.assertEqual('P1 new title', self.p1.title)

    # tests if post is getting an up vote.
    def test_init_votes(self):
        self.assertIs(0, self.p1.up_votes)
        self.assertIs(0, self.p1.down_votes)
        self.assertIs(0, self.p1.diff_votes)

    # tests if post is getting a down vote.
    def test_up_vote(self):
        self.p2.up_vote()
        self.assertIs(1, self.p2.up_votes)

    def test_down_vote(self):
        self.p2.down_vote()
        self.assertIs(1, self.p2.down_votes)

    # tests if post is now having the difference between up and down votes.
    def test_diff_vote(self):
        for i in range(0, 4):
            self.p3.up_vote()
        self.assertIs(4, self.p3.up_votes)
        self.assertIs(0, self.p3.down_votes)
        self.assertIs(4, self.p3.diff_votes)

    # tests that this function returns the most recent objects.
    def test_newest_problems(self):
        newest_list = '[<Problem: P3 title>, <Problem: P2 title>, <Problem: P1 title>]'
        self.assertEqual(newest_list, str(pm.get_top_rated_problems()))

    # tests that this function returns the top rated problems
    def test_top_rated_problems(self):
        top_rated_list = '[<Problem: P3 title>, <Problem: P2 title>, <Problem: P1 title>]'
        self.assertEqual(top_rated_list, str(pm.get_top_rated_problems()))
