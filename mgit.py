import os
import os.path as osp
import sys

import git
from colorama import Fore
from colorama import init
from git import Repo

init()

# TODO : Better manage script params
args = sys.argv


def is_git_repo(path):
    try:
        _ = git.Repo(path).git_dir
        return True
    except git.exc.InvalidGitRepositoryError:
        return False


def list_branch():
    for directory in os.listdir("."):
        if osp.isdir(directory):
            os.chdir(directory)
            lchild_dir = os.getcwd()
            if is_git_repo(lchild_dir):
                print(Fore.GREEN + "#################")
                print(Fore.GREEN + "Directory: " + directory)
                repo = Repo(lchild_dir)
                branches = repo.heads
                for b in branches:
                    print(b)
            os.chdir("..")


def list_remote_branch():
    for directory in os.listdir("."):
        if osp.isdir(directory):
            os.chdir(directory)
            lchild_dir = os.getcwd()
            if is_git_repo(lchild_dir):
                print(Fore.GREEN + "#################")
                print(Fore.GREEN + "Directory: " + directory)
                repo = Repo(lchild_dir)
                remote_branches = repo.remotes.origin.refs
                for b in remote_branches:
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
    project_switch = list()
    wanted_branch = args[2]
    print(Fore.YELLOW + "Switch to branch: " + wanted_branch)
    if wanted_branch:
        for directory in os.listdir("."):
            if osp.isdir(directory):
                os.chdir(directory)
                child_dir = os.getcwd()
                if is_git_repo(child_dir):
                    print(Fore.GREEN + "######################## " + child_dir)
                    repo = Repo(child_dir)
                    if str(repo.active_branch) == wanted_branch:
                        os.chdir("..")
                        print(Fore.LIGHTCYAN_EX + "Already on : " + wanted_branch)
                        print("  ")
                        continue
                    branches = repo.heads
                    remote_branches = repo.remotes.origin.refs
                    checked_out = False
                    for branch in branches:
                        if wanted_branch == str(branch):
                            print(Fore.CYAN + child_dir + " switch to branch " + str(branch))
                            repo.git.checkout(wanted_branch)
                            checked_out = True
                            project_switch.append(child_dir)
                            break
                    if not checked_out:
                        print(Fore.MAGENTA + "not a local branch try remote")
                        for remote_branch in remote_branches:
                            branch_name = str(remote_branch).lstrip("origin/")
                            if wanted_branch == branch_name:
                                print(Fore.CYAN + child_dir + " switch to remote branch " + str(branch))
                                repo.git.checkout(branch_name)
                                project_switch.append(child_dir)
                                checked_out = True
                                break
                    if not checked_out:
                        print(Fore.LIGHTMAGENTA_EX + "No branch: " + wanted_branch + " for project: " + child_dir)
                os.chdir("..")
                print("  ")
    print(Fore.LIGHTBLUE_EX + "projects switch to: " + wanted_branch)
    for p in project_switch:
        print(Fore.LIGHTGREEN_EX + p)


def mgit():
    if args[1] == "--help" or args[1] == "-h":
        print("--list-branch or -l : list all local branches for all projects")
        print("--list-remote-branch or -r : list all remote branches for all projects")
        print("--list-project-for-branch or -p : list all projects for a given branch")
        print(
            "--switch-all or -s : switch all projects on a given branch (locally first, in remote otherwise), "
            "no branch creation")

    elif args[1] == "--list-branch" or args[1] == "-l":
        list_branch()

    elif args[1] == "--list-remote-branch" or args[1] == "-r":
        list_remote_branch()

    elif args[1] == "--list-project-for-branch" or args[1] == "-p":
        list_project_for_branch()

    elif args[1] == "--switch-all" or args[1] == "-s":
        switch_projects_to_branch()


if __name__ == '__main__':
    mgit()
