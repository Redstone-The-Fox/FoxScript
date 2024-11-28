def textafter(text, aft): return text.split(aft)[1] 

class Interpreter:
    def execute(self, code):
        lines = code.splitlines()
        variables = {}
        print(lines, '\n', sep='')
        print('foxscript.py Interpreter v1.05\n')
        for line in lines:
            if line.startswith('printl '):
                print(textafter(line, 'printl ').strip('"'))
            elif line.startswith('print '):
                print(textafter(line, 'print ').strip('"'), end='')
            elif line.startswith('math-printl '):
                eval(f'print(str({textafter(line, 'math-printl ')}))')
            elif line.startswith('var-printl '):
                print(variables[textafter(line, 'var-printl ').strip('{').strip('}')])
            elif line.startswith('var-print '):
                print(variables[textafter(line, 'var-print ').strip('{').strip('}')], end='')
            elif line.startswith('let '):
                variables[textafter(line, 'let ').split(': ', 1)[0]] = textafter(line, ': ').strip('"')
            elif line == 'printvars':
                print(variables)
            elif line == '': ...
            elif line.startswith('::'): ...
            else: exit(f'INVALID: {line}')

interpreter = Interpreter()
with open('testfile.fxsc', 'rt+') as f:
    code = f.read()
interpreter.execute(code)