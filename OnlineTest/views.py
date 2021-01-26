from django.shortcuts import render, redirect
from django.contrib import messages
from .models import StudentDetails
from .models import StudentLoginDetails
from .models import StudentSubjects
from .models import TeacherDetails
from .models import TeacherLoginDetails
from .models import TeacherSubjects
from .models import PhyTest
from .models import ChemTest
from .models import MathTest
from .models import BioTest
from .models import CseTest
from .models import Test


global usn, test


def index(request):
    return render(request, "coderthemes.com/greeva/layouts/vertical/auth-login.html")


def login(request):
    return render(request, "coderthemes.com/greeva/layouts/vertical/auth-login.html")


def register(request):
    return render(request, "coderthemes.com/greeva/layouts/vertical/auth-register.html")


def recoverpassword(request):
    return render(request, "coderthemes.com/greeva/layouts/vertical/auth-recoverpassword.html")


def create_test(request):
    global usn
    log = TeacherLoginDetails.objects.filter(user_id=usn)
    return render(request, "coderthemes.com/greeva/layouts/vertical/createtest.html", {'logs': log})


def submit_test(request, index):
    ans = request.POST['ans']
    print(ans)
    global test_id
    if index not in ['1', '2', '3', '4', '5', '6']:
        test_id = index
    student = StudentDetails.objects.get(studentlogindetails__user_id=usn)
    addtest = Test.objects.get(studentdetails=student, test_id=test_id)
    if index in ['1', '2', '3', '4', '5', '6']:
        i = int(index)
        if i == 3:
            addtest.a2 = ans
            addtest.save()
            return redirect('../../attempt_test/3/')
        elif i == 4:
            addtest.a3 = ans
            addtest.save()
            return redirect('../../attempt_test/4/')
        elif i == 5:
            addtest.a4 = ans
            addtest.save()
            return redirect('../../attempt_test/5/')
        elif i > 5:
            addtest.a5 = ans
            addtest.save()
            marks = 0
            phytest = PhyTest.objects.filter(test_id=test_id, index=1)
            if phytest.exists():
                i = 1
                for a in [addtest.a1, addtest.a2, addtest.a3, addtest.a4, addtest.a5]:
                    count = PhyTest.objects.get(test_id=test_id, index=i)
                    i = i + 1
                    if count.ans == a:
                        marks = marks+1
                addtest.marks = marks
                addtest.save()
            chemtest = ChemTest.objects.filter(test_id=test_id, index=1)
            if chemtest.exists():
                i = 1
                for a in [addtest.a1, addtest.a2, addtest.a3, addtest.a4, addtest.a5]:
                    count = ChemTest.objects.get(test_id=test_id, index=i)
                    i = i + 1
                    if count.ans == a:
                        marks = marks + 1
                addtest.marks = marks
                addtest.save()
            mathtest = MathTest.objects.filter(test_id=test_id, index=1)
            if mathtest.exists():
                i = 1
                for a in [addtest.a1, addtest.a2, addtest.a3, addtest.a4, addtest.a5]:
                    count = MathTest.objects.get(test_id=test_id, index=i)
                    i = i + 1
                    if count.ans == a:
                        marks = marks + 1
                addtest.marks = marks
                addtest.save()
            biotest = BioTest.objects.filter(test_id=test_id, index=1)
            if biotest.exists():
                i = 1
                for a in [addtest.a1, addtest.a2, addtest.a3, addtest.a4, addtest.a5]:
                    count = BioTest.objects.get(test_id=test_id, index=i)
                    i = i + 1
                    if count.ans == a:
                        marks = marks + 1
                addtest.marks = marks
                addtest.save()
            csetest = CseTest.objects.filter(test_id=test_id, index=1)
            if csetest.exists():
                i = 1
                for a in [addtest.a1, addtest.a2, addtest.a3, addtest.a4, addtest.a5]:
                    count = CseTest.objects.get(test_id=test_id, index=i)
                    i = i + 1
                    if count.ans == a:
                        marks = marks + 1
                addtest.marks = marks
                addtest.save()
            return redirect('../../give_test')
    else:
        addtest.a1 = ans
        addtest.save()
        return redirect('../../attempt_test/2/')


