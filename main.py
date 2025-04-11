class Token:
    def __init__(self, token_type, value=None, position=None):
        self.type = token_type
        self.value = value
        self.position = position

    def __repr__(self):
        if self.value is not None:
            return f"Token({self.type}, {repr(self.value)}, pos={self.position})"
        return f"Token({self.type}, pos={self.position})"


class Lexer:
    INTEGER = 'INTEGER'
    FLOAT = 'FLOAT'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    DIVIDE = 'DIVIDE'
    POWER = 'POWER'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    SIN = 'SIN'
    COS = 'COS'
    SQRT = 'SQRT'
    LOG = 'LOG'
    COMMA = 'COMMA'
    EOF = 'EOF'

    KEYWORDS = {
        'sin': SIN,
        'cos': COS,
        'sqrt': SQRT,
        'log': LOG
    }

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None
        self.line = 1
        self.column = 1

    def error(self):
        raise Exception(f'Invalid character {repr(self.current_char)} at position {self.pos} (line {self.line}, column {self.column})')

    def advance(self):
        if self.current_char == '\n':
            self.line += 1
            self.column = 0
        
        self.pos += 1
        self.column += 1
        
        if self.pos >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def peek(self, n=1):
        peek_pos = self.pos + n
        if peek_pos >= len(self.text):
            return None
        return self.text[peek_pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def number(self):
        position = (self.line, self.column)
        result = ''
        is_float = False
        
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                if is_float:
                    self.error()
                is_float = True
            result += self.current_char
            self.advance()
            
        if is_float:
            return Token(Lexer.FLOAT, float(result), position)
        else:
            return Token(Lexer.INTEGER, int(result), position)

    def identifier(self):
        position = (self.line, self.column)
        result = ''
        
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
            
        token_type = self.KEYWORDS.get(result.lower())
        if token_type:
            return Token(token_type, result.lower(), position)
        
        self.error()

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
                
            position = (self.line, self.column)
                
            if self.current_char.isdigit():
                return self.number()
                
            if self.current_char.isalpha():
                return self.identifier()
                
            if self.current_char == '+':
                self.advance()
                return Token(Lexer.PLUS, '+', position)
                
            if self.current_char == '-':
                self.advance()
                return Token(Lexer.MINUS, '-', position)
                
            if self.current_char == '*':
                self.advance()
                return Token(Lexer.MULTIPLY, '*', position)
                
            if self.current_char == '/':
                self.advance()
                return Token(Lexer.DIVIDE, '/', position)
                
            if self.current_char == '^':
                self.advance()
                return Token(Lexer.POWER, '^', position)
                
            if self.current_char == '(':
                self.advance()
                return Token(Lexer.LPAREN, '(', position)
                
            if self.current_char == ')':
                self.advance()
                return Token(Lexer.RPAREN, ')', position)
                
            if self.current_char == ',':
                self.advance()
                return Token(Lexer.COMMA, ',', position)
                
            self.error()
            
        return Token(Lexer.EOF, position=(self.line, self.column))

    def tokenize(self):
        tokens = []
        token = self.get_next_token()
        
        while token.type != Lexer.EOF:
            tokens.append(token)
            token = self.get_next_token()
            
        tokens.append(token)
        return tokens


def main():
    while True:
        try:
            text = input('> ')
            if not text:
                continue
            
            lexer = Lexer(text)
            tokens = lexer.tokenize()
            
            for token in tokens:
                print(token)
                
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    examples = [
        "3 + 4.5 * 2",
        "sin(0.5) + cos(1)",
        "sqrt(16) + log(100)",
        """2 ^ 3 
        + (4 * 5)
        """
    ]
    
    print("Testing the lexer with examples:")
    for example in examples:
        print(f"\nInput: {example}")
        lexer = Lexer(example)
        tokens = lexer.tokenize()
        for token in tokens:
            print(token)
    
    print("\nEnter mathematical expressions to tokenize (press Ctrl+C to exit):")
    main()
