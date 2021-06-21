from selenium import webdriver
import pytest




def inc(x):
    return x + 1


def test_answera():
    assert inc(5) == 4

