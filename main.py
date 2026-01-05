import typer
from rich.console import Console
from rich.table import Table
import httpx
import time

app = typer.Typer()
console = Console()

def check_url(url: str):
    """Checks a single URL and returns its status and response time."""
    try:
        with console.status(f"Checking {url}...", spinner="dots"):
            start_time = time.time()
            response = httpx.get(url, follow_redirects=True)
            end_time = time.time()
            response_time = end_time - start_time
            return response.status_code, response_time
    except httpx.RequestError as e:
        return str(e), None

@app.command()
def check(url: str):
    """Checks a single URL."""
    status_code, response_time = check_url(url)
    table = Table(title=f"Site Sentry Report for {url}")
    table.add_column("Status Code", justify="right", style="cyan", no_wrap=True)
    table.add_column("Response Time (s)", justify="right", style="magenta")

    if isinstance(status_code, int):
        table.add_row(str(status_code), f"{response_time:.2f}")
    else:
        table.add_row(f"[bold red]{status_code}[/bold red]", "[bold red]N/A[/bold red]")
    
    console.print(table)

@app.command()
def monitor(url: str, interval: int = 5):
    """Monitors a URL at a specified interval (in seconds)."""
    console.print(f"Monitoring {url} every {interval} seconds. Press Ctrl+C to stop.")
    try:
        while True:
            status_code, response_time = check_url(url)
            table = Table(title=f"Site Sentry Report for {url}")
            table.add_column("Status Code", justify="right", style="cyan", no_wrap=True)
            table.add_column("Response Time (s)", justify="right", style="magenta")

            if isinstance(status_code, int):
                table.add_row(str(status_code), f"{response_time:.2f}")
            else:
                table.add_row(f"[bold red]{status_code}[/bold red]", "[bold red]N/A[/bold red]")
            
            console.print(table)
            time.sleep(interval)
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Monitoring stopped.[/bold yellow]")

if __name__ == "__main__":
    app()
