PS C:\Users\Onex Cellular\Desktop\hackingtool> Remove-Item -Recurse -Force 
PS C:\Users\Onex Cellular\Desktop\hackingtool> git add .
PS C:\Users\Onex Cellular\Desktop\hackingtool> 
                                                  
PS C:\Users\Onex Cellular\Desktop\hackingtool> git commit -m "My First Com
Author identity unknown

*** Please tell me who you are.
Run


to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'Onex Cellular@DESKTOP-KPOK4AD.(none)')
PS C:\Users\Onex Cellular\Desktop\hackingtool> git config --global user.email "onexfrp@gmail.com"
PS C:\Users\Onex Cellular\Desktop\hackingtool> git config --global user.name "Chanaka Anuradhapura"
>> 
PS C:\Users\Onex Cellular\Desktop\hackingtool> 
PS C:\Users\Onex Cellular\Desktop\hackingtool> git commit -m "My First Commit" [main (root-commit) 34a42eb] My First Commit
 56 files changed, 6191 insertions(+)
 create mode 100644 .dockerignore
 create mode 100644 Dockerfile
 create mode 100644 LICENSE
 create mode 100644 README.md
 create mode 100644 README_template.md
 create mode 100644 config.py
 create mode 100644 constants.py
 create mode 100644 core.py
 create mode 100644 docker-compose.yml
 create mode 100644 generate_readme.py
 create mode 100644 hackingtool.py
 create mode 100644 images/A.png
 create mode 100644 images/AA.png
 create mode 100644 images/AAA.png
 create mode 100644 images/AAAA.png
 create mode 100644 images/AAAAA.png
 create mode 100644 images/demo
 create mode 100644 images/logo.svg
 create mode 100644 install.py
 create mode 100644 install.sh
 create mode 100644 os_detect.py
 create mode 100644 requirements.txt
 create mode 100644 tools/__init__.py
 create mode 100644 tools/active_directory.py
 create mode 100644 tools/anonsurf.py
 create mode 100644 tools/cloud_security.py
 create mode 100644 tools/ddos.py
 create mode 100644 tools/exploit_frameworks.py
 create mode 100644 tools/forensics.py
 create mode 100644 tools/information_gathering.py
 create mode 100644 tools/mobile_security.py
 create mode 100644 tools/other_tools.py
 create mode 100644 tools/others/__init__.py
 create mode 100644 tools/others/android_attack.py
 create mode 100644 tools/others/email_verifier.py
 create mode 100644 tools/others/hash_crack.py
 create mode 100644 tools/others/homograph_attacks.py
 create mode 100644 tools/others/mix_tools.py
 create mode 100644 tools/others/payload_injection.py
 create mode 100644 tools/others/socialmedia.py
 create mode 100644 tools/others/socialmedia_finder.py
 create mode 100644 tools/others/web_crawling.py
 create mode 100644 tools/others/wifi_jamming.py
 create mode 100644 tools/payload_creator.py
 create mode 100644 tools/reverse_engineering.py
 create mode 100644 tools/sql_injection.py
 create mode 100644 tools/tool_manager.py
 create mode 100644 tools/web_attack.py
 create mode 100644 tools/wireless_attack.py
 create mode 100644 tools/wordlist_generator.py
 create mode 100644 tools/xss_attack.py
 create mode 100644 update.sh
PS C:\Users\Onex Cellular\Desktop\hackingtool> git branch -M Main     
PS C:\Users\Onex Cellular\Desktop\hackingtool> git remote add origin https://github.com/onexfrp-art/First-Project.git
PS C:\Users\Onex Cellular\Desktop\hackingtool> git push -u origin main
info: please complete authentication in your browser...
PS C:\Users\Onex Cellular\Desktop\hackingtool> git push -u origin Main
Enumerating objects: 60, done.
Counting objects: 100% (60/60), done.
Delta compression using up to 4 threads
Compressing objects: 100% (58/58), done.
Writing objects: 100% (60/60), 1010.96 KiB | 7.96 MiB/s, done.
Total 60 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), done.
branch 'Main' set up to track 'origin/Main'.
PS C:\Users\Onex Cellular\Desktop\hackingtool> git push -u origin Sample
error: src refspec Sample does not match any
PS C:\Users\Onex Cellular\Desktop\hackingtool> git add .                                                             
PS C:\Users\Onex Cellular\Desktop\hackingtool> git commit -m "My Commit 2"                                           
Your branch is up to date with 'origin/Main'.

nothing to commit, working tree clean
PS C:\Users\Onex Cellular\Desktop\hackingtool> git add .                  
PS C:\Users\Onex Cellular\Desktop\hackingtool> git commit -m "My Commit 2"
[Main ab30a6e] My Commit 2
 1 file changed, 1 insertion(+)
 create mode 100644 Sample/Sample.py
PS C:\Users\Onex Cellular\Desktop\hackingtool> git push -u origin Sample  
error: src refspec Sample does not match any
Counting objects: 100% (5/5), done.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (4/4), 347 bytes | 347.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/onexfrp-art/First-Project.git
branch 'Main' set up to track 'origin/Main'.
PS C:\Users\Onex Cellular\Desktop\hackingtool> 
PS C:\Users\Onex Cellular\Desktop\hackingtool> git add .
Switched to a new branch 'feature/My-First-Branch'
PS C:\Users\Onex Cellular\Desktop\hackingtool> git status
On branch feature/My-First-Branch
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   Sample/Sample2.py

PS C:\Users\Onex Cellular\Desktop\hackingtool> git commit -m "My Commit 3"            
[feature/My-First-Branch 4b992cd] My Commit 3
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 Sample/Sample2.py
PS C:\Users\Onex Cellular\Desktop\hackingtool> git push -u origin feature/My-First-Branch
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Compressing objects: 100% (3/3), done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote: 
remote: Create a pull request for 'feature/My-First-Branch' on GitHub by visiting:
remote: 
To https://github.com/onexfrp-art/First-Project.git
 * [new branch]      feature/My-First-Branch -> feature/My-First-Branch
branch 'feature/My-First-Branch' set up to track 'origin/feature/My-First-Branch'.
PS C:\Users\Onex Cellular\Desktop\hackingtool> git checkout .                            
Updated 0 paths from the index
PS C:\Users\Onex Cellular\Desktop\hackingtool> git status                                
On branch feature/My-First-Branch
Your branch is up to date with 'origin/feature/My-First-Branch'.

nothing to commit, working tree clean
PS C:\Users\Onex Cellular\Desktop\hackingtool> git checkout Main
Switched to branch 'Main'
Your branch is up to date with 'origin/Main'.
PS C:\Users\Onex Cellular\Desktop\hackingtool> git pull
remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (1/1), 894 bytes | 298.00 KiB/s, done.
From https://github.com/onexfrp-art/First-Project
   ab30a6e..910c1c0  Main       -> origin/Main
Updating ab30a6e..910c1c0
Fast-forward
 Sample/Sample2.py | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 Sample/Sample2.py
PS C:\Users\Onex Cellular\Desktop\hackingtool> 




