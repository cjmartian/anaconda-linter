from anaconda_linter import lint
from conftest import check

import os


def test_lint_list():
    checks_file = os.path.abspath(os.path.dirname(__file__) + "/../anaconda_linter/lint_names.md")
    with open(checks_file) as f:
        lint_checks_file = [line.strip() for line in f.readlines() if line.strip()]
    lint_checks_lint = [str(check) for check in lint.get_checks()]
    assert sorted(lint_checks_file) == sorted(lint_checks_lint)
