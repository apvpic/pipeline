def __init__():
    import os
    import sys
    import importlib.util

    this = sys.modules[__name__]

    pipeline_module_path = os.getenv("PIPELINE_PLUGIN_PATH")
    if pipeline_module_path:
        imported_plugins = []
        for root in pipeline_module_path.split(os.pathsep):
            # ignore leading/trailing spaces
            root = root.strip()
            if not root:
                continue
            root = os.path.normpath(root)
            if not os.path.exists(root):
                continue
            # ignore duplicated module that was already imported
            if root in imported_plugins:
                continue
            for item in os.listdir(root):
                init_filepath = os.path.join(root, item, "__init__.py")
                if not os.path.exists(init_filepath):
                    continue
                package_name = item
                module = sys.modules.get(package_name)
                if module:
                    raise RuntimeError(
                        "Failed to import {!r}. The same named package {!r} was already imported from {!r}. ".format(
                            init_filepath, package_name, module.__file__
                        )
                    )
                # create package dynamically and set it to this module
                spec = importlib.util.spec_from_file_location(package_name, init_filepath)
                module = importlib.util.module_from_spec(spec)
                sys.modules[package_name] = module
                spec.loader.exec_module(module)
                setattr(this, package_name, module)
            imported_plugins.append(root)

    # noinspection PyUnresolvedReferences,PyProtectedMember
    # remove reference to current function from the module
    delattr(this, sys._getframe(0).f_code.co_name)


__init__()
