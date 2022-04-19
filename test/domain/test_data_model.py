# -*- coding: utf-8 -*-
import pytest
import sys
from os import path

sys.path.insert(
    0, path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
)
from scripts.main import add


class TestSample:
    def test_data_socket_compare_same(self):
        assert add(1, 2) == 2

    def test_data_socket_compare_same2(self):
        status_code = 100
        assert 1 == 3, f"My custom msg: actual status code {status_code}"
