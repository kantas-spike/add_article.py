from add_article import get_last_prefix_no


def test_get_last_prefix_no():
    last_no = get_last_prefix_no("./test/sample_contents")
    assert last_no == 6
