import sys
import os
import re

class VM:
    def __init__(self):
        self.stack = []
        self.vars = {}
        self.labels = {}
        self.pc = 0
        self.code = []
        self.call_stack = []
        self.halted = False
        self.output_lines = []

    def load(self, code_lines):
        self.code = []
        self.labels = {}
        for line in code_lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if line.endswith(':'):
                label = line[:-1].strip()
                self.labels[label] = len(self.code)
            else:
                self.code.append(line)

    def get_value(self, s):
        s = s.strip()
        try:
            if '.' in s:
                return float(s)
            return int(s)
        except ValueError:
            if s in self.vars:
                return self.vars[s]
            return 0

    def set_value(self, name, val):
        self.vars[name] = val

    def run(self, trace=False):
        self.pc = 0
        self.halted = False
        while not self.halted and self.pc < len(self.code):
            if trace:
                print(f"\nPC={self.pc}: {self.code[self.pc]}")
                print(f"  stack={self.stack}")
                print(f"  vars={self.vars}")
            jumped = self.execute(self.code[self.pc])
            if not jumped:
                self.pc += 1
        
        if self.stack:
            ret_val = self.stack[-1]
            self.output_lines.append(str(ret_val))

    def execute(self, instr):
        parts = instr.split()
        if not parts:
            return False

        op = parts[0]

        if op == 'push':
            val = self.get_value(' '.join(parts[1:]))
            self.stack.append(val)
            return False

        elif op == 'pop':
            if self.stack:
                val = self.stack.pop()
                result_var = None
                idx = instr.find('=')
                if idx > 0:
                    result_var = instr[:idx].strip()
                if result_var:
                    self.set_value(result_var, val)
            else:
                self.output_lines.append("ERROR: pop from empty stack")
                self.halted = True
            return False

        elif op == 'pop_args':
            n = int(parts[1]) if len(parts) > 1 else 0
            for _ in range(n):
                if self.stack:
                    self.stack.pop()
            return False

        elif op == 'return':
            if self.call_stack:
                ret_addr = self.call_stack.pop()
                self.pc = ret_addr
                return True
            else:
                self.halted = True
                return True

        elif op == 'call':
            func_name = parts[1].rstrip(',')
            if func_name == 'print':
                if self.stack:
                    val = self.stack.pop()
                    self.output_lines.append(str(val))
                return True
            if func_name in self.labels:
                self.call_stack.append(self.pc)
                self.pc = self.labels[func_name]
                return True
            else:
                self.output_lines.append(f"ERROR: funcion {func_name} no encontrada")
                self.halted = True
                return True

        elif op == 'goto':
            label = parts[1].strip()
            if label in self.labels:
                self.pc = self.labels[label]
                return True
            else:
                for i, line in enumerate(self.code):
                    if line.strip().rstrip(':') == label:
                        self.pc = i
                        return True
                self.output_lines.append(f"ERROR: label {label} no encontrada")
                self.halted = True
                return True

        elif op == 'ifFalse':
            rest = ' '.join(parts[1:])
            goto_idx = rest.find(' goto ')
            if goto_idx > 0:
                cond_expr = rest[:goto_idx].strip()
                label = rest[goto_idx + 6:].strip()
                val = self._evaluar_cond(cond_expr)
                if val == '0' or val == 0 or val is False:
                    if label in self.labels:
                        self.pc = self.labels[label]
                        return True
                    else:
                        for i, line in enumerate(self.code):
                            if line.strip().rstrip(':') == label:
                                self.pc = i
                                return True
                        self.output_lines.append(f"ERROR: label {label} no encontrada")
                        self.halted = True
                        return True
            return False

        elif op == 'ifTrue':
            rest = ' '.join(parts[1:])
            goto_idx = rest.find(' goto ')
            if goto_idx > 0:
                cond_expr = rest[:goto_idx].strip()
                label = rest[goto_idx + 6:].strip()
                val = self._evaluar_cond(cond_expr)
                if val == '1' or val == 1 or val is True:
                    if label in self.labels:
                        self.pc = self.labels[label]
                        return True
                    else:
                        for i, line in enumerate(self.code):
                            if line.strip().rstrip(':') == label:
                                self.pc = i
                                return True
                        self.output_lines.append(f"ERROR: label {label} no encontrada")
                        self.halted = True
                        return True
            return False

        elif op == 'print':
            if len(parts) > 1:
                val = self.get_value(parts[1])
                self.output_lines.append(str(val))
            elif self.stack:
                val = self.stack.pop()
                self.output_lines.append(str(val))
            return False

        elif op == 'print_str':
            if len(parts) > 1:
                s = ' '.join(parts[1:])
                self.output_lines.append(s)
            return False

        elif op == 'halt':
            self.halted = True
            return False

        elif '=' in instr:
            idx = instr.find('=')
            dest = instr[:idx].strip()
            expr = instr[idx+1:].strip()
            val = self._evaluar_expresion(expr)
            self.set_value(dest, val)
            return False
        
        return False

    def _evaluar_cond(self, expr):
        expr = expr.strip()
        operators = ['==', '!=', '<=', '>=', '<', '>']
        for op in operators:
            if op in expr:
                parts = expr.split(op, 1)
                a = self.get_value(parts[0].strip())
                b = self.get_value(parts[1].strip())
                if op == '==': return '1' if a == b else '0'
                if op == '!=': return '1' if a != b else '0'
                if op == '<=': return '1' if a <= b else '0'
                if op == '>=': return '1' if a >= b else '0'
                if op == '<': return '1' if a < b else '0'
                if op == '>': return '1' if a > b else '0'

        val = self.get_value(expr)
        return '1' if val != 0 else '0'

    def _evaluar_expresion(self, expr):
        expr = expr.strip()
        if expr.startswith('(') and expr.endswith(')'):
            return self._evaluar_expresion(expr[1:-1])
        import re
        comp_ops = [('==', lambda a,b: 1 if a == b else 0), ('!=', lambda a,b: 1 if a != b else 0), ('<=', lambda a,b: 1 if a <= b else 0), ('>=', lambda a,b: 1 if a >= b else 0), ('<', lambda a,b: 1 if a < b else 0), ('>', lambda a,b: 1 if a > b else 0)]
        for op_sym, fn in comp_ops:
            parts = re.split(r'\s*' + re.escape(op_sym) + r'\s*', expr, maxsplit=1)
            if len(parts) == 2:
                a_str, b_str = parts[0].strip(), parts[1].strip()
                if a_str and b_str:
                    a = self._evaluar_expresion(a_str)
                    b = self._evaluar_expresion(b_str)
                    return fn(a, b)
        operators = [('+', lambda a,b: a+b), ('-', lambda a,b: a-b)]
        for op_sym, fn in operators:
            idx = self._find_op_outside_parens(expr, op_sym)
            if idx >= 0:
                a = self._evaluar_expresion(expr[:idx])
                b = self._evaluar_expresion(expr[idx+1:])
                return fn(a, b)
        operators2 = [('*', lambda a,b: a*b), ('/', lambda a,b: a/b if b != 0 else 0), ('%', lambda a,b: a % b if b != 0 else 0)]
        for op_sym, fn in operators2:
            idx = self._find_op_outside_parens(expr, op_sym)
            if idx >= 0:
                a = self._evaluar_expresion(expr[:idx])
                b = self._evaluar_expresion(expr[idx+1:])
                return fn(a, b)
        if expr in self.vars:
            return self.vars[expr]
        try:
            if '.' in expr:
                return float(expr)
            return int(expr)
        except:
            return 0

    def _find_op_outside_parens(self, s, op):
        parens = 0
        for i, ch in enumerate(s):
            if ch == '(':
                parens += 1
            elif ch == ')':
                parens -= 1
            elif ch == op and parens == 0:
                return i
        return -1


def main():
    import sys
    filename = sys.argv[1] if len(sys.argv) > 1 else os.path.join('output', 'CodigoOptimizado.txt')
    filename = os.path.normpath(filename)
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: archivo {filename} no encontrado")
        return

    vm = VM()
    vm.load(lines)
    vm.run(trace=False)
    print("\n=== SALIDA VM ===")
    for line in vm.output_lines:
        print(line)
    print("=== FIN ===")

if __name__ == '__main__':
    main()
