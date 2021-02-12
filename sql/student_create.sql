CREATE TABLE student (
	student_id VARCHAR(5) NOT NULL AUTO_INCREMENT , -- Unique student_id that is auto-generated and auto-incremented
	full_name VARCHAR(40) NOT NULL ,
	class VARCHAR(2) NOT NULL ,
	dob VARCHAR(10) NOT NULL ,
    PRIMARY KEY(student_id) -- student_id is made the primary key
);
