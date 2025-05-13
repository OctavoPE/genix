import click
from rich.console import Console
from .resolver import resolve_command

console = Console()


@click.group(invoke_without_command=True)
@click.argument("query", required=False)
def main(query):
    """Genix: AI-powered command-line interpreter."""
    if query:
        try:
            command = resolve_command(query)
            console.print(f"[bold green]Genix suggests:[/bold green] {command}")
            if click.confirm("Execute?"):
                from .shell import execute_command

                execute_command(command)
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {str(e)}")
    else:
        click.echo("Please provide a query, e.g., 'genix set up new repo'")
