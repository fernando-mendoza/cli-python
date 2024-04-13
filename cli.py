import click
import utils

@click.group()
def cli():
    pass

@cli.command()
def users():
    users = utils.read_json()
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")

if __name__ == '__main__':
    cli()
