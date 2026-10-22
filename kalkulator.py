"""Preprost kalkulator za demonstracijo nadzora različic."""
from __future__ import annotations
import argparse


def izracunaj(a: float, operator: str, b: float) -> float:
    """Izvede osnovno aritmetično operacijo."""
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ValueError("Deljenje z ničlo ni dovoljeno.")
        return a / b
    raise ValueError(f"Nepodprt operator: {operator}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Mini kalkulator")
    parser.add_argument("a", type=float)
    parser.add_argument("operator", choices=["+", "-", "*", "/"])
    parser.add_argument("b", type=float)
    args = parser.parse_args()
    try:
        rezultat = izracunaj(args.a, args.operator, args.b)
    except ValueError as exc:
        parser.error(str(exc))
    print(rezultat)


if __name__ == "__main__":
    main()


def zaokrozi(rezultat: float, mesta: int = 2) -> float:
    """Zaokroži rezultat na izbrano število decimalnih mest."""
    return round(rezultat, mesta)
