import unittest
import pytest

import sys

from unittest import mock

from inhoj.prints import info
from inhoj.prints import trace
from inhoj.prints import err
from inhoj.prints import warn


class TestPrints(unittest.TestCase):

    def test_info(self):
        with mock.patch('sys.stdout') as mock_print:
            info("The process chain completed successfully")
            mock_print.assert_has_calls(
                [
                    mock.call.write('\033[94mThe process chain completed successfully\033[0m'),
                    mock.call.write('\n')
                ]
            )

    def test_trace(self):
        with mock.patch('sys.stdout') as mock_print:
            trace("Processing data folder")
            mock_print.assert_has_calls(
                [
                    mock.call.write('\033[92mProcessing data folder\033[0m'),
                    mock.call.write('\n')
                ]
            )

    def test_err(self):
        with mock.patch('sys.stdout') as mock_print:
            warn("The OFFER field was deprecated")
            mock_print.assert_has_calls(
                [
                    mock.call.write('\033[93mThe OFFER field was deprecated\033[0m'),
                    mock.call.write('\n')
                ]
            )

    def test_warn(self):
        with mock.patch('sys.stdout') as mock_print:
            err("The process was interrupted")
            mock_print.assert_has_calls(
                [
                    mock.call.write('\033[91mThe process was interrupted\033[0m'),
                    mock.call.write('\n')
                ]
            )
