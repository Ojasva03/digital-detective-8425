# Mission 6 - Git and GitHub

> AI-assisted working draft. Commands and tests described as performed were run by the assistant on this computer. Review the explanations and write your final understanding in your own words. Local preparation proceeded while GitHub access was unavailable; the assignment's required push-before-next-mission sequence has not been fulfilled.

## 1. Task / objective
Use staging and commits, create a branch, and prepare GitHub collaboration documentation.

## 2. Work completed
Created dedicated local mission commits, inspected status/history, and created update-about with a committed My Learning section. Returned to main. Both branches are published. Pull request #1 is open and unmerged; its README learning change has been reviewed locally.

## 3. Commands / tools used
| Operation | Command | Explanation |
|---|---|---|
| Initialize | `git init -b main` | Create local Git metadata and main branch |
| Check status | `git status` | Show staged, unstaged and untracked files |
| Stage selected files | `git add README.md` | Select the current README changes for the next commit |
| Commit | `git commit -m "message"` | Record the staged snapshot in local history |
| History | `git log --oneline` | Show local commits concisely |
| Create branch | `git switch -c update-about` | Create and switch to a new branch |
| List branches | `git branch` | Display local branch names |
| Switch branch | `git switch main` | Return to the main branch |
| Inspect changes | `git diff main...update-about -- README.md` | Show the proposed branch change |
| Publish | `git push -u origin main` | Upload commits and establish tracking |
| Retrieve | `git fetch origin` | Download remote objects and references |
| Integrate (pending) | `git pull --ff-only` | Fetch and fast-forward the current branch when possible |

## 4. My understanding
Staging selects the file versions that the next commit will record. Committing saves those staged versions as a local snapshot; it does not upload anything. A push sends commits to a remote repository.

A branch is a movable name for a line of development. The update-about branch contains a README learning section while main keeps its existing README. A pull request proposes integrating one branch into another and gives reviewers a place to inspect and discuss the diff.

### Pull request status

Open and unmerged: https://github.com/Ojasva03/digital-detective-8425/pull/1. Source branch: update-about. Target branch: main. Both branches were pushed successfully. The local proposed diff was reviewed and changes only README.md by adding My Learning. Do not merge unless the instructor requests it.

Suggested PR title: **Add My Learning section to the project overview**.

Suggested PR description: **Adds a short learning section about paths, number representation and the difference between local commits and GitHub pushes. Only the root README changes.**

## 5. Difficulties faced
The first main push was rejected because GitHub contained a separate initial README commit. GitHub CLI was absent. No personal email was supplied for local Git authorship.

## 6. How I resolved them
Created real local commits and branch evidence. Used the supplied handle and an empty author email to avoid inventing or publishing an email. Fetched origin/main, merged its initial history while keeping the assignment README, and merged main into the learning branch without rewriting published history. Pushed both branches, verified the public repository using the GitHub API, and created pull request #1.

## 7. Evidence / files
- [Branch diff](../evidence/mission-06/branch-diff.txt)
- [Publication instructions](PUBLISHING.md)
- Git history in .git (local metadata, not a repository file)

## 8. Commit details
Local commit message: `Complete Git and GitHub collaboration mission`.
GitHub push: mission commits published to the public repository on 2026-11-15. Publication occurred after offline preparation; the original per-mission push sequence was not followed.
