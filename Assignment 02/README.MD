Jordan Unfred

Assignment 02

# 3. Develop Natural Language Statements

- Create a database that stores information about students, the courses they are registered for, and the teachers responsible for teaching those courses.
- Develop a database to manage student enrollment, student-specific information, and the class schedules to which the students enroll for.
- Establish a database for storing student class records, including information about previous classes taken from transfer students, dropped classes, and failed courses

# 5. ERD notation system

This ERD represents a simplified version of a student advising and degree checklist system. Students can enroll in courses, and those courses are associated with a specific curriculum. Each student has an advisor to guide them through course selection. The ERD illustrates how these entities are related, helping students and advisors track degree progress and course enrollment.

(see image in README folder)

# 6. Conceptual, Logical and Physical:

## Conceptual ERD

In the conceptual ERD, we focus on high-level entities, relationships, and their attributes. It represents a simplified, abstract view of the system.

### Entities:

1. Student
2. Curriculum
3. Course
4. EnrolledCourse
5. Advisor

### Relationships:

- One-to-Many: Student to EnrolledCourse
- One-to-Many: EnrolledCourse to Course
- Many-to-One: EnrolledCourse to Curriculum
- Many-to-One: Student to Advisor

## Logical ERD

In the logical ERD, we add more detail, specifying attributes for each entity and refining relationships. It is still relatively abstract but provides a more comprehensive view.

### Entities:

#### Student

- Attributes: Student ID (Primary Key), Name, Email, Phone, Date of Birth, etc.

#### Curriculum

- Attributes: Curriculum ID (Primary Key), Curriculum Name, Total Credits Required, etc.

#### Course

- Attributes: Course ID (Primary Key), Course Code, Course Title, Credit Hours, etc.

#### EnrolledCourse

- Attributes: EnrolledCourse ID (Primary Key), Student ID (Foreign Key), Course ID (Foreign Key), Enrollment Date, Grade, etc.

#### Advisor

- Attributes: Advisor ID (Primary Key), Name, Email, Phone, Office Location, etc.

### Relationships:

- One-to-Many: Student to EnrolledCourse (StudentID -\> Student)
- One-to-Many: EnrolledCourse to Course (CourseID -\> Course)
- Many-to-One: EnrolledCourse to Curriculum (CurriculumID -\> Curriculum)
- Many-to-One: Student to Advisor (AdvisorID -\> Advisor)

## Physical ERD

In the physical ERD, we consider the actual database implementation. It includes details such as data types, primary keys, foreign keys, and indexes. Here, we also include the table names.

### Tables:

#### Students

- Columns: StudentID (Primary Key, INT), Name (VARCHAR), Email (VARCHAR), Phone (VARCHAR), DateOfBirth (DATE), etc.

#### Curricula

- Columns: CurriculumID (Primary Key, INT), CurriculumName (VARCHAR), TotalCreditsRequired (INT), etc.

#### Courses

- Columns: CourseID (Primary Key, INT), CourseCode (VARCHAR), CourseTitle (VARCHAR), CreditHours (INT), etc.

#### EnrolledCourses

- Columns: EnrolledCourseID (Primary Key, INT), StudentID (Foreign Key, INT), CourseID (Foreign Key, INT), EnrollmentDate (DATE), Grade (VARCHAR), etc.

#### Advisors

- Columns: AdvisorID (Primary Key, INT), Name (VARCHAR), Email (VARCHAR), Phone (VARCHAR), OfficeLocation (VARCHAR), etc.
- Foreign Keys and Relationships are maintained as described in the logical ERD.