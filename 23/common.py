class Computer:
    def __init__(self, a=0):
        with open('input.txt') as code:
            self.instructions = [line.strip() for line in code.readlines()]

        self.a, self.b, self.pc = a, 0, 0

    def run(self):
        while self.pc < len(self.instructions):
            values = self.instructions[self.pc].replace(',', ' ').split()
            instruction = values[0]
            op1 = values[1]

            if instruction == 'hlf':
                if op1 == 'a':
                    self.a /= 2
                else:
                    self.b /= 2

            elif instruction == 'tpl':
                if op1 == 'a':
                    self.a *= 3
                else:
                    self.b *= 3

            elif instruction == 'inc':
                if op1 == 'a':
                    self.a += 1
                else:
                    self.b += 1

            elif instruction == 'jmp':
                self.pc += int(op1) - 1

            elif instruction == 'jie':
                op2 = int(values[2])
                if op1 == 'a' and self.a % 2 == 0:
                    self.pc += op2 - 1
                elif op1 == 'b' and self.b % 2 == 0:
                    self.pc += op2 - 1

            elif instruction == 'jio':
                op2 = int(values[2])
                if op1 == 'a' and self.a == 1:
                    self.pc += op2 - 1
                elif op1 == 'b' and self.b == 1:
                    self.pc += op2 - 1

            self.pc += 1

        return self.b
