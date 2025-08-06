import click
from models import PowInput, FibInput, FactInput
from logic import calculate_pow, calculate_fib, calculate_fact
from storage import save_request

@click.group()
def cli():
    """CLI pentru operații matematice."""
    pass

@cli.command()
@click.option('--base', type=int, required=True)
@click.option('--exp', type=int, required=True)
def pow(base, exp):
    data = PowInput(base=base, exponent=exp)
    result = calculate_pow(data)
    save_request("pow", data.dict(), result)
    click.echo(f"Rezultat: {result}")

@cli.command()
@click.option('--n', type=int, required=True)
def fib(n):
    data = FibInput(n=n)
    result = calculate_fib(data)
    save_request("fib", data.dict(), result)
    click.echo(f"Rezultat: {result}")

@cli.command()
@click.option('--n', type=int, required=True)
def fact(n):
    data = FactInput(n=n)
    result = calculate_fact(data)
    save_request("fact", data.dict(), result)
    click.echo(f"Rezultat: {result}")

if __name__ == '__main__':
    cli()
