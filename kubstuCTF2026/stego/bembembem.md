**Description**
![[bembembem_description.png]]

I am also given a file:
![[bembembem.mp4]]

I ran strings command in the .mp4 file and found something towards the end of it:
![[bembembem_hint1.png]]
So i wrote a script to decode as specified in the hint:
[...path to file]

And i got the text:
![[bembembem_hint2.png]]

which in english translates to:
[path to translate script]

![[bembembem_hint2-2.png]]


1) Roman figure 1 mentions forty-second minutes, and spectrum. So i opened the .mp4 with Audacity and went to exactly 42 minutes of the video.
And i found something: K0t05t
![[bembembem_hint3.png]]

2) Roman figure 2 says something about appended data at the end and the vid_md5 in metadata. We must Xor the Vid Md 5 with the appended extras. So i viewed the metadata of the .mp4 file:
![[bembembem_hint4.png]]
- From the image, we got the key and the warning tells us the start point of the offset of the tail. Standard MP4s are built out of atoms or blocks of data. And when exiftool sees an atom that cuts off or has extra garbage attached to it at a specific address, it flags it. In this case, the video ends or becomes corrupted at that extra (ofj8 offset 0x10008581) byte. Therefore i assume that is the beginning of the appended extra tail.  

2) Roman figure 3 says after we Xor we can open the output file extracted from the tail of the video with the key we found in the spectrum. (K0t05t)

So i wrote a script that skips the video, grabs the hidden tail and uses the MD5 key to unscramble it back to a ZIP file.

[path to script]

After i opened the resulting ***trunk.zip*** file with the password found in the spectrum:
![[bembembem_flag.png]]




