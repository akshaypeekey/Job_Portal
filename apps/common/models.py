from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.
from django.utils import timezone


class Company(models.Model):
    company_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=30)
    company_place = models.CharField(max_length=20)
    action1 = (
        ('1', 'Aerospace Industry'),
        ('2', 'Agriculture industry'),
        ('3', 'Banking & Financial Industry'),
        ('4', 'Computer Hardware Industry'),
        ('5', 'Education Industry'),
        ('6', 'Electronics Industry'),
        ('7', 'Energy Industry'),
        ('8', 'Entertainment Industry'),
        ('9', 'Health Care Industry'),
        ('10', 'Hotel & Tourism Industry'),
        ('11', 'Manufacturing Industry'),
        ('12', 'Mining Industry'),
        ('13', 'Music Industry'),
        ('14', 'News & Media Industry'),
        ('15', 'Pharmaceutical Industry'),
        ('16', 'Software Industry'),
        ('17', 'Telecommunication industry'),
        ('18', 'Transport Industry'),
        ('19', 'Other'),
    )
    company_industry = models.CharField(max_length=50, choices=action1)
    company_job_positions = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.company_name


class Job(models.Model):
    job_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_place = models.CharField(max_length=20)
    action2 = (
        ('1', 'Full Time'),
        ('2', 'Part Time'),
        ('3', 'Internship'),
        ('4', 'Freelance'),
    )
    job_type = models.CharField(max_length=20, choices=action2)
    job_title = models.CharField(max_length=20)
    action3 = (
        ('1', 'Aerospace Industry'),
        ('2', 'Agriculture industry'),
        ('3', 'Banking & Financial Industry'),
        ('4', 'Computer Hardware Industry'),
        ('5', 'Education Industry'),
        ('6', 'Electronics Industry'),
        ('7', 'Energy Industry'),
        ('8', 'Entertainment Industry'),
        ('9', 'Health Care Industry'),
        ('10', 'Hotel & Tourism Industry'),
        ('11', 'Manufacturing Industry'),
        ('12', 'Mining Industry'),
        ('13', 'Music Industry'),
        ('14', 'News & Media Industry'),
        ('15', 'Pharmaceutical Industry'),
        ('16', 'Software Industry'),
        ('17', 'Telecommunication industry'),
        ('18', 'Transport Industry'),
        ('19', 'Other'),
    )
    job_category = models.CharField(max_length=50, choices=action3)
    job_skills = models.CharField(max_length=50)
    job_description = models.TextField()
    job_vacancy = models.IntegerField()
    job_experience = models.CharField(max_length=20)
    job_salary = models.CharField(max_length=10)
    job_offer_end = models.DateField()
    action4 = (
        ('1', 'active'),
        ('2', 'inactive')
    )
    job_status = models.CharField(max_length=20, choices=action4)

    def __str__(self):
        return '%s (%s)' % (self.job_title, self.job_company)


class Application(models.Model):
    application_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apply_time = models.DateTimeField(default=timezone.now)
    action5 = (
        ('1', 'Applied'),
        ('2', 'Viewed'),
        ('3', 'Processing'),
        ('4', 'Rejected'),
        ('5', 'Accepted'),
        ('6', 'Closed'),
        ('7', 'None'),
    )
    application_status = models.CharField(max_length=20, choices=action5)

    def __str__(self):
        return self.application_id


class Interview(models.Model):
    application_id = models.ForeignKey(Application,on_delete=models.CASCADE)
    interview_place = models.CharField(max_length=20)
    interview_date = models.DateField()
    action6 = (
        ('1', 'Interview Scheduled'),
        ('2', 'Accepted'),
        ('3', 'Declined'),
        ('4', 'Cancelled'),
        ('5', 'Selected'),
        ('6', 'Rejected'),
    )
    interview_status = models.CharField(max_length=20, choices=action6)
    created_date = models.DateField(timezone.now)

    def __str__(self):
        return self.application_id