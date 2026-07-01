import argparse
import sys
from pathlib import Path

from . import rules
from .rules import get_brief
from .rules import get_code
from .rules import RegisteredRule
from .validator import Validator


def pad_string(text: str, span: tuple[int, int], size: int) -> tuple[str, int]:
    left_str = text[max(0, span[0] - size) : span[0]]
    right_str = text[span[1] : min(len(text), span[1] + size)]

    text_format = "{0}{1}{2}"

    if len(left_str) == size:
        text_format = "..." + text_format

    if len(right_str) == size:
        text_format += "..."

    padded_str = text_format.format(left_str, text[span[0] : span[1]], right_str)
    start_index = len(left_str) + (3 if len(left_str) == size else 0)

    return padded_str, start_index


def write_output(text: str) -> None:
    sys.stdout.write(text)


def iter_tex_paths(path: Path) -> list[Path]:
    if path.is_dir():
        return sorted(path.rglob("*.tex"))
    return [path]


def normalise_rule_code(raw_code: str) -> str:
    code = raw_code.strip().upper()
    code_number = code.removeprefix("DC")
    if not code_number.isdecimal():
        msg = f"Invalid rule code: {raw_code}"
        raise ValueError(msg)
    return f"DC{int(code_number):03d}"


def parse_rule_codes(raw_codes: str) -> set[str]:
    codes = {normalise_rule_code(raw_code) for raw_code in raw_codes.split(",")}
    if not codes:
        msg = "At least one rule code is required."
        raise ValueError(msg)
    return codes


def select_rules(
    selected_codes: set[str] | None,
    ignored_codes: set[str] | None,
    available_rules: list[RegisteredRule],
) -> list[RegisteredRule]:
    available_codes = {get_code(rule) for rule in available_rules}
    requested_codes = selected_codes if selected_codes is not None else ignored_codes
    if requested_codes is not None:
        unknown_codes = sorted(requested_codes - available_codes)
        if unknown_codes:
            msg = f"Unknown rule code(s): {', '.join(unknown_codes)}"
            raise ValueError(msg)

    if selected_codes is not None:
        return [rule for rule in available_rules if get_code(rule) in selected_codes]
    if ignored_codes is not None:
        return [rule for rule in available_rules if get_code(rule) not in ignored_codes]
    return available_rules


def print_warning(
    fname: Path,
    lineno: int,
    line: str,
    span: tuple[int, int],
    rule: RegisteredRule,
) -> None:
    location = f"{fname}:{lineno}:{span[0]}:"
    write_output(f"{location} {get_brief(rule)}\n")

    padded_str, start_index = pad_string(line, span, 10)
    snippet = padded_str.replace(" ", "_") if rule.show_spaces else padded_str

    write_output(f"  {snippet}\n")
    write_output(f"  {' ' * start_index}{'^' * (span[1] - span[0])}\n")
    if rule.proposal is not None:
        write_output(f"  help: {rule.proposal}\n")
    write_output("\n")


def main() -> int:

    parser = argparse.ArgumentParser(
        description="Check for common mistakes in LaTeX documents."
    )

    parser.add_argument(
        "paths",
        nargs="+",
        help="List of .tex files or directories to check",
    )
    rule_group = parser.add_mutually_exclusive_group()
    rule_group.add_argument(
        "--select",
        help="Comma-separated rule codes to enable, such as DC021,DC063",
    )
    rule_group.add_argument(
        "--ignore",
        help="Comma-separated rule codes to disable, such as DC021,DC063",
    )

    args = parser.parse_args()
    try:
        selected_codes = (
            parse_rule_codes(args.select) if args.select is not None else None
        )
        ignored_codes = (
            parse_rule_codes(args.ignore) if args.ignore is not None else None
        )
        rules_to_apply = select_rules(
            selected_codes, ignored_codes, list(rules.RULES_LIST)
        )
    except ValueError as error:
        parser.error(str(error))

    # Count the total number of errors
    num_errors = 0

    for raw_path in args.paths:
        for path in iter_tex_paths(Path(raw_path)):
            with path.open(encoding="utf-8") as infile:
                validator = Validator(rules_to_apply)
                for lineno, line in enumerate(infile):
                    for rule, span in validator.validate(line):
                        print_warning(path, lineno, line.strip(), span, rule)
                        num_errors += 1

    if num_errors > 0:
        write_output(f"\nTotal of {num_errors} mistakes found.\n")
        return 1
    write_output("No mistakes found.\n")
    return 0
