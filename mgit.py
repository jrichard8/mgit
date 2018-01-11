import os
import os.path as osp
import sys

import git
from git import Repo


def is_git_repo(path):
    try:
        _ = git.Repo(path).git_dir
        return True
    except git.exc.InvalidGitRepositoryError:
        return False


args = sys.argv


def list_branch():
    for directory in os.listdir("."):
        if osp.isdir(directory):
            os.chdir(dir)
            lchild_dir = os.getcwd()
            if is_git_repo(lchild_dir):
                print("#################")
                print("Directory: " + directory)
                lrepo = Repo(lchild_dir)
                lbranches = lrepo.heads
                for b in lbranches:
                    print(b)
            os.chdir("..")


def list_project_for_branch():
    if args[2]:
        for directory in os.listdir("."):
            if osp.isdir(directory):
                os.chdir(directory)
                child_dir = os.getcwd()
                if is_git_repo(child_dir):
                    repo = Repo(child_dir)
                    branches = repo.heads
                    for branch in branches:
                        if args[2] == str(branch):
                            print(os.getcwd())
                            break
                os.chdir("..")


def switch_projects_to_branch():
    print("Switch to branch: " + args[2])
    if args[2]:
        for directory in os.listdir("."):
            if osp.isdir(directory):
                os.chdir(directory)
                child_dir = os.getcwd()
                if is_git_repo(child_dir):
                    repo = Repo(child_dir)
                    branches = repo.heads
                    for branch in branches:
                        if args[2] == str(branch):
                            print(os.getcwd() + " switch to branch " + str(branch))
                            repo.git.checkout(args[2])
                os.chdir("..")


if args[1] == "--help" or args[1] == "-h":
    print("--list-branch or -l : list all branches for all projects")
    print("--list-project-for-branch or -p : list all projects for a given branch")
    print("--switch-all or -s : switch all project on a given local branch, no branch creation")

elif args[1] == "--list-branch" or args[1] == "-l":
    list_branch()

elif args[1] == "--list-project-for-branch" or args[1] == "-p":
    list_project_for_branch()

elif args[1] == "--switch-all" or args[1] == "-s":
    switch_projects_to_branch()
