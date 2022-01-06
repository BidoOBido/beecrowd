import click, updater_util, os


def _getPath():
    _parent_directory = os.path.join(os.path.split(__file__)[0], os.path.pardir)

    return os.path.abspath(_parent_directory)


@click.group()
def main():
    """
    Simple CLI for help in beecrowd problem solving
    """
    pass


@main.command()
def update_readme():
    """
    This updates de readme file
    """
    click.echo(updater_util.update(_getPath()))


if __name__ == "__main__":
    main()
