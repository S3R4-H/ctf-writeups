**Description**


![description](./images/Is_The_Report_in_English_description.png)



I am given a PDF file here:


![item](./items/KUBSTU_Financial_Report_2025.pdf)


First i use Strings command to see if there is any thing useful. 
I tried to grep for the flag using the format ***kubSTU{}*** but did not get anything


![attempt1](./images/attempt_1.png)



But there are a lot of base64 encoded strings:


![attempt2](./images/attempt_2.png)

So i wrote i a simple script:


![decode1](./images/decode_1.png)



1) It searches for every sequence of 4 or more base64 characters in the file.
2) It decodes every single on of them
3) It then prints results if the decoded string contains the string ***kubSTU***


And i got the flag:
![flag](./images/flag.png)

