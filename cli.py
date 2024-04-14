import click
import utils

@click.group()
def cli():
    pass


@cli.command()
@click.option('--name', required=True, help='Name of the user')
@click.option('--lastname', required=True, help='Lastname of the user')
@click.pass_context
def new_user(ctx, name, lastname):
    if not name or not lastname:
        ctx.fail('the name and lastname are required')
    else:
        data = utils.read_json()
        new_id = len(data) + 1
        new_user = {
            'id': new_id,
            'name': name,
            'lastname': lastname
        }
        data.append(new_user)
        utils.write_json(data)
        print(f"User {name} - {lastname} created successfully with id {new_id}")

@cli.command()
def users():
    users = utils.read_json()
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")

@cli.command()
@click.argument('id', type=int)
def user(id):
    data = utils.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"User with id {id} not found")
    else:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")

@cli.command()
@click.argument('id', type=int)
def delete(id):
    data = utils.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"User with id {id} not found")
    else:
        data.remove(user)
        utils.write_json(data)
        print(f"User with id {id} deleted successfully!")

if __name__ == '__main__':
    cli()
