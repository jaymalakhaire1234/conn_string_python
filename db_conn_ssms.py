import pyodbc
conn_str=(

"DRIVER={ODBC Driver 17 for SQL Server};"

"SERVER=OMKAR\SQLEXPRESS03;"

"DATABASE=python;"
"Trusted_Connection=yes;"
)
conn=pyodbc.connect(conn_str)
cur=conn.cursor()
# cur.execute('''CREATE TABLE Students (
#     StudentID INT PRIMARY KEY IDENTITY(1,1),  -- Unique ID for each student
#     FirstName NVARCHAR(50) NOT NULL,         -- Student's first name
#     LastName NVARCHAR(50) NOT NULL,          -- Student's last name
#     DateOfBirth DATE,                        -- Student's date of birth
#     Email NVARCHAR(100) UNIQUE,              -- Student's email address (must be unique)
#     EnrollmentDate DATETIME NOT NULL DEFAULT GETDATE(),  -- Date of enrollment
#     PhoneNumber NVARCHAR(15),                 -- Student's phone number
#     Address NVARCHAR(255)                     -- Student's address
# )''')
cur.execute('''INSERT INTO Students (FirstName, LastName, DateOfBirth, Email, PhoneNumber, Address)
VALUES 
('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Elm St, Springfield, IL'),
('Jane', 'Smith', '1992-01-01', 'jane.smith@example.com', '987-654-3210', '456 Oak St, Springfield, IL'),
('Bob', 'Johnson', '1991-01-01', 'bob.johnson@example.com', '555-123-4567', '789 Pine St, Springfield, IL'),
('Alice', 'Williams', '1993-05-15', 'alice.williams@example.com', '321-654-9870', '135 Maple St, Springfield, IL'),
('Charlie', 'Brown', '1994-03-22', 'charlie.brown@example.com', '456-789-0123', '246 Birch St, Springfield, IL') ''')
cur.commit()
conn.close()