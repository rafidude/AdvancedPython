import contextlib


@contextlib.contextmanager
def managed_resource():
    resource = "RESOURCE contextlib"
    try:
        print("setting up contextlib resource")
        yield resource
    finally:
        print("Cleaning up contextlib resource")


with managed_resource() as resource:
    print(resource)
