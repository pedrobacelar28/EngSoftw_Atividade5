from __future__ import annotations

import argparse


def add(left: float, right: float) -> float:
    return left + right


def subtract(left: float, right: float) -> float:
    return left - right


def multiply(left: float, right: float) -> float:
    return left * right


def divide(left: float, right: float) -> float:
    if right == 0:
        raise ZeroDivisionError("cannot divide by zero")

    return left / right


def power(left: float, right: float) -> float:
    return left**right


def calculate(operation: str, left: float, right: float) -> float:
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
        "power": power,
    }

    try:
        return operations[operation](left, right)
    except KeyError as exc:
        valid_operations = ", ".join(sorted(operations))
        raise ValueError(f"unknown operation: {operation}. Use one of: {valid_operations}") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Calculadora simples")
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide", "power"],
        help="operacao a ser executada",
    )
    parser.add_argument("left", type=float, help="primeiro numero")
    parser.add_argument("right", type=float, help="segundo numero")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    result = calculate(args.operation, args.left, args.right)
    print(result)


if __name__ == "__main__":
    main()
