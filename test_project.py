# test_project.py
from project import add_task, mark_task_complete, view_all_tasks, delete_task

def test_add_task():
    add_task("Task 1")
    assert len(tasks) == 1

def test_mark_task_complete():
    add_task("Task 2")
    mark_task_complete(0)
    assert tasks[0]["completed"] == True

def test_view_all_tasks():
    add_task("Task 3")
    add_task("Task 4")
    view_all_tasks()
    assert len(tasks) == 2

def test_delete_task():
    add_task("Task 5")
    delete_task(0)
    assert len(tasks) == 0
