import typer
from passwordgen import generate_password
from .vault import Vault

app = typer.Typer()


@app.command()
def generate(length: int = 32):
    """Generates a random password
    P.S from Silletr - Even owner of this app,
    dont know your password from Youtube
    (promise)
    """
    typer.echo(generate_password(length))


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
