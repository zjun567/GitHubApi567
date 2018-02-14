# -*- coding: utf-8 -*-
import json
import urllib.request, urllib.parse, urllib.error


def result(user):
    """get the repo and commit number"""
    
    url = 'https://api.github.com/users/' + user + '/repos'
    repo1 = urllib.request.urlopen(url)
    data = repo1.read().decode()
    js1 = json.loads(data)
    number = len(js1) - 1
    repos = list()

    for i in (0, number):
        repos.append(js1[i]['name'])

    commits = list()

    for repo in repos:
        commit_url = 'https://api.github.com/repos/' + user + '/' + repo + '/commits'
        commit = urllib.request.urlopen(commit_url)
        commit_data = commit.read().decode()
        js2 = json.loads(commit_data)
        commits.append(len(js2))

    return number, repos, commits


def main():
    user = input('username: ')
    results = result(user)

    print('User: ' + user)
    
    for n in (0, results[0]):
        print('Repo: ' + str(results[1][n]) + '  Number of commits: ' + str(results[2][n]))


if __name__ == '__main__':
    main()