def attempt_test(request, index):
    global test_id, subj
    if index in ['1', '2', '3', '4', '5']:
        i = int(index)
        if subj == "PHY":
            tecusr = PhyTest.objects.get(test_id=test_id, index=i)
        elif subj == "CHEM":
            tecusr = ChemTest.objects.get(test_id=test_id, index=i)
        elif subj == "MATH":
            tecusr = MathTest.objects.get(test_id=test_id, index=i)
        elif subj == "BIO":
            tecusr = BioTest.objects.get(test_id=test_id, index=i)
        else:
            tecusr = CseTest.objects.get(test_id=test_id, index=i)
        indexnxt = int(index) + 1
        return render(request, "coderthemes.com/greeva/layouts/vertical/attempttest.html",
                      {'index': index, 'nxt': indexnxt, 'tname': test_id, 'test': tecusr})
    else:
        student = StudentDetails.objects.get(studentlogindetails__user_id=usn)
        phyteacher = PhyTest.objects.filter(test_id=index, index=1)
        if phyteacher.exists():
            subj = "PHY"
            tecusr = PhyTest.objects.get(test_id=index, index=1)
            tec = TeacherDetails.objects.get(teacherlogindetails__user_id=tecusr.user_id)
            testvar = Test(studentdetails=student, teacherdetails=tec, test_id=index, subject="phy")
            testvar.save()
        chemteacher = ChemTest.objects.filter(test_id=index, index=1)
        if chemteacher.exists():
            subj = "CHEM"
            tecusr = ChemTest.objects.get(test_id=index, index=1)
            tec = TeacherDetails.objects.get(teacherlogindetails__user_id=tecusr.user_id)
            testvar = Test(studentdetails=student, teacherdetails=tec, test_id=index, subject="chem")
            testvar.save()
        mathteacher = MathTest.objects.filter(test_id=index, index=1)
        if mathteacher.exists():
            subj = "MATH"
            tecusr = MathTest.objects.get(test_id=index, index=1)
            tec = TeacherDetails.objects.get(teacherlogindetails__user_id=tecusr.user_id)
            testvar = Test(studentdetails=student, teacherdetails=tec, test_id=index, subject="math")
            testvar.save()
        bioteacher = BioTest.objects.filter(test_id=index, index=1)
        if bioteacher.exists():
            subj = "BIO"
            tecusr = BioTest.objects.get(test_id=index, index=1)
            tec = TeacherDetails.objects.get(teacherlogindetails__user_id=tecusr.user_id)
            testvar = Test(studentdetails=student, teacherdetails=tec, test_id=index, subject="bio")
            testvar.save()
        cseteacher = CseTest.objects.filter(test_id=index, index=1)
        if cseteacher.exists():
            subj = "CSE"
            tecusr = CseTest.objects.get(test_id=index, index=1)
            tec = TeacherDetails.objects.get(teacherlogindetails__user_id=tecusr.user_id)
            testvar = Test(studentdetails=student, teacherdetails=tec, test_id=index, subject="cse")
            testvar.save()
        i = 1
        indexnxt = index
        test_id = index
        return render(request, "coderthemes.com/greeva/layouts/vertical/attempttest.html",
                      {'index': i, 'nxt': indexnxt, 'tname': test_id, 'test': tecusr})


def give_test(request):
    global usn, physub, chemsub, mathsub, biosub, cssub
    log = StudentLoginDetails.objects.filter(user_id=usn)
    sub = StudentSubjects.objects.get(studentdetails__studentlogindetails__user_id=usn)
    if sub.phy == "on":
        giventests = Test.objects.filter(studentdetails__studentlogindetails__user_id=usn, subject="phy")
        physub = PhyTest.objects.filter(index=1)
        for giventest in giventests:
            physub = physub.exclude(test_id=giventest.test_id)
    else:
        physub = None
    if sub.chem == "on":
        giventests = Test.objects.filter(studentdetails__studentlogindetails__user_id=usn, subject="chem")
        chemsub = ChemTest.objects.filter(index=1)
        for giventest in giventests:
            chemsub = chemsub.exclude(test_id=giventest.test_id)
    else:
        chemsub = None
    if sub.math == "on":
        giventests = Test.objects.filter(studentdetails__studentlogindetails__user_id=usn, subject="math")
        mathsub = MathTest.objects.filter(index=1)
        for giventest in giventests:
            mathsub = mathsub.exclude(test_id=giventest.test_id)
    else:
        mathsub = None
    if sub.bio == "on":
        giventests = Test.objects.filter(studentdetails__studentlogindetails__user_id=usn, subject="bio")
        biosub = BioTest.objects.filter(index=1)
        for giventest in giventests:
            biosub = biosub.exclude(test_id=giventest.test_id)
    else:
        biosub = None
    if sub.cse == "on":
        giventests = Test.objects.filter(studentdetails__studentlogindetails__user_id=usn, subject="cse")
        cssub = CseTest.objects.filter(index=1)
        for giventest in giventests:
            cssub = cssub.exclude(test_id=giventest.test_id)
    else:
        cssub = None
    return render(request, "coderthemes.com/greeva/layouts/vertical/givetest.html",
                  {'logs': log, 'phys': physub, 'chems': chemsub, 'maths': mathsub, 'bios': biosub, 'css': cssub})


