import click
import updater_util


@click.group()
def main():
    """
    Simple CLI for help in beecrowd problem solving
    """
    pass


@main.command()
@click.argument("path")
def update_readme(path):
    """
    This updates de readme file\n
    - PATH\t indicate the path to the beecrowd directory
    """
    click.echo(updater_util.update(path))


if __name__ == "__main__":
    main()
