#!/usr/bin/env python3
# First time I use [[click]] ~ anagora.org/click, it looks cool like the other [[pallets project]], [[flask]], which we use in [[agora server]].
# https://click.palletsprojects.com/en/8.1.x/arguments/
# https://click.palletsprojects.com/en/8.1.x/options/

import click
import io
import math

# I'm not proud (I am a little bit?).
PROOF = [] # :)

class RichGroup(click.Group):
    def format_help(self, ctx, formatter):
        sio = io.StringIO()
        console = rich.Console(file=sio, force_terminal=True)
        console.print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:")
        formatter.write(sio.getvalue())

@click.group(cls=RichGroup)
def cli():
    pass

def factor(n):
    for i in range(2, n+1):
        click.echo(f"Is {i} a factor of {n}, I wonder?")

def is_prime(n):
    is_prime = [True for n in range(0, n+1)]
    upto = math.ceil(math.sqrt(n))
    for i, _ in enumerate(is_prime):
        # click.echo(f"i: {i}")
        if i < 2:
            continue
        # If we're above the square root, we can stop considering the first factor, as we'll try higher numbers in the inner loop.
        if i > upto:
            break
        # If this is a known composite, then we've already crossed off its multiples when we iterated over its primes.
        if not is_prime[i]:
            continue
        # for j in range(2, math.ceil(math.sqrt(n) + 1)):
        for j in range(2, n):
            # I wrote >= here initially. That did *not* work ;)
            if i * j > n:
                break
            PROOF.append(f"[[{i*j}]] is composite: {i} * {j}.")
            try:
                is_prime[i*j] = False
            except IndexError:
                continue
    # click.echo(f"Sieve: {is_prime}.")
    return is_prime[n]

@click.command()
@click.group(cls=RichGroup)
@click.argument('n', type=click.INT)
def prime(n):
    """Simple program that factors a number using a [[Sieve of Eratosthenes]]."""
    if is_prime(n):
        click.echo(f"[[{n}]] is prime.")
    else:
        click.echo(f"{n} is not prime. Want proof? :)")
        click.echo("\n".join([line for line in PROOF if f'[[{n}]]' in line]))

if __name__ == '__main__':
    prime()
