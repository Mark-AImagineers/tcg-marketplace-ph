import typer
from typing_extensions import Annotated
from app.sync.checker import get_missing_card_ids
from app.sync.puller import pull_cards_by_ids

def main(
    command: Annotated[str, typer.Argument(help="Commands: check, pull, status")],
    api_key: Annotated[str, typer.Option(help="PokéTCG.io API key")] = ""
):
    # ========== CHECK ==========
    if command == "check":
        if not api_key:
            typer.secho("❌ Missing API key. Use --api-key=...", fg=typer.colors.RED)
            raise typer.Exit(code=1)

        typer.echo("🔍 Running sync check...")
        try:
            missing = get_missing_card_ids(api_key)
        except Exception as e:
            typer.secho(f"❌ Error: {str(e)}", fg=typer.colors.RED)
            raise typer.Exit(code=1)

        if missing:
            typer.secho(f"🟡 {len(missing)} cards missing from local DB", fg=typer.colors.YELLOW)
            typer.echo("Examples:")
            for card_id in list(missing)[:5]:
                typer.echo(f" - {card_id}")
        else:
            typer.secho("🟢 Your local card DB is fully up to date!", fg=typer.colors.GREEN)

    # ========== PULL ==========
    elif command == "pull":
        if not api_key:
            typer.secho("❌ Missing API key. Use --api-key=...", fg=typer.colors.RED)
            raise typer.Exit(code=1)

        typer.echo("🚀 Pulling cards listed in missing_ids.json...")
        try:
            inserted_ids = pull_cards_by_ids(api_key)
        except Exception as e:
            typer.secho(f"❌ Pull failed: {str(e)}", fg=typer.colors.RED)
            raise typer.Exit(code=1)

        if inserted_ids:
            typer.secho(f"✅ Pulled {len(inserted_ids)} new cards into your DB", fg=typer.colors.GREEN)
            typer.echo("Examples:")
            for card_id in inserted_ids[:5]:
                typer.echo(f" - {card_id}")
        else:
            typer.secho("ℹ No cards pulled — either all were already in DB or none to pull.", fg=typer.colors.YELLOW)

    # ========== STATUS ==========
    elif command == "status":
        typer.echo("ℹ Sync status check (not implemented yet)")

    else:
        typer.secho("❌ Unknown command. Try: check | pull | status", fg=typer.colors.RED)


if __name__ == "__main__":
    typer.run(main)
