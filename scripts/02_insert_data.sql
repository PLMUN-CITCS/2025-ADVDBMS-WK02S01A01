/*
    Filename:       02_insert_data.sql
    Purpose:        Insert data into the database
    Instructions:
    1. Insert the following data into the tblStudents table:
        - student_name: John Doe
        - student_email: johndoe@gmail.com
        - student_phone: 123-456-7890

        - student_name: Jane Doe
        - student_email: janedoe@gmail.com
        - student_phone: 123-456-7890

    2. Place your insert queries below this comment
*/

INSERT INTO 
    tblStudents (student_name, student_email, student_phone) 
    VALUES 
        ('John Doe', 'johndoe@gmail.com', '123-456-7890'),
        ('Jane Doe', 'janedoe@gmail.com', '123-456-7890');