**Execution After Redirect (EAR)**

The web asks for a username and password. 
![[Ear_login.png]]

### Challenge

Login page redirected but continued executing code.

### Vulnerability

- CWE-698: Execution After Redirect.
    
- `header()` called without `exit()` or `die()`.
    
- Browser redirected, but server continued executing.

### What Happens Without `exit()`

- Browser: “Okay, I’ll go to `login.php`.”
    
- Server: “Meanwhile, I’ll keep running `admin.php` or `system.php`.”
    
- Result: You can still reach protected functionality by directly requesting those files, or by intercepting the response before the redirect completes.

**What Would Happen With `exit()`**
- The `exit()` stops PHP immediately.
    
- No further code runs on the server.
    
- Sensitive files like `admin.php` or `system.php` would never be executed in that request.

![[EAR_SourceCode.png]]

### Exploit

1. Used directory fuzzing (`ffuf`) to discover hidden files.
    
2. Found `admin.php`, then `system.php`.
    
3. Accessed these directly despite redirect logic.
    
4. Retrieved the flag.

![[FUZZ_Ears.png]]

![[admin_ears.png]]

![[final_ears.png]]

and got the flag
FLAG::THJCC{U_kNoW-HOw-t0_uSe-EaR}



### Fix

Always terminate script execution after `header()`:
header("Location: index.php");
exit();


REFERENCES
https://owasp.org/www-community/attacks/Execution_After_Redirect_(EAR)
