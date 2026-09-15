def test_healthy_control():
    print("VM2_QPOLICY_HEALTHY_PASS")
    assert True


def test_branch_scoped_failure():
    print("VM2_QPOLICY_FAILURE_EXECUTED")
    assert False, "VM2 branch-scoped failure must be quarantined only on target A"
