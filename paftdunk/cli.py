import random
import logging

import click


@click.group()
def main():
    pass


@click.command()
@click.option('--sides', default=6, help='how many sides your ')
@click.option('--times', default=1, help='name of the user')
def roll(sides, times):
    eyes = sum([random.randint(1, sides) for _ in range(times)])
    click.echo(f"we rolled {times} dice and got {eyes} eyes")


@click.command()
@click.option('--name', default=6, help='how many sides your ')
def hello(name):
    click.echo("running hello command")
    click.echo(f"hello {name}")


main.add_command(roll)
main.add_command(hello)


if __name__ == "__main__":
    main()
