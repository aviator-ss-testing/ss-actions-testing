from numbers import safe_div, clamp, round_to_sig_figs


def test_safe_div_basic():
    assert safe_div(10, 2) == 5
    assert safe_div(7, 0) is None


def test_clamp_within_range():
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(11, 0, 10) == 10


def test_round_to_sig_figs():
    assert round_to_sig_figs(1234, 2) == 1200
    assert round_to_sig_figs(0.0456, 2) == 0.046
    assert round_to_sig_figs(0, 3) == 0
