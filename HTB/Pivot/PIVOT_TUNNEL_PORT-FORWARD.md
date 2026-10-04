### HTB-SKILLS-ASSESSMENT

**DESCRIPTION**
A team member started a Penetration Test against the Inlanefreight environment but was moved to another project at the last minute. Luckily for us, they left a `web shell` in place for us to get back into the network so we can pick up where they left off. We need to leverage the web shell to continue enumerating the hosts, identifying common services, and using those services/protocols to pivot into the internal networks of Inlanefreight.

Sample of the network
![NETWORK-SUMMARY.png](images/NETWORK-SUMMARY.png)

**QUESTIONS**

---

![question_1.png](images/question_1.png)

![question_2.png](images/question_2.png)

There is nothing of interest inside administrator directory, but something inside webadmin. The user:pass is -> mlefay:Plain Human Work!

![answer_1.png](images/answer_1.png)

---

![question_3.png](images/question_3.png)

Firstly, i create a Meterpreter shell for the Ubuntu server, which will connect back to us at port 8080.

![answer_3.4.png](images/answer_3.4.png)

Afterwards i start a generic payload listener so that linux connects back to me when i run backupjob.

![answer_3.3.png](images/answer_3.3.png)

I will start a python server where i created the meterpreter shell for ubuntu and then download it to the initial target.

![answer_3-pythonserver.png](images/answer_3-pythonserver.png)

I have no "Write" permissions inside webadmin directory, so i will go back to /var/www/html directory where i have write permissions, and i will download the backupjob in there.

![answer_3-fail.png](images/answer_3-fail.png)
![answer_3-download.png](images/answer_3-download.png)
![answer_3-ok.png](images/answer_3-ok.png)

After downloading backupjob, i run it and it connects back to me. 
![answer_3-run.png](images/answer_3-run.png)

**ENUMERATE INTERNAL HOSTS**

The initial host's internal ip is "172.16.5.15/16 brd 172.16.255.255". I will reduce the number of hosts to enumerate.
Initially we have network-addr 172.16.0.0/16 to enumerate, but its too much...
I will start with 172.16.5.0/24. And i expect the internal IPs to be between 172.16.5.1 and 172.16.5.254.

![answer_3.2.png](images/answer_3.2.png)

I will use ping_sweep to enumerate internal hosts. 
![answer_3.png](images/answer_3.png)

The initial target host's internal ip is 172.16.5.15 and we have another one at 172.16.5.35.

---

![question_4.png](images/question_4.png)

I will background my session and continue using MSF and configure it to  use SOCKS Proxy.
![answer_4.1.png](images/answer_4.1.png)
![answer4.2.png](images/answer4.2.png)
I also configure proxychains in my attack host
![answer_4-conf.png](images/answer_4-conf.png)

Afterwards i add routes.

![answer4.3.png](images/answer4.3.png)

Then i connect to the internal host at 172.16.5.35  using my proxychains4.

The first command failed with some errors including a "Timeout waiting for activation" error. After  some trial and error i used the second command.  

![answer_4-fail1.png](images/answer_4-fail1.png)
![answer_4.2.png](images/answer_4.2.png)

The flag::
![answer_4.png](images/answer_4.png)

---
![question_5.png](images/question_5.png)

The hint is "We may be able to find something stored in LSASS."
More on the issue: https://redcanary.com/threat-detection-report/techniques/lsass-memory/


Firstly, i create a damp file (.DMP) for lsass within the RDP session from question 4. 
Then i copy it to my linux (attack host). And then i extract creds using pypykatz.

![answer_5.1.png](images/answer_5.1.png)
![answer_5.2.png](images/answer_5.2.png)

And our vulnerable user is vfrank.

![answer_5.3.png](images/answer_5.3.png)


