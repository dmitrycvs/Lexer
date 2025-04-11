# Mathematical Expression Lexer

## Course: Formal Languages & Finite Automata
### Author: [Cvasiuc Dmitrii]

---

## Overview
This project implements a lexical analyzer (lexer/scanner) for mathematical expressions. The lexer transforms input strings containing mathematical expressions into a sequence of tokens that can be used for further processing, such as parsing and evaluation.

## Theory Behind Lexical Analysis

Lexical analysis is the process of converting a sequence of characters into a sequence of tokens. The lexer operates as a finite state machine, transitioning between states as it reads characters from the input.

## Implementation Details

### Token Class

```python
class Token:
    def __init__(self, token_type, value=None, position=None):
        self.type = token_type
        self.value = value
        self.position = position
```

### Selected Token Types

```python
# Token types (abbreviated)
INTEGER = 'INTEGER'
FLOAT = 'FLOAT'
PLUS = 'PLUS'
MINUS = 'MINUS'
# ...
```

### Number Parsing

```python
def number(self):
    result = ''
    is_float = False
    
    while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
        if self.current_char == '.':
            is_float = True
        result += self.current_char
        self.advance()
        
    return Token(Lexer.FLOAT if is_float else Lexer.INTEGER, 
                 float(result) if is_float else int(result), 
                 (self.line, self.column))
```

### Function Recognition

```python
# Reserved keywords
KEYWORDS = {
    'sin': SIN,
    'cos': COS,
    'sqrt': SQRT,
    'log': LOG
}
```

### Tokenization Example

```python
# Example usage
lexer = Lexer("sin(0.5) + 2 * 3")
tokens = lexer.tokenize()
for token in tokens:
    print(token)

# Output:
# Token(SIN, 'sin', pos=(1, 1))
# Token(LPAREN, '(', pos=(1, 4))
# ...
```

## Usage Examples

```python
# Basic usage
lexer = Lexer("3 + 4.5 * 2")
tokens = lexer.tokenize()

# Interactive mode
while True:
    text = input('> ')
    if not text: continue
    tokens = Lexer(text).tokenize()
    for token in tokens:
        print(token)
```

## Conclusion

This lexer successfully implements a tokenizer for mathematical expressions by applying concepts from formal languages and finite automata. The implementation demonstrates how to:

1. **Create a finite state machine** for recognizing different token patterns
2. **Handle multiple token types** including numbers, operators, and functions
3. **Maintain position information** for detailed error reporting
4. **Process input streams** character by character with lookahead capability

The lexer serves as a foundation for a potential expression parser and evaluator. Through this project, we've seen how theoretical concepts of lexical analysis can be applied to solve a practical programming problem. The implementation is simple yet effective, and follows good software engineering practices like modularity and clean separation of concerns.

The challenges encountered included handling decimal numbers correctly and recognizing mathematical functions. Future work could include extending the lexer to support variables and implementing an associated parser to evaluate the tokenized expressions.

## References

1. [Wikipedia - Lexical Analysis](https://en.wikipedia.org/wiki/Lexical_analysis)
2. [Crafting Interpreters - Chapter 4: Scanning](https://craftinginterpreters.com/scanning.html)

---

## Repository

[GitHub Repository](https://github.com/dmitrycvs/Lexer)
