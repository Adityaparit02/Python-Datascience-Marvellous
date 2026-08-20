# ======================================================================
# Rich Dashboard for Random Forest Classification
# Original ML File: 50_RandomForest.py
# ======================================================================

import subprocess
import sys
import re

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.text import Text
from rich import box


# ======================================================================
# Rich Console
# ======================================================================

console = Console()


# ======================================================================
# Execute Original Random Forest Program
# ======================================================================

result = subprocess.run(
    [sys.executable, "50_RandomForest.py"],
    capture_output=True,
    text=True
)

output = result.stdout


# ======================================================================
# Extract Model Metrics
# ======================================================================

accuracy = re.search(
    r"Accuracy of Model is\s*:\s*([0-9.]+)",
    output
)

precision = re.search(
    r"Precision Score of Model is\s*:\s*([0-9.]+)",
    output
)

recall = re.search(
    r"Recall Score of Model is\s*:\s*([0-9.]+)",
    output
)

f1 = re.search(
    r"F1 Score of Model is\s*:\s*([0-9.]+)",
    output
)

trees = re.search(
    r"Number of Trees\s*:\s*(\d+)",
    output
)


# ======================================================================
# Extract Confusion Matrix
# ======================================================================

confusion_match = re.search(
    r"confusion Matrix:\s*\[\[\s*(\d+)\s+(\d+)\s*\]\s*\[\s*(\d+)\s+(\d+)\s*\]\]",
    output,
    re.MULTILINE
)

if confusion_match:

    tn, fp, fn, tp = map(
        int,
        confusion_match.groups()
    )

else:

    tn = fp = fn = tp = 0


# ======================================================================
# Extract Tree Information
# ======================================================================

tree_data = []

tree_matches = re.findall(
    r"Tree\s+(\d+)\s+"
    r"Number of Nodes\s*:\s*(\d+)\s+"
    r"Maximum Depth\s*:\s*(\d+)",
    output
)

for tree_number, nodes, depth in tree_matches:

    tree_data.append(
        (
            int(tree_number),
            int(nodes),
            int(depth)
        )
    )


# ======================================================================
# HEADER
# ======================================================================

console.print()

console.print(
    Panel(
        Text(
            "RANDOM FOREST CLASSIFICATION",
            justify="center",
            style="bold bright_white"
        ),
        subtitle="[bold cyan]Breast Cancer Wisconsin Dataset[/bold cyan]",
        border_style="bright_blue",
        box=box.DOUBLE,
        padding=(1, 4)
    )
)

console.print()


# ======================================================================
# MODEL INFORMATION
# ======================================================================

model_table = Table(
    title="[bold bright_blue]MODEL INFORMATION[/bold bright_blue]",
    title_style="bold bright_blue",
    box=box.ROUNDED,
    border_style="bright_blue",
    show_header=True
)

model_table.add_column(
    "Property",
    style="bold cyan"
)

model_table.add_column(
    "Value",
    justify="center",
    style="bold white"
)

model_table.add_row(
    "Algorithm",
    "[bold green]Random Forest Classifier[/bold green]"
)

model_table.add_row(
    "Number of Trees",
    f"[bold yellow]{len(tree_data) if tree_data else trees.group(1) if trees else '100'}[/bold yellow]"
)

model_table.add_row(
    "Training Data",
    "[bold magenta]70%[/bold magenta]"
)

model_table.add_row(
    "Testing Data",
    "[bold magenta]30%[/bold magenta]"
)

model_table.add_row(
    "Random State",
    "[bold cyan]42[/bold cyan]"
)

console.print(model_table)

console.print()


# ======================================================================
# PERFORMANCE METRICS
# ======================================================================

metric_table = Table(
    title="[bold green]MODEL PERFORMANCE[/bold green]",
    box=box.HEAVY_HEAD,
    border_style="green",
    show_header=True
)

metric_table.add_column(
    "Metric",
    style="bold cyan"
)

metric_table.add_column(
    "Score",
    justify="center",
    style="bold green"
)

metric_table.add_row(
    "Accuracy",
    f"[bold green]{float(accuracy.group(1)):.2f}%[/bold green]"
    if accuracy else "[red]N/A[/red]"
)

metric_table.add_row(
    "Precision",
    f"[bold green]{float(precision.group(1)):.4f}[/bold green]"
    if precision else "[red]N/A[/red]"
)

