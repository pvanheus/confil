import os

import pytest

from confil.report import parse_report
from test_runner import TEST_DATA_DIR

TEST_REPORT = os.path.join(TEST_DATA_DIR, "test_file.tab")

# test using a cutoff of 50%


@pytest.mark.parametrize("test_input, expected", [
    (type(parse_report(TEST_REPORT, 50)), list),
    (parse_report(TEST_REPORT, 50)[5], 'Mycobacterium'),
    (parse_report(TEST_REPORT, 50)[0], '55.84')
])
def test_parse_report(test_input, expected):
    assert test_input == expected


def test_parse_report_exception():
    with pytest.raises(SystemExit):
        parse_report(TEST_REPORT, 90)
        parse_report(TEST_REPORT, 20)
