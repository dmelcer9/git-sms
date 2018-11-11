#!/usr/bin/env python3

import sys
from git import Repo
import os
import pdb
from unidiff import PatchSet

def process_commits_between(old, new):
    repo = Repo(os.environ["GIT_REPO_PATH"])
    rawdiff = repo.git.diff(old, new)

    parseddiff = PatchSet(rawdiff)

    for file in parseddiff:
        for hunk in file:
            for line in hunk.target_lines():
                if line.is_added and line.value.strip() != "" :
                    print("Send message %s to %s" % (line.value.strip(), os.path.split(file.target_file)[1]))
                
                

def main():
    for line in sys.stdin:
        old, new, ref = line.strip().split(' ')
        if ref == 'refs/heads/master':
            process_commits_between(old, new)

if __name__ == '__main__':
    process_commits_between("10eedc1865fb403018ab9bb91761f78a9d5da8fa", "9f62fed1fc885ecac65adec9f1e9aee824665db9")
    # main()
