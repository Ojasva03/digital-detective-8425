# Mission 2 - Become comfortable with the Terminal

> AI-assisted working draft. Commands and tests described as performed were run by the assistant on this computer. Review the explanations and write your final understanding in your own words. Local preparation proceeded while GitHub access was unavailable; the assignment's required push-before-next-mission sequence has not been fulfilled.

## 1. Task / objective
Practise Terminal file operations, options, pipes and package-manager inspection.

## 2. Work completed
Ran file creation, append, copy, rename, directory navigation and listing operations inside the repository. Both practice files contain the same two lines. Checked the existing Homebrew version and formula list without installing or removing packages.

## 3. Commands / tools used
| Command | Purpose | Observation |
|---|---|---|
| `pwd` | Print the current absolute path | Ended in the repository folder; personal prefix redacted |
| `ls` | List visible entries | Displayed the mission folders and root README |
| `ls -l` | Show a detailed listing | Added permissions, sizes and other metadata |
| `cd ..` | Move to the parent directory | Returned from the mission folder to the repository |
| `mkdir -p terminal-practice` | Create a practice directory | The directory exists |
| `touch original.txt` | Create an empty file | The file existed before text was written |
| `cp original.txt backup.txt` | Copy a file | Created a separate copy |
| `mv backup.txt renamed-backup.txt` | Rename a file | The backup appeared under its new name |
| `cat original.txt` | Display contents | Both lines appeared |
| `ls -lah` | Long listing, hidden entries, readable sizes | Included dot entries and metadata |
| `ls -l | head -n 3` | Pass listing output to a line limiter | Displayed only the first three listing lines |
| `brew --version` | Inspect installed Homebrew version | Homebrew 7.0.9 |
| `brew list --formula` | List managed formulae | Included git and other existing formulae |

## 4. My understanding
The shell runs commands relative to its working directory. `pwd` identifies that location and `ls` shows the entries available there. Copying makes another file; moving changes a file's location or name.

`>` creates a file or replaces its current contents, while `>>` appends text at the end. The two separate `printf` operations kept both lines because the second used `>>`.

Options modify a command: `-l` requests details, `-a` includes hidden entries and `-h` formats sizes for reading. A pipe sends standard output from the command on its left into standard input of the command on its right. Here, `ls -l` produces listing lines and `head -n 3` selects the first three.

A package manager tracks software packages and their dependencies. It helps install, update and remove managed software consistently. This activity inspected the existing Homebrew installation and made no package changes.

## 5. Difficulties faced
No major difficulties during the file-management practice. Detailed listings can expose local account names.

## 6. How I resolved them
Redacted local names and home-directory prefixes before saving the transcript.

## 7. Evidence / files
- [Command transcript](../evidence/mission-02/terminal-output.txt)
- [Original file](terminal-practice/original.txt)
- [Renamed backup](terminal-practice/renamed-backup.txt)

## 8. Commit details
Local commit message: `Complete Terminal and file management mission`.
GitHub push: pending; no remote publication has been verified.
