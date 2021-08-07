import click

click.clear()
@click.command()
def up():
    """Обновление системы."""
    click.secho('EASYQQUEST!',bg='yellow',fg='black')
    click.launch('help')
