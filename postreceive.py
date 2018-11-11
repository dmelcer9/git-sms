#!/usr/bin/env python3

import sys
from git import Repo
import os
import pdb
from unidiff import PatchSet

def process_commits_between(old, new):
    repo = Repo(os.environ["GIT_REPO_PATH"])
    end = repo.commit(new)
    for diff in end.diff(old, create_patch=True).iter_change_type('A'):
        for message in diff.b_blob.data_stream.read().decode("utf-8").strip().split("\n"):
                print("Send message %s to %s" % (message, diff.b_path))
                

def main():
    for line in sys.stdin:
        old, new, ref = line.strip().split(' ')
        if ref == 'refs/heads/master':
            process_commits_between(old, new)

if __name__ == '__main__':
    process_commits_between("39439cfac68cd2acd6ae8363214d3339ee241006", "10eedc1865fb403018ab9bb91761f78a9d5da8fa") 
    # main()
