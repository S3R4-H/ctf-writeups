![[lockout_description.png]]

**Description
The app has a rate limit of 1 IP per 10 requests. This means after 10 failed login attempts the same IP will be rejected from sending any more requests.
![[lockout_exceed_rate_func.png]]
Every time a user visits /login, the code runs if exceeded_rate_limit()
It identifies the user via client_ip = request.remote_addr
If the request is a POST, it increments num_requests for that specific IP
If num_requests exceeds 10 (MAX_REQUESTS), it sets a lockout_util timestamp
While lock_util is active, the function will return True, and the route sends back the RATE_LIMIT_HTML message instead of checking the password

**Vulnerability
The script uses  request.remote_addr to identify the client. This makes it insecure because the value can be manipulated using the headers such as X-Forwarded-For. The server trust this header without validation, allowing spoofing IP possible

**Exploitation
I used a script to automate the matches. It also sends a header X-Forwarded-For which will automatically change the IP after every 10 requests.

![[lockout_changeipcode.png]]
![[lockout_flag.png]]
and the flag is ::
picoCTF{f00l_7h4t_l1m1t3r_e5c7c994}