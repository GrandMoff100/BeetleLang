import logging


class CommandQueue:
    commands = []
    index = 0

    def put(self, obj):
        self.commands.append(obj)

    def get(self):
        try: 
            command = self.commands[0]
        except IndexError:
            exit(logging.error(f'Expected a hex pair after pair {self.index}'))
        else:
            self.commands.pop(0)
            self.index += 1
            return command

    def empty(self):
        return self.qsize() == 0

    def qsize(self):
        return len(self.commands)


class Program:
    _commands = CommandQueue()

    def add_command(self, text: str, index: int):
        self._commands.put(Command.process(text, index))
        return self

    def run(self):
        while not self._commands.empty():
            cmd = self._commands.get()
            cmd.run(self)

    def run_next(self, raw=False):
        cmd = self._commands.get()
        if raw:
            return cmd.text
        return cmd.run(self)

    def __len__(self):
        return self._commands.qsize()


class Command:
    commands = {}

    def __init__(self, text: str, index: int):
        self.text = text
        self.index = index

    def __repr__(self):
        return f'{type(self).__name__}({self.text!r})'

    def __init_subclass__(cls):
        Command.commands.update({cls.text: cls})

    def run(self, program: Program):
        pass

    def process(text: str, index: str):
        return Command.commands.get(text, Command)(text, index)


class Print(Command):
    text = 'ff'

    def run(self, program: Program):
        print(program.run_next())


class Int(Command):
    text = '01'

    def run(self, program: Program):
        count = int(program.run_next(raw=True), 16)
        digits = [program.run_next(raw=True) for _ in range(count)]
        return int(''.join(digits), 16)


class Add(Command):
    text = '10'

    def run(self, program: Program):
        a = program.run_next()
        b = program.run_next()
        return a + b


class Sub(Command):
    text = '11'

    def run(self, program: Program):
        a = program.run_next()
        b = program.run_next()
        return a - b


class Mul(Command):
    text = '12'

    def run(self, program: Program):
        a = program.run_next()
        b = program.run_next()
        return a * b


class Div(Command):
    text = '13'

    def run(self, program: Program):
        a = program.run_next()
        b = program.run_next()
        return a / b


class String(Command):
    text = '02'

    def run(self, program: Program):
        length = int(program.run_next(raw=True), 16)
        pairs = map(lambda _: program.run_next(raw=True), range(length))
        numbers = map(lambda pair: int(pair, 16), pairs)
        chars = map(chr, numbers)
        return ''.join(chars)


