drop table if exists "students";
drop table if exists "courses";
drop table if exists "student_courses";


CREATE TABLE "students" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT NOT NULL,
	"age"	INTEGER,
	"major"	TEXT NOT NULL
);

CREATE TABLE "courses" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT NOT NULL,
	"instructor"	TEXT
);

CREATE TABLE "student_courses" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"student_id"	INTEGER NOT NULL,
	"course_id"	INTEGER NOT NULL,
	FOREIGN KEY("course_id") REFERENCES "courses"("id") ON DELETE CASCADE,
	FOREIGN KEY("student_id") REFERENCES "students"("id") ON DELETE CASCADE
);

insert into students (name, age, major) values ('Alice', 20, 'Computer Science');
insert into students (name, age, major) values ('Bob', 22, 'Mathematics');
insert into students (name, age, major) values ('Charlie', 21, 'Physics');
insert into courses (name, instructor) values ('Data Structures', 'Dr. Smith');
insert into courses (name, instructor) values ('Calculus', 'Dr. Johnson');

insert into student_courses (student_id, course_id) values (1, 1);
insert into student_courses (student_id, course_id) values (2, 2);
insert into student_courses (student_id, course_id) values (1, 2);
insert into student_courses (student_id, course_id) values (2, 1);
insert into student_courses (student_id, course_id) values (3, 1);

