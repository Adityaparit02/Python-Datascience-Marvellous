# ======================================================================
# Rich Dashboard for Decision Tree Classification
# Original ML File: 50_DecisionTree.py
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
# Execute Original Decision Tree Program
# ======================================================================

result = subprocess.run(
    [sys.executable, "50_DecisionTree.py"],
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
# Calculate Decision Tree Details
# ======================================================================
#
# We cannot directly access the trained Model because the original
# program is executed as a separate process.
#
# Therefore, we extract the basic model information from the dataset
# independently for display purposes.
#
# ======================================================================

try:

    import pandas as pd
    import numpy as np

    from sklearn.tree import DecisionTreeClassifier

    from sklearn.model_selection import train_test_split


    # --------------------------------------------------------------
    # Load Dataset
    # --------------------------------------------------------------

    df = pd.read_csv("breast-cancer-wisconsin.csv")

    df.replace("?", np.nan, inplace=True)

    df["BareNuclei"] = pd.to_numeric(
        df["BareNuclei"],
        errors="coerce"
    )

    df["BareNuclei"] = df["BareNuclei"].fillna(
        df["BareNuclei"].median()
    )

    df.drop_duplicates(inplace=True)


    # --------------------------------------------------------------
    # Prepare Data
    # --------------------------------------------------------------

    X = df.drop(columns=["CancerType"])

    Y = df["CancerType"]


    # --------------------------------------------------------------
    # Train Decision Tree
    # --------------------------------------------------------------

    X_Train, X_test, Y_Train, Y_Test = train_test_split(
        X,
        Y,
        train_size=0.7,
        random_state=42,
        stratify=Y
    )

    TreeModel = DecisionTreeClassifier(
        random_state=42
    )

    TreeModel.fit(
        X_Train,
        Y_Train
    )


    # --------------------------------------------------------------
    # Extract Tree Information
    # --------------------------------------------------------------

    node_count = TreeModel.tree_.node_count

    max_depth = TreeModel.tree_.max_depth

    leaf_count = TreeModel.get_n_leaves()

    feature_count = X.shape[1]

    training_samples = X_Train.shape[0]

    testing_samples = X_test.shape[0]


except Exception:

    node_count = "N/A"
    max_depth = "N/A"
    leaf_count = "N/A"
    feature_count = "N/A"
    training_samples = "N/A"
    testing_samples = "N/A"


# ======================================================================
# HEADER
# ======================================================================

console.print()

console.print(
    Panel(
        Text(
            "DECISION TREE CLASSIFICATION",
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
    "[bold green]Decision Tree Classifier[/bold green]"
)

model_table.add_row(
    "Number of Trees",
    "[bold yellow]1[/bold yellow]"
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
# DECISION TREE DETAILS
# ======================================================================

tree_table = Table(
    title="[bold yellow]DECISION TREE DETAILS[/bold yellow]",
    box=box.ROUNDED,
    border_style="yellow",
    show_header=True
)

tree_table.add_column(
    "Property",
    style="bold cyan"
)

tree_table.add_column(
    "Value",
    justify="center",
    style="bold yellow"
)

tree_table.add_row(
    "Number of Trees",
    "1"
)

tree_table.add_row(
    "Total Nodes",
    str(node_count)
)

tree_table.add_row(
    "Maximum Depth",
    str(max_depth)
)

tree_table.add_row(
    "Leaf Nodes",
    str(leaf_count)
)

tree_table.add_row(
    "Features Used",
    str(feature_count)
)

tree_table.add_row(
    "Training Samples",
    str(training_samples)
)

tree_table.add_row(
    "Testing Samples",
    str(testing_samples)
)

console.print(tree_table)

console.print()


# ======================================================================
# EXPERIMENT SUMMARY
# ======================================================================

console.print(
    Panel(
        Text.from_markup(
            "[bold green]Decision Tree Training Completed Successfully[/bold green]\n\n"
            "[white]The model was trained using a single Decision Tree "
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