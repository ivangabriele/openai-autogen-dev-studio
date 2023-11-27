import utils


def test_mask_secret():
    assert utils.mask_secret("abcdef") == "******"
    assert utils.mask_secret("1234567890") == "123****890"
    assert utils.mask_secret(None) is None
    assert utils.mask_secret("a") == "*"
