#!/usr/bin/env python

import click


@click.command()
@click.argument("names", nargs=-1)
@click.option('-g', '--greeting', default="Hello")
@click.option('--question/--no-question')
def cli(names, greeting, question):
    if question:
        punctuation = "?"
    else:
        punctuation = "!"
    for name in names:
        print(f"{greeting}, {name}{punctuation}")


if __name__ == "__main__":
    cli()
