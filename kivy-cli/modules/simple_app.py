import click

def simple_app(name):
    click.echo(f'[register] {click.style((name), fg = "yellow")}')