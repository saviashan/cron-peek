"""
Cron Peek: A CLI tool to decode and display cron schedules in UTC and local time.
"""

import typer
from rich.console import Console
from rich.table import Table
from croniter import croniter
from datetime import datetime, timezone
from tzlocal import get_localzone
from typing_extensions import Annotated

app = typer.Typer(
    name="cron-peek",
    help="A CLI tool to decode and display cron schedules in UTC and local time.",
    add_completion=False,
)

console = Console()


def get_human_readable_cron(expression: str) -> str:
    """Provides a human-readable description of the cron expression."""
    try:
        # This is a simplified human-readable conversion.
        # For a full-blown one, a more complex library or logic would be needed.
        return f"Runs according to the schedule: '{expression}'"
    except Exception:
        return "Invalid cron expression"


@app.command(help="Display the next 5 run times for a given cron expression.")
def main(
    expression: Annotated[
        str,
        typer.Argument(
            help="The cron expression to analyze (e.g., '*/15 * * * *')."
        ),
    ]
):
    """
    Parses a cron expression and displays the next 5 scheduled run times in
    both UTC and the user's local timezone.
    """
    try:
        base_time = datetime.now(timezone.utc)
        if not croniter.is_valid(expression):
            console.print(
                f"[bold red]Error:[/] Invalid cron expression: '{expression}'"
            )
            raise typer.Exit(code=1)

        console.print(
            f"[bold green]Analysis for:[/] [yellow]'{expression}'[/]"
        )
        console.print(
            f"[cyan]Description:[/] {get_human_readable_cron(expression)}"
        )

        table = Table(
            title="Next 5 Scheduled Runs",
            caption="Times are based on the current system time.",
            show_header=True,
            header_style="bold magenta",
        )
        table.add_column("#", style="dim", width=3)
        table.add_column("UTC Time (Server Time)", justify="left")
        table.add_column("Local Time", justify="left")

        local_tz = get_localzone()
        cron = croniter(expression, base_time)

        for i in range(5):
            next_run_utc = cron.get_next(datetime)
            next_run_local = next_run_utc.astimezone(local_tz)
            table.add_row(
                str(i + 1),
                next_run_utc.strftime("%Y-%m-%d %H:%M:%S"),
                next_run_local.strftime("%Y-%m-%d %H:%M:%S (%Z)"),
            )

        console.print(table)

    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred:[/] {e}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
