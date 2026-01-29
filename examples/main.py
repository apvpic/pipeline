import os
import sys

DIR_EXAMPLES = os.path.dirname(__file__)
DIR_SOURCE = os.path.join(os.path.dirname(DIR_EXAMPLES), "src")

# plugins to load;
# every package collected from all 'src' folders must have unique name,
# any package will be accessible by 'pipeline.<package_name>'
os.environ["PIPELINE_PLUGIN_PATH"] = ";".join(
    os.path.join(DIR_EXAMPLES, item, "src") for item in os.listdir(DIR_EXAMPLES)
)
if DIR_SOURCE not in sys.path:
    sys.path.append(DIR_SOURCE)

if __name__ == "__main__":
    # noinspection PyUnresolvedReferences
    import pipeline

    print("example one")
    # simple call
    pipeline.one.test.execute()
    # call function that executes code from another plugin
    pipeline.one.test.execute_two()

    print("\nexample two")
    # simple call
    pipeline.two.test.execute()
    # call function that executes code from another plugin
    pipeline.two.test.execute_one()
