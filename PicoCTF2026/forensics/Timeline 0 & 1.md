![Timeline0_description.png](./images/Timeline0_description.png)

**First i generate  the body file: I use fls tool which scans the partition and creates a machine-readable list of all files, including hidden and deleted ones, along with their metadata. 

![Timeline0_command1.png](./images/Timeline0_command1.png)

-r recurse through all directories and -m / sets the mounting point prefix

**Second i convert to a CSV Timeline. I use mactime to make that body file and format it into a chronological CSV so that i can open it in LibreOffice Calc.

![Timeline0_command2.png](./images/Timeline0_command2.png)

-b points to generated .txt, -d output in comma-delimited format and -y uses ISO 8601 date format
**The hint says
![Timeline_hint.png](./images/Timeline_hint.png)

This hint mean that .attacker attempted to hide a file by changing its timestamps but made a mistake in the process.

**So we will look at a very old time
From the .csv i found an old date 
![Timeline0_oldone.png](./images/Timeline0_oldone.png)
I tried reading the file and got 
![Timeline0_command3.png](./images/Timeline0_command3.png)
I decoded the base64 string in cyberchef 
![Timeline0_flag.png](./images/Timeline0_flag.png)
Then i wrap the flag picoCTF{71m311n3_0u7113r_h3r_43a2e7af}


---


TIMELINE 1

![Timeline1_description.png](./images/Timeline1_description.png)

**I download the image and do the same as i did for Timeline0 to convert it to .csv

**This time around one of the hint says
![Timeline1_hint1.png](./images/Timeline1_hint1.png)

In Sleuth Kit timelines "macb" refers to the four types of timestamps: Modified, Accessed, Changed, Birth.
So i filtered to "macb"
Then i opened it and found an unusual file for standard setup
![Timeline1_filefound.png](./images/Timeline1_filefound.png)

I opened it and found a base64 string and decoded it with cyberchef and got the flag
![Timeline1_encodedflag.png](./images/Timeline1_encodedflag.png)
![Timeline1_flag.png](./images/Timeline1_flag.png)
The flag is picoCTF{573417h13r_7h4n_7h3_1457_58527bb222}
