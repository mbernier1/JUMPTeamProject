SELECT *
FROM users
WHERE users.email = %s
AND users.userpassword = %s;