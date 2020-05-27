import click
from modules.simple_app import simple_app
import time

def colorizer(text_no_decorate, text_to_decorate, color):
    click.echo(
        text_no_decorate + click.style(
        (str(text_to_decorate)), 
        fg = color
    ))

@click.group()
def main():
    pass

@main.command('create')
@click.argument('name', 
                default = 'my_first_app', nargs = 1)
@click.option('--mode', '-m', 
              default = 'simple_app', nargs = 1, required=False)
@click.option("--arch", "-a",
              default = "mvc")
def create(name, mode, arch):
    """create structure app.
       args:
          kv create meu_app
    """
    colorizer("[mode] ", mode, 'green')
    colorizer("[arch] ", arch, 'green')
    simple_app(name)
    with click.progressbar(
        iterable = [1,2], label = '[create]',
        bar_template='%(label)s %(bar)s | %(info)s',
        fill_char=click.style(u'█', fg='cyan'),
        empty_char=' ') as bar:
        for x in bar:
            time.sleep(x)
    colorizer("[status] ", f'{name} created', 'green')

@main.command('run')
def run():
    click.launch("py " + __file__)


# @click.option("--simple_app", "-sa", 
#               default = True)

# def main(project_name, simple_app, arch):


#     from pyfiglet import Figlet
#     f = Figlet(font = 'slant')
#     click.echo(click.style(
#         f.renderText("Kivy CLI"), fg = 'blue'
#     ))
#     colorizer('', "Welcome to Kivy CLI", 'green')
#     colorizer('Project Name: ', project_name, 'blue')
#     colorizer('Project Mode: ', simple_app, 'blue')
#     colorizer('Project Arch: ', arch, 'blue')

if __name__ == "__main__":
    main()
    click.pause()