"""
Unit and regression test for the maxsmi package.
"""

# Import package, test suite, and other packages as needed
# import maxsmi
import pytest
import sys
import torch
from maxsmi.utils_evaluation import evaluation_results


def test_maxsmi_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "maxsmi" in sys.modules


####################
@pytest.mark.parametrize(
    "pred_output, true_output, solution",
    [(torch.zeros(2), torch.zeros(2), (0, 0, 1))],
)
def test_evaluation_results(pred_output, true_output, solution):
    results = evaluation_results(true_output, pred_output)
    assert solution == results
