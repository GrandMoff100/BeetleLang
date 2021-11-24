import rply
from beetle.commands import Program


class Interpreter:
    lg = rply.LexerGenerator()
    tokens = {
        'COMMAND': '[a-f0-9]{2}'
    }
    pg = rply.ParserGenerator(tokens)

    @pg.production("cmds : COMMAND")
    @pg.production("cmds : cmds COMMAND")
    def cmds(p):
        if len(p) == 1:
            program = Program()
            return program.add_command(p[0].value, 0)
        elif len(p) == 2:
            return p[0].add_command(p[1].value, len(p[0]))

    def __init__(self):
        for name, pattern in self.tokens.items():
            self.lg.add(name, pattern)
        self.lg.ignore('\s')

    def compile(self, code: str):
        lexer = self.lg.build()
        parser = self.pg.build()
        try:
            return parser.parse(lexer.lex(code))
        except rply.errors.LexingError as exc:
            pos = exc.source_pos.colno
            print(f'Unexpected {code[pos + 1]!r} at postion {pos}')
