from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    fruits: list[str] = ["apple", "orange", "banana", "watermelon"]
    assert get_first(fruits) == "apple"
