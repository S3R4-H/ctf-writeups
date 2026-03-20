![[Order_Order.png]]

**Description
After signing up and logging in, i go to my expense page to add an expense and download the .csv in the inbox page
![[Order_Order_inbox.png]]
![[Order_Order_expense.png]]
From the following i can see the reports are downloaded based on the logged in user.  That is they filter what to download based on the user who is currently logged in.
![[Order_Order_downloadresult.png]]

**Vulnerability
The app fails to properly sanitise user input in SQL queries because the username field is directly concatenated into the query. This allows UNION-based SQL injection to retrieve data from other table. 
When placing the payload in the username field during registration, the app stores it in the database without proper sanitisation. Later when the system generated report, it reuses that stored value in a SQL query without escaping it, this the known as second-order injection

**Exploit
Command1:
Since i know that injecting the payload in the description will not work, i will use the username field to inject my payload
![[Order_Order_command1username.png]]
And this time in the description i will add whatever i want, and the report now will look like 
![[Order_Order_command1inbox.png]]
Now when i open i get
![[Order_Order_command1details.png]]
The part below the description is base64 encoded
![[Order_Order_command1decode.png]]

**Command2
**Now that  i got a suspicious table i will read it by registering another username and add a any expense and download
![[Order_Order_command2.png]]
![[Order_Order_command2download.png]]
Then i opened it again and got the flag
![[Order_Order_command2flag.png]]

**Flag::picoCTF{s3c0nd_0rd3r_1t_1s_30dc1ce8}