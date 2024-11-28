def textafter(text, aft): return text.split(aft)[1] 

class FoxScriptInterpreter:
    def execute(self, code):
        lines = code.splitlines()
        variables = {}
        print(lines, '\n', sep='')
        print('foxscript.py Interpreter v1.05')
        for line in lines:
            if line.startswith('printl '):
                print(textafter(line, 'printl ').strip('"'))
            elif line.startswith('print '):
                print(textafter(line, 'print ').strip('"'), end='')
            elif line.startswith('math-printl '):
                eval(f'print(str({textafter(line, 'math-printl ')}))')
            elif line.startswith('let '):
                variables[textafter(line, 'let ').split(': ', 1)[0]] = textafter(line, ': ').strip('"')
            elif line == 'printvars':
                print(variables)
            elif line == '': ...
            else: exit(f'INVALID: {line}')

interpreter = FoxScriptInterpreter()
code = """
let hw: "Hello, World!"
print "Hello, "
printl "World!"
printl "Welcome to FoxScript!"
print "3+3 = "
math-printl 3+3
printvars
"""
interpreter.execute(code)