

  * [HEAD](https://github.com/rixwoodling/raspberry-pi/blob/master/test.md#head)
  * [Screenshot](#screenshot)
  * [Installation](#installation)
        * [OR using Pathogen:](#or-using-pathogen)
        * [OR using Vundle:](#or-using-vundle)
  * [License](#license)

###The Path of Git-lightenment

Exploring a new Git Init
Linear Commits
Checking Out the Past
Custom Configs
Branch Management 
Merge Management
Push/Pulk Revolving Doors (Github)
Exploring an old Git Init
Further Study

####Create a new local git repository
####Exploring a new Git Init 

1. Start a new git repository with ```git init``` in an empty folder.
2. Type in ```ls -a```, and then ```cd .git```. 
3. Type in ```ls -lh``` or ```ls -lh -F```.
```bash
-rw-r--r--@  1 rixwoodling  staff    23B May  7 19:58 HEAD
drwxr-xr-x@  2 rixwoodling  staff    68B May  7 19:58 branches
-rw-r--r--@  1 rixwoodling  staff   137B May  7 19:58 config
-rw-r--r--@  1 rixwoodling  staff    73B May  7 19:58 description
drwxr-xr-x@ 11 rixwoodling  staff   374B May  7 19:58 hooks
drwxr-xr-x@  3 rixwoodling  staff   102B May  7 19:58 info
drwxr-xr-x@  4 rixwoodling  staff   136B May  7 19:58 objects
drwxr-xr-x@  4 rixwoodling  staff   136B May  7 19:58 refs
```
A new git initialization creates a handful of files and folders. Note the permissions and count numbers in the first two columns (fields). 

#####HEAD
Open "HEAD" with ```nano HEAD```. All it should say is:
```bash
ref: refs/heads/master
```
<sup>Jump to here to see what happens when commits are made.</sup>

#####branches/
Open ```branches/``` directory using ```cd branches``` and type ```ls -a```. 
```bash
.     ..
```
<sup>Jump to here to see what happens when commits are made.</sup>

#####config
Open "config" to view the default value configurations.
```bash
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
        ignorecase = true
        precomposeunicode = true
```
7. Open "description".
```bash
Unnamed repository; edit this file 'description' to name the repository.
```
8. Open "hooks" directory. ```ls -a1```
```bash
.
..
applypatch-msg.sample
commit-msg.sample
post-update.sample
pre-applypatch.sample
pre-commit.sample
pre-push.sample
pre-rebase.sample
prepare-commit-msg.sample
update.sample
```
9. Open "info" directory... (then,```ls -a1F```)
```bash
./    
../    
exclude
```
    ...Open "exclude".
```bash
# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~
```
10. Open objects.

References
http://www.thegeekstuff.com/2009/07/linux-ls-command-examples/
