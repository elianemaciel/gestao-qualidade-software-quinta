from branches import branch_out


def test_branch_out_x_positive_y_positive():
    assert branch_out(2, 3) == (4, 6)


def test_branch_out_x_positive_y_zero():
    assert branch_out(2, 0) == (4, 0)


def test_branch_out_x_zero_y_positive():
    assert branch_out(0, 3) == (0, 3)


def test_branch_out_x_zero_y_zero():
    assert branch_out(0, 0) == (0, 0)
