import pytest
from todo_app.data.classes import to_do_item
from todo_app.data.viewmodel import ViewModel


def test_todo_items():
    items = [
        to_do_item(1, "new item", "To-Do"),
        to_do_item(2, "in progress item", "Doing"),
        to_do_item(3, "done item", "Done"),
    ]
    viewmodel = ViewModel(items)
    todo_items = viewmodel.todo_items
    assert len(todo_items) == 1
    assert todo_items[0].status == "To-Do"


# def test_doing_items():
#     items = [
#         to_do_item(1, "new item", "To-do"),
#         to_do_item(2, "in progress item", "Doing"),
#         to_do_item(3, "done item", "Done"),
#     ]
#     viewmodel = ViewModel(items)
#     doing_items = viewmodel.doing_items
#     assert len(doing_items) == 1
#     assert doing_items[0].status == "Doing"


# def test_done_items():
#     items = [
#         to_do_item(1, "new item", "To-do"),
#         to_do_item(2, "inprogress item", "Doing"),
#         to_do_item(3, "done item", "Done"),
#     ]
#     viewmodel = ViewModel(items)
#     done_items = viewmodel.done_items
#     assert len(done_items) == 1
#     assert done_items[0].status == "Done"