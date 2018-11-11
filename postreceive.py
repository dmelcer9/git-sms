#!/usr/bin/env python3

import sys
from git import Repo
import os
import pdb
from unidiff import PatchSet
from twilio.rest import Client

client = Client()

def process_commits_between(old, new):
    repo = Repo(os.environ["GIT_REPO_PATH"])
    
    thiscommit = repo.commit(new)

    if thiscommit.message.startswith("Incoming message"):
        return

    rawdiff = repo.git.diff(old, new)

    parseddiff = PatchSet(rawdiff)

    for file in parseddiff:
        for hunk in file:
            for line in hunk.target_lines():
                if line.is_added and line.value.strip() != "" :
                    phoneNum = os.path.splitext(os.path.basename(file.target_file))[0]
                    print("Send message %s to %s" % (line.value.strip(), phoneNum))

                    client.messages.create(
                            to= "+" + phoneNum,
                            from_= "+" + os.environ["FROM_PHONE_NUM"],
                            body= line.value.strip())
                
                

def main():
    try:
        for line in sys.stdin:
            old, new, ref = line.strip().split(' ')
            if ref == 'refs/heads/master':
                process_commits_between(old, new)
    except Exception as e:
        print(str(e))
        sys.exit(1)

if __name__ == '__main__':
    # process_commits_between("10eedc1865fb403018ab9bb91761f78a9d5da8fa", "9f62fed1fc885ecac65adec9f1e9aee824665db9")
    main()
