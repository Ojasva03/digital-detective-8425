# Mission 6 - Git and GitHub

> AI-assisted working draft. Commands and tests described as performed were run by the assistant on this computer. Review the explanations and write your final understanding in your own words. Local preparation proceeded while GitHub access was unavailable; the assignment's required push-before-next-mission sequence has not been fulfilled.

## 1. Task / objective
Use staging and commits, create a branch, and prepare GitHub collaboration documentation.

## 2. Work completed
Created dedicated local mission commits, inspected status/history, and created update-about with a committed My Learning section. Returned to main. The branch remains local and unmerged; no pull request exists yet.

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
| Publish (pending) | `git push -u origin main` | Upload commits and establish tracking |
| Retrieve (pending) | `git fetch origin` | Download remote objects and references |
| Integrate (pending) | `git pull --ff-only` | Fetch and fast-forward the current branch when possible |

## 4. My understanding
Staging selects the file versions that the next commit will record. Committing saves those staged versions as a local snapshot; it does not upload anything. A push sends commits to a remote repository.

A branch is a movable name for a line of development. The update-about branch contains a README learning section while main keeps its existing README. A pull request proposes integrating one branch into another and gives reviewers a place to inspect and discuss the diff.

### Pull request status

Not created. Source branch: update-about. Target branch: main. Local diff is saved as evidence. Branch push, PR creation and review are pending authenticated GitHub access. Do not merge unless the instructor requests it; no merge has been performed.

Suggested PR title: **Add My Learning section to the project overview**.

Suggested PR description: **Adds a short learning section about paths, number representation and the difference between local commits and GitHub pushes. Only the root README changes.**

## 5. Difficulties faced
GitHub tools are unavailable in this task and GitHub CLI is absent. Installation was reported but access has not been verified. No personal email was supplied for Git authorship.

## 6. How I resolved them
Created real local commits and branch evidence. Used the supplied handle and an empty author email to avoid inventing or publishing an email. Documented the exact publication steps without claiming they ran.

## 7. Evidence / files
- [Branch diff](../evidence/mission-06/branch-diff.txt)
- [Publication instructions](PUBLISHING.md)
- Git history in .git (local metadata, not a repository file)

## 8. Commit details
Local commit message: `Complete Git and GitHub collaboration mission`.
GitHub push: pending; no remote publication has been verified.
