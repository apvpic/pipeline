# noinspection PyUnresolvedReferences
import pipeline


def execute():
    print("two")


def execute_one():
    print("execute code from plugin one:")
    pipeline.one.test.execute()
