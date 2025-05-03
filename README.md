# Mathematical Expression Lexer

## Course: Formal Languages & Finite Automata

### Author: Cvasiuc Dmitrii

---

## Overview

This project implements a **lexical analyzer (lexer/scanner)** for mathematical expressions. The lexer reads a raw string containing a mathematical expression and breaks it down into a **sequence of tokens**—structured objects representing numbers, operators, and functions. These tokens can then be fed into a parser for further processing.

---

## Theory Behind Lexical Analysis

**Lexical analysis** is the process of converting a sequence of characters into a sequence of tokens. This process is often the first step in the compilation or interpretation of source code.

The lexer operates like a **finite state machine (FSM)**:

* It reads one character at a time.
* Based on the current character, it decides which type of token is being processed.
* It collects the necessary characters to form that token.
* Then, it creates a token object and moves to the next part of the input.

---

## Implementation Details

### `Token` Class

```python
class Token:
    def __init__(self, token_type, value=None, position=None):
        self.type = token_type
        self.value = value
        self.position = position

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)}, pos={self.position})"
```

* `token_type`: a string that describes what kind of token it is (e.g., `"INTEGER"`, `"PLUS"`).
* `value`: the actual content of the token (e.g., the number `3.14` or string `"sin"`).
* `position`: a tuple to help identify where in the input this token appeared (line, column). Useful for debugging or error reporting.

---

### Selected Token Types

```python
# Token types
INTEGER = 'INTEGER'
FLOAT = 'FLOAT'
PLUS = 'PLUS'
MINUS = 'MINUS'
MUL = 'MUL'
DIV = 'DIV'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
SIN = 'SIN'
COS = 'COS'
SQRT = 'SQRT'
LOG = 'LOG'
EOF = 'EOF'  # End of file/input
```

Each constant represents a specific token that the lexer can identify. This separation of type names makes the code more readable and easier to extend.

---

### Number Parsing Function

```python
def number(self):
    result = ''
    is_float = False
    
    while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
        if self.current_char == '.':
            if is_float:  # Prevent multiple dots
                raise Exception("Invalid number format")
            is_float = True
        result += self.current_char
        self.advance()
        
    return Token(FLOAT if is_float else INTEGER, 
                 float(result) if is_float else int(result), 
                 (self.line, self.column))
```

* **Purpose**: Parses both integers and floating-point numbers.
* **Key logic**:

  * Iterates through digits and a possible decimal point.
  * Converts the final string into either `int` or `float`.
  * Tracks whether the number is a float using `is_float`.
  * Returns a `Token` with appropriate type and value.

---

### Recognizing Reserved Functions

```python
KEYWORDS = {
    'sin': SIN,
    'cos': COS,
    'sqrt': SQRT,
    'log': LOG
}
```

When a sequence of letters (an identifier) is found, it’s checked against this dictionary:

* If it's a known mathematical function like `"sin"` or `"log"`, the lexer returns the associated token.
* Otherwise, this could be extended in the future to support user-defined variables.

---

### Example of Tokenizing Input

```python
lexer = Lexer("sin(0.5) + 2 * 3")
tokens = lexer.tokenize()
for token in tokens:
    print(token)
```

**Expected Output**:

```
Token(SIN, 'sin', pos=(1, 1))
Token(LPAREN, '(', pos=(1, 4))
Token(FLOAT, 0.5, pos=(1, 5))
Token(RPAREN, ')', pos=(1, 8))
Token(PLUS, '+', pos=(1, 10))
Token(INTEGER, 2, pos=(1, 12))
Token(MUL, '*', pos=(1, 14))
Token(INTEGER, 3, pos=(1, 16))
```

Each token is printed with its type, value, and location—very useful for debugging and parser integration.

---

## Usage Examples

### Basic Tokenization

```python
lexer = Lexer("3 + 4.5 * 2")
tokens = lexer.tokenize()
```

This will produce tokens for `3`, `+`, `4.5`, `*`, and `2`.

### Interactive REPL Mode

```python
while True:
    text = input('> ')
    if not text:
        continue
    tokens = Lexer(text).tokenize()
    for token in tokens:
        print(token)
```

This allows you to test expressions live in the console and see how they are tokenized.

---

## Conclusion

This lexer successfully implements a tokenizer for mathematical expressions by applying key **theoretical concepts** from formal languages and finite automata:

### Key Concepts Demonstrated

1. **Finite State Machine (FSM)**

   * The lexer transitions between states based on character classes (digits, operators, letters).

2. **Multi-Type Token Recognition**

   * Supports both numeric and symbolic types (e.g., numbers, operators, functions).

3. **Position Tracking**

   * Each token tracks where it appeared for potential error reporting.

4. **Stream Processing**

   * Characters are processed one-by-one using lookahead via `self.advance()`.

---

### Challenges Encountered

* Handling multiple decimal points in a float (e.g., `3..14`) required careful validation.
* Differentiating between functions like `sin` and variables involved checking a reserved keyword table.

---

### Future Improvements

* Add **variable support**: allow identifiers beyond reserved keywords.
* Implement an **expression parser** to evaluate the tokenized expressions.
* Provide **better error messages** with suggestions for fixes.

---

## References

1. [Wikipedia - Lexical Analysis](https://en.wikipedia.org/wiki/Lexical_analysis)
2. [Crafting Interpreters - Chapter 4: Scanning](https://craftinginterpreters.com/scanning.html)

---

## Repository

🔗 [GitHub Repository](https://github.com/dmitrycvs/Lexer)
