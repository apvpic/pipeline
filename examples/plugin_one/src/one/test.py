# noinspection PyUnresolvedReferences
import pipeline


def execute():
    print("one")


def execute_two():
    print("execute code from plugin two:")
    pipeline.two.test.execute()
