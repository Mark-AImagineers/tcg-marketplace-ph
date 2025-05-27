import typer
from typing_extensions import Annotated

def main(
    command: Annotated[str, typer.Argument(help="Commands: check, pull, status")]
):
    if command == "check":
        typer.echo("Running sync check")
        # from .checker import run_check
        # run_check()

    elif command == "pull":
        typer.echo("Running data puller")
        # from .puller import run_puller
        # run_puller()

    elif command == "status":
        typer.echo("ℹSync status check (not implemented yet)")
        # optional: show last sync time, # of local cards, etc.

    else:
        typer.secho("Unknown command. Try: check | pull | status", fg=typer.colors.RED)

if __name__ == "__main__":
    typer.run(main)
