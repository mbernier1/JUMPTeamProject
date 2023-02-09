SELECT * FROM users
INSERT INTO users (username, email, userpassword) 
VALUES (%s, %s, %s)