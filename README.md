# mgit

## Intallation :

### Requirements

    * Python 2.7 or newer
        Since GitPython 2.0.0. Please note that python 2.6 is still reasonably well supported, but might deteriorate over time. Support is provided on a best-effort basis only.

    * Git 1.7.0 or newer
        It should also work with older versions, but it may be that some operations involving remotes will not work as expected.
    
    * $ sudo apt-get install python-pip python-dev build-essential 
    
    * sudo pip install gitpython
    
    * sudo pip install colorama
        
    * copy/paste mgit.py in the root directory that contains your git projects
    
### Usage
    --list-branch or -l : list all branches for all projects
    --list-project-for-branch or -p : list all projects for a given branch
    --switch-all or -s : switch all project on a given local branch, no branch creation
    python mgit.py --list-branch     
    python mgit.py --list-project-for-branch feature/TH-0000     
    python mgit.py --switch-all feature/TH-0000     
   

