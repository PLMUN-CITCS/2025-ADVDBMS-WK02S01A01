# 2025-ADVDBMS-LAB002
Week 02 - Creating Tables and Querying Data from Tables

Laboratory # 02 - Creating Tables and Querying Data from Tables

## **Instructions**

### **Step 1.1: Accept the Assignment**

1. Click on the assignment link provided by your instructor.
2. GitHub Classroom will create a **private repository** under your GitHub account.
3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 1.2: Setup your Git Environment**
*Only perform if this is the first time you will setup your Git Environment*

1. Create a GitHub Account:
```bash
https://github.com/signup?source=login
```
   
2. Download and Install Git on your Laptop/Desktop:
```bash
https://git-scm.com/downloads
```

3. Create a Folder in your Laptop/Desktop
4. Right-click anywhere in the created folder and select "Open Git Bash Here".
5. In the Git Bash Terminal, set your git name, perform command:
```bash
git config --global user.name "Your Name"
```

6. In the Git Bash Terminal, set your git email, perform command:
```bash
git config --global user.email "your.email@example.com"
```

7. Create your SSH Key, just follow the instructions, no need to provide filename and passphrase (Just Press ENTER allthroughout). In the Git Bash Terminal, perform command:
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

8. Copy your SSH Keys into clipboard by performing this command in the Git Bash Terminal:
```bash
clip < ~/.ssh/id_rsa.pub
```

9. Log in to your GitHub account.
10. In the upper-right corner of GitHub, click your profile picture and select Settings.
11. In the left sidebar, click on SSH and GPG keys.
12. Click the New SSH key button.
13. In the Title field, give the key a recognizable name (e.g., "My Windows Laptop").
14. In the Key field, CTRL + V or paste the keys copied into your clipboard. Save the key.
15. Go Back to terminal, use command:
```bash
ssh -T git@github.com
```

### **Step 2: Clone the Repository to Your Local Machine**

1. On your repository page, click the green **"Code"** button.
2. Copy the repository URL (choose HTTPS for simplicity).
3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:

```bash
git clone <git_repo_url>
```

4. Navigate into the cloned folder:

```bash
cd <git_cloned_folder>
```

### **Step 3: Complete the Assignment**

# **Laboratory # 02 - Creating Tables and Querying Data from Tables**

**Objectives**
- Understand Table Creation: Learn how to design and create a SQL table with a primary key and auto-increment functionality.
- Data Insertion Skills: Gain experience in writing SQL INSERT statements to add records to your table.
- File Organization: Learn how to organize SQL scripts using a consistent folder structure and file naming conventions.
- Best Practices: Familiarize yourself with SQL script best practices, such as proper formatting, commenting, and data integrity considerations.
- Real-world Application: Apply these skills to build a simple, yet effective, database component that can be expanded in larger projects.

**Folder Structure & File Naming Convention**
Folder Structure
- Organize your project directory as follows:
   - SQL_Lab_Project/: Main project folder.
   - scripts/: Subfolder that contains all SQL scripts.
```txt
SQL_Lab_Project/
└── scripts/
    ├── 01_create_tables.sql
    └── 02_insert_data.sql
```

**File Naming Conventions**
- 01_create_tables.sql: The prefix “01_” indicates that this script should be executed first. The filename clearly describes that this file is used for creating tables.
- 02_insert_data.sql: The prefix “02_” indicates that this script should be executed after the table creation script. The filename clearly shows that this file is used for inserting data.

**Notable Observation:**
- Using a numbered prefix in filenames not only ensures the correct execution order but also improves clarity when collaborating with others. Consistent naming helps maintain organization and scalability as projects grow.

**SQL Script Best Practices**
- Comments: Add descriptive comments to explain the purpose of each section or critical lines of code. For example:
```SQL
-- This script creates the tblStudents table with basic student details.
```
- Indentation & Formatting: Format your SQL commands for readability. Each field definition should be on its own line, and SQL keywords should be capitalized.
- Consistency: Stick to a consistent naming convention for tables and columns (e.g., using camelCase or snake_case). Here we use “tblStudents” for the table name.
- Use of Constraints: Define appropriate constraints like PRIMARY KEY and AUTO_INCREMENT to maintain data integrity.
- Version Control: Consider using version control (such as Git) to manage changes to your SQL scripts over time.

**Step-by-Step Instructions**
1. Create the Table
- Open scripts/01_create_tables.sql in your SQL editor.
- Write the SQL command to create the table tblStudents:
```SQL
-- Creating tblStudents table
CREATE TABLE tblStudents (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(50),
    student_email VARCHAR(50),
    student_phone VARCHAR(50)
);

```
- Save the file. Observation: Notice that the primary key is set on student_id with AUTO_INCREMENT to ensure that each student record is uniquely identifiable and automatically incremented.
  
2. Follow this syntax format:
- Open scripts/02_insert_data.sql in your SQL editor.
- Insert sample data into tblStudents:
```SQL
-- Creating tblStudents table
-- Inserting data into tblStudents
INSERT INTO tblStudents (student_name, student_email, student_phone)
VALUES
    ('John Doe', 'johndoe@gmail.com', '123-456-7890'),
    ('Jane Doe', 'janedoe@gmail.com', '123-456-7890');

```
- Save the file. Observation: The use of a multi-row INSERT statement makes your script efficient and scalable. Ensure that the column names in the INSERT statement match those defined in the table creation script.

3. Execution and Verification
- Run the 01_create_tables.sql script first to create the table.
- Run the 02_insert_data.sql script to insert the records.
- Verify the data insertion: Execute a simple query to check if the records have been inserted correctly:
```SQL
SELECT * FROM tblStudents;

```

**Conclusion**
By completing this exercise, you have practiced creating a table with a primary key and auto-increment, inserting multiple records with a well-formatted INSERT statement, and organizing your work within a structured folder system using clear file naming conventions. These skills are essential for building robust SQL databases and contribute to best practices in coding and project management. As you continue learning, always remember the importance of script organization, clear documentation, and adherence to best practices to ensure your SQL projects are scalable, maintainable, and collaborative.

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
Open the terminal and run:

```bash
git status
```
This command shows any modified or new files.

2. Stage the changes:
Add all modified files to staging:

```bash
git add .
```

3. Commit your changes:
Write a meaningful commit message:

```bash
git commit -m "Completed assignment: Created tables and inserted data"
```

4. Push your changes to GitHub:
Upload your changes to your remote repository:

```bash
git push origin main
```

### **Step 5: Submit Your Repository Link**
Once your changes have been pushed:
1. Visit your GitHub repository online.
2. Copy the repository URL from your browser (e.g., https://github.com/PLMUN-CITCS/your-github-repo-link).
3. Submit the repository link to your instructor via the Google Classroom Assignment, turn in and Privately Comment:
   - GitHub Repository URL: `[Your Repo Link]`
   - GitHub Username: `[Your GitHub Username]`
