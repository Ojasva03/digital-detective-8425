# Mission 5 - Numbers and data

> AI-assisted working draft. Commands and tests described as performed were run by the assistant on this computer. Review the explanations and write your final understanding in your own words. Local preparation proceeded while GitHub access was unavailable; the assignment's required push-before-next-mission sequence has not been fulfilled.

## 1. Task / objective
Show number-conversion working, verify with Python, build and test a decimal converter, and explain text encoding.

## 2. Work completed
Prepared all seven worked conversions, ran the Python verification expressions, tested the converter with three positive integers plus zero, and checked invalid input and EOF handling.

## 3. Commands / tools used
- `python3 -i -q`: interactive Python verification.
- `input`: reads the entered text.
- `int(text, 10)`: parses a decimal integer.
- `bin`: formats an integer in base 2 with a 0b prefix.
- `hex`: formats an integer in base 16 with a 0x prefix.
- `ord`: returns a character code point.

## 4. My understanding
### Task 5.1 - Worked conversions for review

| Conversion | Working | Answer |
|---|---|---|
| Decimal 13 to binary | 13=1x8+1x4+0x2+1x1 | 1101 |
| Decimal 25 to binary | 25=1x16+1x8+0x4+0x2+1x1 | 11001 |
| Binary 1010 to decimal | 1x8+0x4+1x2+0x1=8+2 | 10 |
| Binary 1101 to decimal | 1x8+1x4+0x2+1x1=8+4+1 | 13 |
| Hexadecimal A to decimal | A is the digit with value 10; 10x16^0 | 10 |
| Hexadecimal 1F to decimal | 1x16+15x1=16+15 | 31 |
| Binary 1111 to hexadecimal | 1x8+1x4+1x2+1x1=15; hex digit for 15 is F | F |

Binary place values are powers of 2; hexadecimal place values are powers of 16. Leading zeros do not change the numeric value. Four binary digits can represent the values of one hexadecimal digit.

### Task 5.2 - Python verification

| Expression | Result | Matches working? |
|---|---|---|
| `bin(13)` | `0b1101` | Yes |
| `bin(25)` | `0b11001` | Yes |
| `int('1010', 2)` | `10` | Yes |
| `int('1101', 2)` | `13` | Yes |
| `int('A', 16)` | `10` | Yes |
| `int('1F', 16)` | `31` | Yes |
| `hex(int('1111', 2))` | `0xf` | Yes |
| `hex(13)` | `0xd` | Yes, the same integer 13 |
| `hex(25)` | `0x19` | Yes, 1x16+9=25 |

### Task 5.3 - Converter behavior

| Input | Binary output | Hexadecimal output |
|---|---|---|
| 13 | 0b1101 | 0xd |
| 25 | 0b11001 | 0x19 |
| 31 | 0b11111 | 0x1f |
| 0 | 0b0 | 0x0 |

The program reads text, converts it to an integer, rejects negative values and prints binary and hexadecimal strings. Invalid text, fractional text and missing input produce a clear message and a nonzero exit status. The prefixes identify the bases; they are not additional digits.

### Task 5.4 - Text encoding

A bit is one binary digit; eight bits make one byte. Uppercase A has ASCII decimal code 65 and lowercase a has code 97, confirmed by `ord('A')` and `ord('a')`. An encoding standard gives programs a shared rule for representing characters as bytes so that saved text can be decoded consistently. Basic ASCII has 128 character codes; UTF-8 encodes Unicode characters in one to four bytes and represents ASCII characters with the same single-byte values. The character `₹` is outside basic ASCII.

## 5. Difficulties faced
`input()` returns text, and converting invalid text with int raises ValueError. End-of-input raises EOFError.

## 6. How I resolved them
Handled both exceptions and tested the resulting messages and exit statuses.

## 7. Evidence / files
- [number_converter.py](number_converter.py)
- [Converter tests](../evidence/mission-05/converter-tests.txt)
- [Python verification](../evidence/mission-05/python-verification.txt)

## 8. Commit details
Local commit message: `Build number converter and practise data representation`.
GitHub push: mission commits published to the public repository on 2026-11-15. Publication occurred after offline preparation; the original per-mission push sequence was not followed.
