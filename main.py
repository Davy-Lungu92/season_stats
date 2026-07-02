import argparse
from load_data import Data


# def main():
#     print("Hello from season-stats!")


# if __name__ == "__main__":
#     main()

from rich.console import Console
from rich.table import Table

# Initialize the console
console = Console()

# Create a basic table object
table = Table(title="Server Status Overview")

# Define the columns
table.add_column("Server ID", justify="center", style="cyan", no_wrap=True)
table.add_column("Location", style="magenta")
table.add_column("Uptime", justify="right", style="green")

# Add the rows of data
table.add_row("SRV-01", "New York", "99.9%")
table.add_row("SRV-02", "London", "98.5%")
table.add_row("SRV-03", "Tokyo", "99.2%")

# Print the table to the terminal
console.print(table)