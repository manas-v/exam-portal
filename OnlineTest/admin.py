from django.contrib import admin
from .models import StudentDetails, StudentLoginDetails, StudentSubjects
from .models import TeacherDetails, TeacherLoginDetails, TeacherSubjects
from .models import LoginDetails, PhyTest, ChemTest, MathTest, BioTest, CseTest
from .models import Test


admin.site.register(StudentDetails)
admin.site.register(StudentLoginDetails)
admin.site.register(StudentSubjects)
admin.site.register(TeacherDetails)
admin.site.register(TeacherLoginDetails)
admin.site.register(TeacherSubjects)
admin.site.register(LoginDetails)
admin.site.register(PhyTest)
admin.site.register(ChemTest)
admin.site.register(MathTest)
admin.site.register(BioTest)
admin.site.register(CseTest)
admin.site.register(Test)