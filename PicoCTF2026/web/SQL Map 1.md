![[SQL_Map1_Description.png]]

**Description
After registering a username i login and i see a page with search parameter. From the hints i found an SQLMap sample command so assumed the vulnerability was SQLi and i am suppose to exploit with sql map
![[SQL_Map1_browser.png]]
![[SQL_Map1_hint.png]]

**Vulnerability
My URL looks like /vuln.php?q=hello&PHPSESSID=f96dc5fc6a560eb0d4180aa060261ba5  
![[SQL_Map1_URL.png]]
So i will construct my sqlmap command from that.
I used the following command::
![[SQL_Map1_command1.png]]
The command tells SQLMap to automatically test and extract the list of tables from the database using the search parameter i specified.
But with this command i kept getting a timeout 
![[SQL_Map1_Command1error.png]]
So i used a second command
![[SQL_Map1_command2.png]]
This command forces SQLMap to use Boolean-based injection which we discovered in the first command i used. Then it will brute-force the names of tables by guessing them from a built-in dictionary

**The command is at 42 and i found the user table  so i will go to the next step before the instance timesout



