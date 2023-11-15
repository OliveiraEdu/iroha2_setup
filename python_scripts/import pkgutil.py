import pkgutil
from icecream import ic

# Get a list of all installed modules
installed_modules = [name for _, name, _ in pkgutil.iter_modules()]

# Iterate through the modules and print their classes
for module_name in installed_modules:
    try:
        module = __import__(module_name)
        module_contents = dir(module)
        classes_in_module = [name for name in module_contents if isinstance(getattr(module, name), type)]
        if classes_in_module:
            ic(f"Classes in {module_name}: {classes_in_module}")
    except ImportError as e:
        ic(f"Error importing module {module_name}: {e}")
