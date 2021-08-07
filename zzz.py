import click

click.clear()
@click.command()
def up():
    """Обновление системы."""
    click.secho('EASYQUEST!',bg='yellow',fg='black')
    click.pause()
    click.launch('http://easyquest.host/')
