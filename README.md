# Cloudsek Hackathon [![Made with Python](https://img.shields.io/badge/python-3.5.2%20|%203.8.0-grey?style=for-the-badge&labelColor=yellow&logo=python)](https://www.python.org/)   [![Uses Multithreading](https://img.shields.io/badge/Uses-Multi%20threading-grey?style=for-the-badge&labelColor=blue)](https://www.python.org/)

## Problem Statement by CloudSEK: Build a minimal web path bruteforcer: Optimised memory, CPU usage

### The CLI interface to the web path bruteforcer should accept these from the user:
<ul> <li>webapp url</li>
<li>A file containing a list of webapp paths that need to be brute forced against the specified webapp url [Minimum paths: 1000]<br>
Sample wordlist: Link </li>
<li>List of success status code: (default: [200])</li>
</ul>
<h3> Sample Input:</h3>

Webapp url: https://www.github.com<br>
Webapp paths: sample 5 lines out of 1000 of the input file wordlist.txt
<ul><li>admin</li>
<li>info</li>
<li> .git/config</li>
<li> .htaccess </li>
<li>backup.zip
</li></ul>

Success status codes: [200, 302]

## Usage:
```
python app.py [url] [word file] [status code]
```

### Example
```
python app.py www.github.com file.txt 200 302
```
