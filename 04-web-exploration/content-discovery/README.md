# Content discovery

Find unlinked paths and files. Brute forcing is intrusive - authorisation required.

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [dirhunt](dirhunt.md) | What directory structure does this site have, worked out **without** brute forcing thousands of paths at it? | 2 | active |
| [feroxbuster](feroxbuster.md) | I am authorised to test this site. What directories and files exist that nothing links to - and what is inside the directories I... | 2 | intrusive |
| [ffuf](ffuf.md) | I am authorised to test this site. What happens if I substitute a wordlist into *this specific position* - a path, a parameter... | 2 | intrusive |
| [gobuster](gobuster.md) | I am authorised to test this target. What directories, DNS subdomains, or virtual hosts exist, brute-forced from a wordlist? | 2 | intrusive |
| [DirBuster](dirbuster.md) | What directories and files exist on this web server that nothing links to? | 3 | intrusive |
| [wfuzz](wfuzz.md) | What happens when I substitute a wordlist into any part of an HTTP request - path, parameter, header, or cookie? | 3 | intrusive |
<!-- END:TOOLS -->
