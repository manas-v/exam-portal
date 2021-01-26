from django.db import models


class StudentDetails(models.Model):
    SNo = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phno = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    date = models.DateField(max_length=10)

    def __int__(self):
        return self.SNo


class StudentLoginDetails(models.Model):
    studentdetails = models.ForeignKey(StudentDetails, default=0, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=20, default=0)
    password = models.CharField(max_length=20)

    def __int__(self):
        return self.studentdetails


class StudentSubjects(models.Model):
    studentdetails = models.ForeignKey(StudentDetails, default=0, on_delete=models.CASCADE)
    phy = models.CharField(max_length=3, blank=True, default='off')
    chem = models.CharField(max_length=3, blank=True, default='off')
    math = models.CharField(max_length=3, blank=True, default='off')
    bio = models.CharField(max_length=3, blank=True, default='off')
    cse = models.CharField(max_length=3, blank=True, default='off')

    def __int__(self):
        return self.studentdetails


class TeacherDetails(models.Model):
    TNo = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phno = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    date = models.DateField(max_length=10)

    def __int__(self):
        return self.TNo


class TeacherLoginDetails(models.Model):
    teacherdetails = models.ForeignKey(TeacherDetails, default=0, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=20, default=0)
    password = models.CharField(max_length=20)

    def __int__(self):
        return self.teacherdetails


class TeacherSubjects(models.Model):
    teacherdetails = models.ForeignKey(TeacherDetails, default=0, on_delete=models.CASCADE)
    phy = models.CharField(max_length=3, blank=True)
    chem = models.CharField(max_length=3, blank=True)
    math = models.CharField(max_length=3, blank=True)
    bio = models.CharField(max_length=3, blank=True)
    cse = models.CharField(max_length=3, blank=True)

    def __int__(self):
        return self.teacherdetails


class LoginDetails(models.Model):
    index = models.IntegerField(default=0)
    user_id = models.CharField(max_length=20, default=0)

    def __int__(self):
        return self.user_id


class PhyTest(models.Model):
    user_id = models.CharField(max_length=20, default=0)
    test_id = models.CharField(max_length=7)
    index = models.IntegerField(default=0)
    qn = models.TextField(max_length=300)
    a1 = models.TextField(max_length=300)
    a2 = models.TextField(max_length=300)
    a3 = models.TextField(max_length=300)
    a4 = models.TextField(max_length=300)
    ans = models.CharField(max_length=2)

    def __int__(self):
        return self.test_id


class ChemTest(models.Model):
    user_id = models.CharField(max_length=20, default=0)
    test_id = models.CharField(max_length=7)
    index = models.IntegerField(default=0)
    qn = models.TextField(max_length=300)
    a1 = models.TextField(max_length=300)
    a2 = models.TextField(max_length=300)
    a3 = models.TextField(max_length=300)
    a4 = models.TextField(max_length=300)
    ans = models.CharField(max_length=2)

    def __int__(self):
        return self.test_id


class MathTest(models.Model):
    user_id = models.CharField(max_length=20, default=0)
    test_id = models.CharField(max_length=7)
    index = models.IntegerField(default=0)
    qn = models.TextField(max_length=300)
    a1 = models.TextField(max_length=300)
    a2 = models.TextField(max_length=300)
    a3 = models.TextField(max_length=300)
    a4 = models.TextField(max_length=300)
    ans = models.CharField(max_length=2)

    def __int__(self):
        return self.test_id


class BioTest(models.Model):
    user_id = models.CharField(max_length=20, default=0)
    test_id = models.CharField(max_length=7)
    index = models.IntegerField(default=0)
    qn = models.TextField(max_length=300)
    a1 = models.TextField(max_length=300)
    a2 = models.TextField(max_length=300)
    a3 = models.TextField(max_length=300)
    a4 = models.TextField(max_length=300)
    ans = models.CharField(max_length=2)

    def __int__(self):
        return self.test_id


class CseTest(models.Model):
    user_id = models.CharField(max_length=20, default=0)
    test_id = models.CharField(max_length=7)
    index = models.IntegerField(default=0)
    qn = models.TextField(max_length=300)
    a1 = models.TextField(max_length=300)
    a2 = models.TextField(max_length=300)
    a3 = models.TextField(max_length=300)
    a4 = models.TextField(max_length=300)
    ans = models.CharField(max_length=2)

    def __int__(self):
        return self.test_id


class Test(models.Model):
    studentdetails = models.ForeignKey(StudentDetails, default=0, on_delete=models.CASCADE)
    teacherdetails = models.ForeignKey(TeacherDetails, default=0, on_delete=models.CASCADE)
    subject = models.CharField(max_length=10)
    test_id = models.CharField(max_length=10, default=0)
    # date = models.DateField(blank=True)
    # time = models.DateTimeField(blank=True)
    a1 = models.CharField(max_length=2)
    a2 = models.CharField(max_length=2)
    a3 = models.CharField(max_length=2)
    a4 = models.CharField(max_length=2)
    a5 = models.CharField(max_length=2)
    marks = models.IntegerField(default=0)

    def __int__(self):
        return self.test_id



