def reverse_string_loop(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

my_string = "hello"
reversed_string = reverse_string_loop(my_string)
print(reversed_string)