def view_test1(request):
    log = TeacherLoginDetails.objects.filter(user_id=usn)
    sub = TeacherSubjects.objects.get(teacherdetails__teacherlogindetails__user_id=usn)
    if sub.phy == "on":
        subject = "Physics"
        sub = PhyTest.objects.filter(user_id=usn, index=1)
    elif sub.chem == "on":
        subject = "Chemistry"
        sub = ChemTest.objects.filter(user_id=usn, index=1)
    elif sub.math == "on":
        subject = "Mathematics"
        sub = MathTest.objects.filter(user_id=usn, index=1)
    elif sub.bio == "on":
        subject = "Biology"
        sub = BioTest.objects.filter(user_id=usn, index=1)
    elif sub.cse == "on":
        subject = "Computer Science"
        sub = CseTest.objects.filter(user_id=usn, index=1)
    else:
        subject = ""
    return render(request, "coderthemes.com/greeva/layouts/vertical/viewtest-1.html", {'logs': log,
                            'subjects': subject, 'subs': sub})


def view_test2(request):
    log = StudentLoginDetails.objects.filter(user_id=usn)
    takentest = Test.objects.filter(studentdetails__studentlogindetails__user_id=usn)
    return render(request, "coderthemes.com/greeva/layouts/vertical/viewtest-2.html", {'logs': log, 'subs': takentest})


def view_results_t1(request):
    global usn
    log = TeacherLoginDetails.objects.filter(user_id=usn)
    return render(request, "coderthemes.com/greeva/layouts/vertical/viewresults-t1.html", {'logs': log})


def view_results_t2(request, index):
    giventest = Test.objects.filter(test_id=index)
    stuname = []
    for stu in giventest:
        student = stu.studentdetails
        stuname.append(student.first_name)
    i = range(0, 10)
    log = TeacherLoginDetails.objects.filter(user_id=usn)
    return render(request, "coderthemes.com/greeva/layouts/vertical/viewresults-t2.html", {'logs': log, 'stu': stuname, 'tests': giventest, 'j': i})