metric_table.add_row(
    "Recall",
    f"[bold green]{float(recall.group(1)):.4f}[/bold green]"
    if recall else "[red]N/A[/red]"
)

metric_table.add_row(
    "F1 Score",
    f"[bold green]{float(f1.group(1)):.4f}[/bold green]"
    if f1 else "[red]N/A[/red]"
)


# ======================================================================
# CONFUSION MATRIX
# ======================================================================

matrix_table = Table(
    title="[bold cyan]CONFUSION MATRIX[/bold cyan]",
    box=box.SQUARE,
    border_style="cyan",
    show_header=True
)

matrix_table.add_column(
    "",
    style="bold white"
)

matrix_table.add_column(
    "Predicted Benign",
    justify="center",
    style="bold green"
)

matrix_table.add_column(
    "Predicted Malignant",
    justify="center",
    style="bold red"
)

matrix_table.add_row(
    "Actual Benign",
    f"[bold green]{tn}[/bold green]",
    f"[bold red]{fp}[/bold red]"
)

matrix_table.add_row(
    "Actual Malignant",
    f"[bold red]{fn}[/bold red]",
    f"[bold green]{tp}[/bold green]"
)


# ======================================================================
# Display Performance + Confusion Matrix
# ======================================================================

console.print(
    Columns(
        [
            metric_table,
            matrix_table
        ],
        equal=True,
        expand=True
    )
)

console.print()


# ======================================================================
# TREE STATISTICS
# ======================================================================

if tree_data:

    # --------------------------------------------------------------
    # Split Trees into Groups of 25
    # --------------------------------------------------------------

    tree_groups = [
        tree_data[i:i + 25]
        for i in range(0, len(tree_data), 25)
    ]


    # --------------------------------------------------------------
    # Create Tables
    # --------------------------------------------------------------

    tree_tables = []

    for group_index, group in enumerate(tree_groups):

        start_tree = group[0][0]
        end_tree = group[-1][0]

        tree_table = Table(
            title=f"[bold yellow]TREES {start_tree} - {end_tree}[/bold yellow]",
            box=box.ROUNDED,
            border_style="yellow",
            show_header=True,
            padding=(0, 1)
        )

        tree_table.add_column(
            "Tree",
            justify="center",
            style="bold cyan"
        )

        tree_table.add_column(
            "Nodes",
            justify="center",
            style="bold white"
        )

        tree_table.add_column(
            "Depth",
            justify="center",
            style="bold yellow"
        )

        for tree_number, nodes, depth in group:

            tree_table.add_row(
                str(tree_number),
                str(nodes),
                str(depth)
            )

        tree_tables.append(tree_table)


    # --------------------------------------------------------------
    # Display Two Tables Per Row
    # --------------------------------------------------------------

    console.print(
        Panel(
            Columns(
                tree_tables[:2],
                equal=True,
                expand=True
            ),
            title="[bold yellow]RANDOM FOREST TREE DETAILS[/bold yellow]",
            border_style="yellow",
            box=box.DOUBLE
        )
    )

    if len(tree_tables) > 2:

        console.print(
            Panel(
                Columns(
                    tree_tables[2:4],
                    equal=True,
                    expand=True
                ),
                border_style="yellow",
                box=box.DOUBLE
            )
        )

else:

    console.print(
        Panel(
            "[bold red]Tree information could not be extracted.[/bold red]",
            title="[bold red]TREE DETAILS[/bold red]",
            border_style="red",
            box=box.ROUNDED
        )
    )
    
# ======================================================================
# EXPERIMENT SUMMARY
# ======================================================================

console.print()

console.print(
    Panel(
        Text.from_markup(
            "[bold green]Random Forest Training Completed Successfully[/bold green]\n\n"
            "[white]The model was trained using multiple Decision Trees "
            "and evaluated on the test dataset.[/white]"
        ),
        title="[bold bright_magenta]EXPERIMENT SUMMARY[/bold bright_magenta]",
        border_style="bright_magenta",
        box=box.DOUBLE
    )
)

console.print()


# ======================================================================
# Error Handling
# ======================================================================

if result.returncode != 0:

    console.print(
        Panel(
            result.stderr,
            title="[bold red]PROGRAM ERROR[/bold red]",
            border_style="red",
            box=box.HEAVY
        )
    )