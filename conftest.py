"""Configuration for pytest."""

import pytest


def pytest_addoption(parser):
    """Add command-line flags for pytest."""
    parser.addoption("--run-flaky", action="store_true", help="runs flaky tests")
    parser.addoption(
        "--run-network-tests",
        action="store_true",
        help="runs tests requiring a network connection",
    )


def pytest_runtest_setup(item):
    # based on https://stackoverflow.com/questions/47559524
    if "flaky" in item.keywords and not item.config.getoption("--run-flaky"):
        pytest.skip("set --run-flaky option to run flaky tests")
    if "network" in item.keywords and not item.config.getoption("--run-network-tests"):
        pytest.skip(
            "set --run-network-tests to run test requiring an " "internet connection"
        )
