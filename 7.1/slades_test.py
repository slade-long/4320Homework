# Slade Long - 3/21/22 - CS 4320
# I had a really hard time with the techinical requirements to this assignments (I was asking for help a lot in the discord). Please excues this late assingment
# I also posted this on canvas
# For 7.2 I used the discord and ask for help and contributed the discussion
# Please excuse some of these functions... I tried my best on this assignment but it was very rigious and time consuming
import pytest
import System
import Staff
import Professor
import Student

# Test 1 - Login Function
# The login function takes a name and passwor and sets tje use for the program. 
# This program passed! (1/5)

def test_login(grading_system):
    username = 'hdjsr7'
    password =  'pass1234'
    if (grading_system.login(username,password) == True):
        assert False

# Test 2 - Check Password
# This functions checks that the password is correct. Enter several different formats formats of passwords to verify that the password returns correctly if the passwords are the same
# This program Passed! (2/5)

def test_check_password(grading_system):
    passwordPass = grading_system.check_password('hdjsr7', 'pass1234')
    passwordFail = grading_system.check_password('hdjsr7', 'bAdPaSsWoRd')
    passwordFail2 = grading_system.check_password('hdjsr7', 'anotherPass')
    if (passwordPass == passwordFail or passwordPass == passwordFail2):
        assert False

# Test 3 - Change Grade
# This function will change the grade of a student and updates the database. Verify that the correct grade is changed on the correct user in the database.
# This program failed! (2/5)
def test_change_grade(staff):
    gradeData = grading_system.users
    grading_system.login('goggins','augurrox')
    grading_system.change_grade('akend3','databases', 'assignment1', '100')
    if(gradeData[('akend3', 'databases', 'assignment1', 'grade', 100)] != True):
        assert False

# Test 4 - Create Assignment
# This function allows the staff to create a new assignment. Verify that an assignment is created with the correct due date in the correct course in the database.
# This program failed! (2/5)!
def test_create_assignment(staff):
    gradeData = grading_system.all_courses
    grading_system.login('cmhbf5', 'bestTA')
    new_assignment = [('cloud_computing', '5/1/22', 'assignment7')]
    grading_system.create_assignment(new_assignment)
    if(gradeData[('cloud_computing', '5/1/22', 'assignment7')] != True):
        assert False

# Test 5 - Add Student
# This function allows the professor to add a student to a course. Verify that a student will be added to the correct course in the database.
# This program failed! (3/5)!
def test_add_student(professor):
    professor.add_student('sdlp6f', 'cloud_computing')
    if ('sdlp6f' not in temp.users):
        assert False

# Test 6 - Drop Student
# This function allows the professor to drop a student in a course. Verify that the student is added and dropped from the correct course in the database.
# This program failed! (4/5)!
def test_drop_student(professor):
    professor.drop_student('akend3', 'cloud_computing')
    if ('akend3' in users):
        assert False

# Test 7 - Submit Assignment
# This function allows a student to submit an assignment. Verify that the database is updated with the correct assignment, submission, submission dateand in the correct course.
# This program passed (3/5)!
def test_submit_assignment(student):
    sub = student.submit_assignment('comp_sci', 'assignment2', 'Blah2 Blah2 Blah2', '3/22/22')
    if (sub == False):
        assert False

# Test 8 - Check Ontime
# This function checks if an assignment is submitted on time. Verify that it will return true if the assignment is on time, and false if the assignment is late!
# This program passed (4/5)!
def test_check_ontime(student):
    ot = student.check_ontime('2/1/20', '2/2/20')
    if (ot != True):
        assert False

# Test 9 - Check Grades
# This function returns the users grades for a specific course. Verify the correct grades are returned for the correct user.
# This program passed (5/5)!
def test_check_grades(student):
    checkedGrade = student.check_grades('comp_sci')
    if (checkedGrade == 99):
        assert False

# Test 10 - View Assignments
# This function returns assignments and their due dates for a specific course. Verify that the correct assignments for thecorrect course are returned.
# This program failed (5/5)!
def test_view_assignments(student):
    viewedAssignment = student.view_assignments('comp_sci')
    if(viewedAssignment != True):
        assert False

# Test 11 - Bad Login
# Similar to Test 1, this test is designed to intentially fail when a user feeds it bad information
# This program failed
def test_bad_login():
    username = 'badLOGIN'
    password =  'abcd1235'
    if (grading_system.login(username,password) == True):
        assert False

# Test 12 - Bad Assignment Creation
# Similar to Test 3, this test is designed to intentially fail when a user feeds it an assingmnet that cannot exist due to key errors
# This program failed
def test_fail_bad_assignment_insertion():
    gradeData = grading_system.all_courses
    grading_system.login('cmhbf5', 'bestTA')
    new_assignment = [('notACLASS', '9/9/99', 'assignment1')]
    grading_system.create_assignment(new_assignment)
    if(gradeData[('notACLASS', '9/9/99', 'assignment1')] != True):
        assert False

# Test 13 - TA Change Grade
# This test is designed to intentially fail when a ta feeds it an assingmnet that they can not create
# This program failed
def test_ta_change_grade(grading_system):
    gradeData = grading_system.users
    grading_system.login('cmhbf5','bestTA')
    grading_system.change_grade('akend3','databases', 'assignment1', '100')
    if(gradeData[('akend3', 'databases', 'assignment1', 'grade', 100)] != True):
        assert False

# Test 14 - Drop Professor
# This test is designed to intentially fail when a professor tries to drop another professor
# This program failed
def test_drop_professor(professor):
    professor.drop_student('goggins', 'databases')
    if ('goggins' in users):
        assert False

# Test 15 - Add Professor
# This test is designed to intentially fail when a professor tries to adds another professor
# This program failed
def test_add_professor(professor):
    professor.drop_student('JRies', 'CS 1050')
    if ('JRies' not in users):
        assert False

@pytest.fixture
def student():
    temp = System.System()
    temp.load_data()
    gradingStudent = Student.Student('akend3', temp.users, temp.courses)
    return gradingStudent

@pytest.fixture
def professor():
    temp = System.System()
    temp.load_data()
    gradingProfessor = Professor.Professor('goggins', temp.users, temp.courses)
    return gradingProfessor

@pytest.fixture
def staff():
    gradingStaff = Staff.Staff()
    return gradingStaff

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem