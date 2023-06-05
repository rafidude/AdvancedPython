class ManagedResource:
    def __enter__(self):
        print("setting up resource.")
        return "RESOURCE"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Cleaning up resource.")


with ManagedResource() as resource:
    print(resource)
