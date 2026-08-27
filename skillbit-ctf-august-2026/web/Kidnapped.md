Web Challenge: Business Logic Vulnerability
![](images/description.png)

We are given the app file but i will attempt black-box.

I Register a username and passwords and login
![](images/register.png)
![](images/login.png)

Challenge description says "We built a cool website that uses JWT for authentication" so i target JWT.
I will attempt to manipulate the auth_token to get the flag:

![](images/auth-cookie.png)

I target the highlighted part. 
![](images/manipulate-1.png)

I change the balance
![](images/2026-08-28_00-50.png)

Burp response redirects me to /login and my price does not change
![](images/manipulate-fail.png)

![](images/manipulate-fail-2.png)

Second test, i target the quantity parameter within /add_to_cart/21

![](images/quantity.png)

I change it to a lower number to decrease its price. It did not work when i change in browser, so i used burpsuite intercept.

![](images/quantity-down.png)

I proceed to checkout and get the flag
![](images/flag.png)