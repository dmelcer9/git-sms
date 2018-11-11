#!/usr/bin/env python3

import sys

def process_commits_between(old, new):


def main():
    for line in sys.stdin:
        old, new, ref = line.strip().split(' ')
        if ref == 'refs/heads/master':
            process_commits_between(old, new)

if __name__ == '__main__':
    main()
