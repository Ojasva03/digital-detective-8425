# Mission 3 - Understand the operating system

## 1. Task / objective
Inspect the OS, account, storage, processes, paths and permissions, and explain OS responsibilities.

## 2. Work completed
Checked macOS details, current-account identity, storage and a practice file permission mode. Saved redacted evidence. Opened the practice file in TextEdit and identified PID 83781 in a successful process snapshot outside the sandbox.

## 3. Commands / tools used
- `sw_vers`: OS version/build.
- `whoami`: active account (output withheld).
- `df -h .`: filesystem capacity/usage.
- `ps -Ao pid,comm`: initial blocked process listing.
- `open -a TextEdit`: opened the practice file in the editor.
- `ps -Ao pid,pcpu,pmem,comm`: successful PID and activity snapshot, restricted to selected rows in evidence.
- `pwd`, `cd`, `ls -l`: paths and file metadata.
- Python stat and os.getpid: file mode and the collector process PID.

## 4. My understanding
### Task 3.1 - System observations

| Information | What it tells us | Observation |
|---|---|---|
| Operating system | OS product, version and build | See captured `sw_vers` output |
| Account identity | Which account runs the command | Checked, then redacted |
| Storage | Filesystem size, used space and available space | See captured `df -h .` output; values are a point-in-time snapshot |
| System activity | Processes currently running | Follow-up selected snapshot: launchd PID 1 and TextEdit PID 83781; CPU and memory percentages recorded |

### Task 3.2 - Processes

A process is a running instance of a program with its own execution state and resources. Its PID is a numeric identifier assigned by the OS; it can change between runs and may later be reused. Python and a web browser are examples of programs that can run as processes; the Python collector PID is actually observed in the evidence. TextEdit was opened with the practice file and observed with PID 83781; the background process launchd was observed with PID 1. TextEdit showed 0.0% CPU and 0.5% memory in this brief snapshot, while launchd showed 0.6% CPU and 0.1% memory. These values can change immediately.

### Task 3.3 - Paths and permissions

An absolute path begins at the filesystem root. A relative path begins from the current working directory. A privacy-redacted absolute example is `/Users/[redacted]/digital-detective-8425/mission-03-operating-system/README.md`; a relative example from the repository root is `mission-03-operating-system/README.md`. The placeholder is explanatory and is not a literal usable path.

In the permission mode recorded in the evidence, the first character indicates file type and the next three positions describe the owner's read, write and execute permissions. A dash means that permission is absent. A Python script can be read by `python3` without itself having an execute bit.

| Permission | File meaning | Directory meaning |
|---|---|---|
| r | Read contents | List entry names |
| w | Modify contents | Add/remove entries when traversal is also allowed |
| x | Execute as a program | Traverse/access entries |

The observed owner permissions allow reading, writing. The owner execute bit is absent.

### Task 3.4 - OS responsibilities

| Responsibility | Explanation | Example |
|---|---|---|
| Process management | Schedule running programs and track their states | Share CPU time between a browser and editor |
| Memory management | Allocate memory and isolate address spaces | Give an editor memory for a document |
| Device management | Coordinate hardware through drivers | Send print data to a printer |
| File management | Organize files, directories and metadata | Save a document in a mission folder |
| User interface / shell | Provide ways to request actions | Run a command in Terminal |
| Security and permissions | Control which accounts can access resources | Refuse writing to a protected file |

## 5. Difficulties faced
The initial process-list attempt was blocked by the sandbox. Private account details must not be published.

## 6. How I resolved them
Retried the observation outside the sandbox, opened TextEdit, and saved selected PID/activity rows. Redacted private names and paths from other observations.

## 7. Evidence / files
- [System observations](../evidence/mission-03/system-observations.txt)
- [Practice file](../mission-02-terminal/terminal-practice/original.txt)

## 8. Commit details
Local commit message: `Document operating system and file management`.
GitHub push: mission commits published to the public repository on 2026-11-15.
