## Initial Observation

We were provided with files **A–C**, which contained captured conversations and application components.

From the analysis of `script.js`, we identified that it functions as a **Client-Side Path Traversal (CSPT) protection module**.

![[secre_file_viewer_UI.png]]

![[secret_file_viewer_fileA.png]]

![[secret_file_viewer_fileA.png]]

![[secret_file_viewerfileC.png]]

## JavaScript Analysis (`script.js`)

### 1. De-obfuscation

The function `_0x1c9a()` acts as a decoder for the `_0x5a3d` string array.

After reversing the obfuscation, key decoded strings include:

- `"log"`
    
- `"warn"`
    
- `".."` (directory traversal)
    
- `"/"`
    
- `"%2e%2e"` (URL-encoded `..`)
    

This confirms that the script attempts to detect directory traversal sequences.

### 2. Core Functionality

The script performs the following operations:

#### • Security Validation

The function `SecurityModule.validatePath()` checks whether a provided file path contains:

- `..`
    
- `%2e%2e`
    

These patterns are commonly used in **Local File Inclusion (LFI)** and path traversal attacks.

If detected, the request is blocked on the client side.

#### • Request Construction

If the path passes validation, the function `loadFileSecurely()` constructs a request:

obfuscation.php?file=[encoded_path]

---

#### • Event Handling

An event listener is attached to all `a.btn` elements.

When a user hovers over a button, it triggers the “secure” file loading process using that link’s URL.

## Security Analysis

Despite appearing protective, this mechanism is fundamentally flawed.
### 1. Incomplete Filtering

The script only checks for:

- `..`
    
- `%2e%2e`
    

It does **not** account for:

- Double encoding (`%252e%252e`)
    
- Windows-style traversal (`..\`)
    
- Mixed encoding
    
- Null byte injection (`%00`)
    
- Absolute paths (`/etc/passwd`)

## Critical Server-Side Flaw

The application loads files from `download.php`.

Although the UI suggests files are served from a specific directory, this is misleading.

In PHP, when functions such as:

- `include()`
    
- `require()`
    
- `file_get_contents()`
    
- `readfile()`
    

are given an **absolute path** (e.g., `/etc/passwd`), the operating system ignores the script’s current directory and resolves from the filesystem root.

This behavior is documented in PHP’s filesystem handling.

## Exploitation

Instead of using traversal (`../../etc/passwd`), we directly requested:

/etc/passwd

No traversal was necessary.

The current directory is files from downloads.php, files is not root::

![[secret_file_viewer_html.png]]
But wait!! In PHP, if a script uses a function like file_get_contents($file), or include($$file), and you provide /etc/passwd, the OS ignored whatever current directory the sript is in and goes straight to the root. W3School's PHP include and PHP's filesystem documentation explain that paths starting with / are treated as absolute.
Therefore the script.js was no use

![[secret_file_viewer_test1.png]]
From the above image, you can see i did not have to traverse to reach the root and access /etc/passwd.

![[secret_file_viewer_final.png]]


NOTE::We assume it uses functions like `include()`, `require()`, `file_get_contents()`, or `readfile()` because your `curl` command successfully returned the contents of `/etc/passwd`

## Conclusion

Agent Q implemented a **security theater mechanism**.

The obfuscated JavaScript was designed to appear as a protection layer but had:

- Zero backend validation
    
- No absolute path restriction
    
- No server-side filtering
    
The vulnerability is a classic **Local File Inclusion (LFI)** via absolute path injection.

FLAG::`THJCC{h0w_dID_y0u_br34k_q'5_pr073c710n???}`




















