import pytest
from data_structures.linked_list import LinkedList


def test_exists():
    assert LinkedList


def test_instantiate():
    assert LinkedList()


def test_empty_head():
    linked = LinkedList()
    assert linked.head is None


def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"


def test_head_inserted_into_populated_list():
    linked = LinkedList()
    linked.insert("apple")
    linked.insert("banana")
    assert linked.head.value == "banana"


def test_head_next_inserted_into_populated_list():
    linked = LinkedList()
    linked.insert("apple")
    linked.insert("banana")
    assert linked.head.next.value == "apple"
    assert linked.head.next.next is None


def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "NULL"


def test_to_string_single():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"


def test_to_string_double():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"

    linked_list.insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> NULL"


def test_includes_true():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple") is True


def test_includes_false():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert not linked_list.includes("cucumber")
