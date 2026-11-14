# Mission 4 - How programs run

> AI-assisted working draft. Commands and tests described as performed were run by the assistant on this computer. Review the explanations and write your final understanding in your own words. Local preparation proceeded while GitHub access was unavailable; the assignment's required push-before-next-mission sequence has not been fulfilled.

## 1. Task / objective
Run a one-line Python program and compare compilation with interpretation.

## 2. Work completed
Created hello.py, ran it using Python 3, and verified the exact message Hello from Python. Prepared the comparison below.

## 3. Commands / tools used
- `python3 hello.py`: runs the saved program.
- `print`: writes a message to standard output.

## 4. My understanding
| Point | Compiler | Interpreter |
|---|---|---|
| Translation / execution | Translates source into another form before that result runs | Executes instructions at runtime |
| Typical output | Object code, executable code or bytecode | Program behavior/output during execution |
| Example | Clang compiling C to machine code | CPython executing Python bytecode |
| Advantage | Native compiled output can run efficiently | Supports quick interactive experimentation |

A compiler translates source code into another representation before that result executes. An interpreter carries out instructions at runtime. Real implementations can combine both: CPython compiles Python source to bytecode, then executes it using its interpreter. Therefore, calling Python interpreted does not mean that no compilation takes place.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [hello.py](hello.py)
- [Execution output](../evidence/mission-04/hello-output.txt)

## 8. Commit details
Local commit message: `Compare compilers and interpreters`.
GitHub push: pending; no remote publication has been verified.
