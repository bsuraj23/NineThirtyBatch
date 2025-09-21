def print_args_kwargs(*args, **kwargs):
    print("Arguments (args):")
    for arg in args:
        print(arg)
    
    print("\nKeyword Arguments (kwargs):")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# Example usage
print_args_kwargs(1, 2, 3, name="Prasad", age=25, country="India")
