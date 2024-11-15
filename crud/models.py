from django.db import models
from django.utils.timezone import now

# User model
class User(models.Model):
    # CharField for user's first name
    first_name = models.CharField(
        null=False, 
        max_length=30,
        default='john'
    )
    # CharField for user's last name
    last_name = models.CharField(
        null=False,
        max_length=30,
        default='doe'
    )
    # CharField for user's date for birth
    dob = models.DateField(
        null=True
    )

    # Create a toString method for object string reprensen
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Instructor model that inherits from User
class Instructor(User):
    full_time = models.BooleanField(
        default=True
    )
    total_learners = models.IntegerField()

    # Create a toString method for object string reprensentation
    def __str__(self):
        return "First name: " + self.first_name + ", " + \
                "Last name: " + self.last_name + ", " + \
                "Full time: " + str(self.full_time) + ", " + \
                "Total learners: " + str(self.total_learners)

# Learner model
class Learner(User):
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data scientist'
    DATABASE_ADMIN = 'dba'
    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT
    )
    social_links = models.URLField(max_length=200)

    # Create a toString method for object string reprensentation
    def __str__(self):
        return "First name: " + self.first_name + ", " + \
                "Last name: " + self.last_name + ", " + \
                "Date of Birth: " + str(self.dob) + ", " + \
                "Occupation: " + self.occupation + ", " + \
                "Social links: " + self.social_links

# Course model
class Course(models.Model):
    name = models.CharField(
        null=False,
        max_length=100,
        default='online course'
    )
    description = models.CharField(max_length=500)
    # Many to many relationship with Instructor
    instructors = models.ManyToManyField(Instructor)
    learners = models.ManyToManyField(Learner, through='Enrollment')
    # Create a toString method for object string reprensentation
    def __str__(self):
        return f'Name: {self.name}, Description: {self.description}'
    
# Lesson model
class Lesson(models.Model):
    title = models.CharField(
        max_length=200,
        default='title'
    )
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()

# Enrollment model
class Enrollment(models.Model):
    AUDIT = 'audit'
    HONOR = 'honor'
    COURSE_MODES = [
        (AUDIT, 'Audit'),
        (HONOR, 'Honor'),
    ]
    # Add a learner foreign key
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    # Add a course foreign key
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Enrollment date
    date_enrolled = models.DateField(default=now)
    # Enrollment mode
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)