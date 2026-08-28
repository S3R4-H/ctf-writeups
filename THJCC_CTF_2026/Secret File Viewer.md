## Initial Observation##

We were provided with files **A–C**, which contained captured conversations and application components.

From the analysis of `script.js`, we identified that it functions as a **Client-Side Path Traversal (CSPT) protection module**.

![UserInterface](./images/secre_file_viewer_UI.png)

![FileA](./images/secret_file_viewer_fileA.png)

![FileB](./images/secret_file_viewer_fileB.png)

![FileC](./images/secret_file_viewerfileC.png)


/etc/passwd

No traversal was necessary.

The current directory is files from downloads.php, files is not root::

![HTML](./images/secret_file_viewer_html.png)
But wait!! In PHP, if a script uses a function like file_get_contents($file), or include($$file), and you provide /etc/passwd, the OS ignored whatever current directory the sript is in and goes straight to the root. W3School's PHP include and PHP's filesystem documentation explain that paths starting with / are treated as absolute.
Therefore the script.js was no use

![Test](./images/secret_file_viewer_test1.png)
From the above image, you can see i did not have to traverse to reach the root and access /etc/passwd.

![Final](./images/secret_file_viewer_final.png)


FLAG::`THJCC{h0w_dID_y0u_br34k_q'5_pr073c710n???}`




















