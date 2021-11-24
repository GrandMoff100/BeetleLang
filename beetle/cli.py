import click
from beetle.interpreter import Interpreter


interpreter = Interpreter()


@click.command()
def cli():
    while True:
        interpreter.compile(input(">>> ")).run()


cli()


