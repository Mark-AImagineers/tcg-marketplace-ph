import typer
from typing_extensions import Annotated
from app.sync.checker import get_missing_card_ids

def main(
    command: Annotated[str, typer.Argument(help="Commands: check, pull, status")],
    api_key: Annotated[str, typer.Option(help="PokéTCG.io API key")] = ""
):
    
    ### CHECK ###
    if command == "check":
        if not api_key:
            typer.secho("Missing API key. Use --api-key=...", fg=typer.colors.RED)
            raise typer.Exit(code=1)
        
        typer.echo("Running sync check")
        missing = get_missing_card_ids(api_key)
        if missing:
            typer.echo(f"🟡 {len(missing)} cards missing from local DB")
            typer.echo("Examples:")
            for card_id in list(missing)[:5]:
                typer.echo(f" - {card_id}")
        else:
            typer.echo(f"🟢 Your local card DB is fully up to date!", fg=typer.colors.GREEN)

    ### PULL ###
    elif command == "pull":
        from app.sync.puller import pull_cards_by_ids

        if not api_key:
            typer.secho("❌ Missing API key. Use --api-key=...", fg=typer.colors.RED)
            raise typer.Exit(code=1)

        typer.echo("🚀 Running data puller")
        pull_cards_by_ids(api_key)
        typer.secho("✅ Done pulling cards (within safe rate limits)", fg=typer.colors.GREEN)

    elif command == "status":
        typer.echo("ℹSync status check (not implemented yet)")
        # optional: show last sync time, # of local cards, etc.

    else:
        typer.secho("Unknown command. Try: check | pull | status", fg=typer.colors.RED)

if __name__ == "__main__":
    typer.run(main)
