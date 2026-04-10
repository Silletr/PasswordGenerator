from passwordgen import generate_password
from passwordgen.enhancer.mutator import apply_policy
import typer

from .vault import Vault

app = typer.Typer()


@app.command()
def generate(
    length: int = 32,
    policy: bool = False,
):
    """Generates a random password
    P.S from Silletr - Even owner of this app,
    dont know your password from Youtube
    (promise)
    """
    password = generate_password(length)
    if policy:
        password = apply_policy(
            password,
            min_digits=5,
            min_upper=3,
            min_symbols=5,
            min_lower=1,  # usually you also need at least one lowercase
        )
        typer.echo(password)
    if not policy:
        typer.echo(password)
        typer.echo("!!! Warning !!! No policy applied")
        typer.echo("To enable policy add --policy in prompt (pls)")


@app.command()
def save(site: str, user: str):
    """
    Generate and save a password
    """
    password = generate_password(16)
    vault = Vault()
    vault.save_entry(site, user, password)
    typer.echo(f"Saved {site} / {user}")


@app.command()
def entry_list():
    """List all saved entries"""
    vault = Vault()
    entries = vault.entries_list()
    for entry in entries:
        typer.echo(f"{entry['site']} / {entry['user']}")


def main():
    app()


if __name__ == "__main__":
    main()