def performance_graph(request, index):
    log = TeacherLoginDetails.objects.filter(user_id=usn)
    a = Test.objects.filter(test_id=index, marks='0').count()
    b = Test.objects.filter(test_id=index, marks='1').count()
    c = Test.objects.filter(test_id=index, marks='2').count()
    d = Test.objects.filter(test_id=index, marks='3').count()
    e = Test.objects.filter(test_id=index, marks='4').count()
    f = Test.objects.filter(test_id=index, marks='5').count()
    return render(request, "coderthemes.com/greeva/layouts/vertical/graph.html", {'logs': log, 'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f})


def view_results_s1(request):
    log = StudentLoginDetails.objects.filter(user_id=usn)
    return render(request, "coderthemes.com/greeva/layouts/vertical/viewresults-s1.html", {'logs': log})


def findtestresults(request):
    index = request.POST['testname']
    url = 'view_results_t2/'+str(index)
    return redirect(url)


def searchtestresults(request):
    index = request.POST['testname']
    url = 'view_results_s2/'+str(index)
    return redirect(url)


def view_results_s2(request, index):
    phytest = PhyTest.objects.filter(test_id=index)
    chemtest = ChemTest.objects.filter(test_id=index)
    mathtest = MathTest.objects.filter(test_id=index)
    biotest = BioTest.objects.filter(test_id=index)
    csetest = CseTest.objects.filter(test_id=index)
    if phytest.exists():
        tecusr = PhyTest.objects.filter(test_id=index)
    elif chemtest.exists():
        tecusr = ChemTest.objects.filter(test_id=index)
    elif mathtest.exists():
        tecusr = MathTest.objects.filter(test_id=index)
    elif biotest.exists():
        tecusr = BioTest.objects.filter(test_id=index)
    elif csetest.exists():
        tecusr = CseTest.objects.filter(test_id=index)
    else:
        tecusr = None
    det = StudentDetails.objects.get(studentlogindetails__user_id=usn)
    print(det)
    log = StudentLoginDetails.objects.filter(user_id=usn)
    takentest = Test.objects.get(studentdetails__studentlogindetails__user_id=usn, test_id=index)
    return render(request, "coderthemes.com/greeva/layouts/vertical/viewresults-s2.html", {'users': det, 'logs': log, 'test': takentest, 'qns': tecusr})


def regform_submit(request):
    print("Registeration done successfully")
    first_name = request.POST['f_name']
    last_name = request.POST['l_name']
    phno = request.POST['phno']
    email = request.POST['mail']
    date = request.POST.get('date', False)
    cse = request.POST.get('cs', False)
    teacher = request.POST['tec']
    phy = request.POST.get('phy', False)
    chem = request.POST.get('chem', False)
    math = request.POST.get('math', False)
    bio = request.POST.get('bio', False)
    user_id = request.POST.get('user_name', False)
    password = request.POST['passwrd']
    if teacher == '0':
        teacherdetails = TeacherDetails(first_name=first_name, last_name=last_name, phno=phno,
                                        email=email, date=date)
        teacherdetails.save()
        teacherlogindetails = TeacherLoginDetails(user_id=user_id, password=password)
        teacherlogindetails.teacherdetails = teacherdetails
        teacherlogindetails.save()
        teachersubjects = TeacherSubjects(phy=phy, chem=chem, math=math, bio=bio, cse=cse)
        teachersubjects.teacherdetails = teacherdetails
        teachersubjects.save()
    else:
        studentdetails = StudentDetails(first_name=first_name, last_name=last_name, phno=phno, email=email, date=date)
        studentdetails.save()
        studentlogindetails = StudentLoginDetails(user_id=user_id, password=password)
        studentlogindetails.studentdetails = studentdetails
        studentlogindetails.save()
        studentsubjects = StudentSubjects(phy=phy, chem=chem, math=math, bio=bio, cse=cse)
        studentsubjects.studentdetails = studentdetails
        studentsubjects.save()

    return render(request, "coderthemes.com/greeva/layouts/vertical/auth-login.html")


def loginform_submit(request):
    checkusn = request.POST['user_name']
    checkpwd = request.POST['passwrd']
    loginform_submit.usn = checkusn
    check1 = StudentLoginDetails.objects.filter(user_id=checkusn, password=checkpwd)
    check2 = TeacherLoginDetails.objects.filter(user_id=checkusn, password=checkpwd)
    global usn
    if check1.exists():
        usn = checkusn
        return redirect('student_dashboard')
    elif check2.exists():
        usn = checkusn
        return redirect('teacher_dashboard')
    else:
        messages.error(request, "Incorrect username or password")
        return render(request, "coderthemes.com/greeva/layouts/vertical/auth-login.html")


def createtest_name(request):
    tn = request.POST['testname']
    sub = TeacherSubjects.objects.get(teacherdetails__teacherlogindetails__user_id=usn)
    if sub.phy == "on":
        for i in [1, 2, 3, 4, 5]:
            addtest = PhyTest(user_id=usn, test_id=tn, index=i)
            addtest.save()
    elif sub.chem == "on":
        for i in [1, 2, 3, 4, 5]:
            addtest1 = ChemTest(user_id=usn, test_id=tn, index=i)
            addtest1.save()
    elif sub.math == "on":
        for i in [1, 2, 3, 4, 5]:
            addtest1 = MathTest(user_id=usn, test_id=tn, index=i)
            addtest1.save()
    elif sub.bio == "on":
        for i in [1, 2, 3, 4, 5]:
            addtest1 = BioTest(user_id=usn, test_id=tn, index=i)
            addtest1.save()
    elif sub.cse == "on":
        for i in [1, 2, 3, 4, 5]:
            addtest1 = CseTest(user_id=usn, test_id=tn, index=i)
            addtest1.save()
    global test
    test = tn
    j = 1
    return render(request, "coderthemes.com/greeva/layouts/vertical/addtest.html", {'users': tn, 'i': j})


def question_submit(request, index, i):
    sub = TeacherSubjects.objects.get(teacherdetails__teacherlogindetails__user_id=usn)
    qn = request.POST['qn']
    a = request.POST['opa']
    b = request.POST['opb']
    c = request.POST['opc']
    d = request.POST['opd']
    ans = request.POST['ans']
    print(i)
    if sub.phy == "on":
        question = PhyTest.objects.get(user_id=usn, test_id=test, index=i)
    elif sub.chem == "on":
        question = ChemTest.objects.get(user_id=usn, test_id=test, index=i)
    elif sub.math == "on":
        question = MathTest.objects.get(user_id=usn, test_id=test, index=i)
    elif sub.bio == "on":
        question = BioTest.objects.get(user_id=usn, test_id=test, index=i)
    elif sub.cse == "on":
        question = CseTest.objects.get(user_id=usn, test_id=test, index=i)
    else:
        question = None
    question.qn = qn
    question.a1 = a
    question.a2 = b
    question.a3 = c
    question.a4 = d
    question.ans = ans
    question.save()
    if i == '1':
        url = '../../../createtest_submit/' + str(index) + '/2/'
    elif i == '2':
        url = '../../../createtest_submit/' + str(index) + '/3/'
    elif i == '3':
        url = '../../../createtest_submit/' + str(index) + '/4/'
    elif i == '4':
        url = '../../../createtest_submit/' + str(index) + '/5/'
    elif i == '5':
        url = '../../../create_test'
    else:
        url = '../../../create_test'
    return redirect(url)


def createtest_submit(request, index, i):
    return render(request, "coderthemes.com/greeva/layouts/vertical/addtest.html", {'users': index, 'i': i})


def student_dashboard(request):
    det = StudentDetails.objects.filter(studentlogindetails__user_id=usn)
    sub = StudentSubjects.objects.filter(studentdetails__studentlogindetails__user_id=usn)
    log = StudentLoginDetails.objects.filter(user_id=usn)
    takentest = Test.objects.filter(studentdetails__studentlogindetails__user_id=usn)
    return render(request, "coderthemes.com/greeva/layouts/vertical/index-4.html",
                  {'users': det, 'subs': sub, 'logs': log, 'results': takentest})


def teacher_dashboard(request):
    det = TeacherDetails.objects.filter(teacherlogindetails__user_id=usn)
    log = TeacherLoginDetails.objects.filter(user_id=usn)
    sub = TeacherSubjects.objects.get(teacherdetails__teacherlogindetails__user_id=usn)
    if sub.phy == "on":
        subject = PhyTest.objects.filter(user_id=usn, index=1)
        count = PhyTest.objects.filter(user_id=usn, index=1).count()
        print(count)
        name = "Physics"
    elif sub.chem == "on":
        subject = ChemTest.objects.filter(user_id=usn, index=1)
        count = ChemTest.objects.filter(user_id=usn, index=1).count()
        print(count)
        name = "Chemistry"
    elif sub.math == "on":
        subject = MathTest.objects.filter(user_id=usn, index=1)
        count = MathTest.objects.filter(user_id=usn, index=1).count()
        print(count)
        name = "Mathematics"
    elif sub.bio == "on":
        subject = BioTest.objects.filter(user_id=usn, index=1)
        count = BioTest.objects.filter(user_id=usn, index=1).count()
        print(count)
        name = "Biology"
    elif sub.cse == "on":
        subject = CseTest.objects.filter(user_id=usn, index=1)
        count = CseTest.objects.filter(user_id=usn, index=1).count()
        print(count)
        name = "Computers"
    else:
        count = 0
        subject = 0
        name = ""
    return render(request, "coderthemes.com/greeva/layouts/vertical/index-3.html",
                  {'users': det, 'subs': sub, 'subjects': subject, 'logs': log, 'name': name, 'count': count})
