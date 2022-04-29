#!usr/bin/env python3
"""
Author:         David Meijer
Description:    Create a clamshell plot of your counts data.
Usage:          Run './clamshell_plot.py -h' for help.
"""
import typing as ty 
import argparse


def cli () -> argparse.Namespace:
    """
    Create command line interface for script.
    
    Returns
    -------
    argparse.Namespace: parsed command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Create a clamshell plot of your counts data."
    )
    parser.add_argument("-i", "--input", required=True,
        help="Input file containing a list of items to count and visualize."
    )
    return parser.parse_args()


def main() -> None:
    """
    Driver code.
    """
    args = cli()


if __name__ == "__main__":
    main()
    