from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.db import models

'''
Table: Problem  -> contains the fields of a single problem
@title             A brief problem title
@description       A more detailed problem description
'''


# TODO need to define a fixed number of newest problems to be shown
# TODO let us say for the sake of argument that this number is 4.
def get_newest_problems():
    newest_list = list(Problem.objects.order_by('created_at'))
    newest_list = newest_list[-4:]
    newest_list.reverse()
    return newest_list


def get_top_rated_problems():
    top_rated_list = list(Problem.objects.order_by('diff_votes'))
    top_rated = top_rated_list[-4:]
    top_rated.reverse()
    return top_rated


class Problem(models.Model):
    title = models.CharField(max_length=200)  # table field, type & size.
    description = models.TextField(default='This is a default project description')
    # not to be touched by the user, used for the home page 'new', 'top' etc.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    diff_votes = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('problem:problem_page', kwargs={'problem_id': self.pk})

    # TODO user.id as foreign key.

    def up_vote(self):
        self.up_votes = self.up_votes + 1
        self.diff_vote()
        return self.up_votes

    def down_vote(self):
        self.down_votes = self.down_votes + 1
        self.diff_vote()
        return self.down_votes

    def diff_vote(self):
        self.diff_votes = self.up_votes - self.down_votes
        self.save()
        return self.diff_votes

    # A string representation of the problem object used in the db shell.
    def __str__(self):
        return str(self.title)


class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, default=1)
    description = models.TextField(default='This is a default solution description')
    file = models.FileField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    diff_votes = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('problem:solution_page', kwargs={'solution_id': self.pk, 'problem_id': self.problem.pk})

    def alert_subscribers(self, full_url):
        subscribers = self.problem.subscriber_set.all()
        subject = 'A solution to the problem you submitted has been submitted!'
        message = 'Someone submitted a solution to your problem:' + self.problem.title + \
                  '. Visit Spark to find out more. The solution link is below: ' + full_url
        for subscriber in subscribers:
            subscriber.email_user(subject, message)

    def up_vote(self):
        self.up_votes = self.up_votes + 1
        self.diff_vote()
        return self.up_votes

    def down_vote(self):
        self.down_votes = self.down_votes + 1
        self.diff_vote()
        return self.down_votes

    def diff_vote(self):
        self.diff_votes = self.up_votes - self.down_votes
        self.save()
        return self.diff_votes

    def __str__(self):
        return str(self.id)


class Subscriber(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    email = models.EmailField(max_length=300)

    def __str__(self):
        return str(self.id) + ' -> Email: ' + self.email

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])