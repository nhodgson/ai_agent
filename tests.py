from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_files import write_file
from functions.run_python_file import run_python_file

# print(get_files_info("calculator", "."))
# print(get_files_info("calculator", "pkg"))
# print(get_files_info("calculator", "/bin"))
# print(get_files_info("calculator", "../"))

# result = get_file_content("calculator", "lorem.txt")
# print(result)

# print('Test main.py')
# result = get_file_content("calculator", "main.py")
# print(result)

# print('Test calculator.py')
# result = get_file_content("calculator", "pkg/calculator.py")
# print(result)

# print('Test for outside working directory')
# result = get_file_content("calculator", "/bin/cat") 
# print(result)

# print('Test for non existant file')
# result = get_file_content("calculator", "pkg/does_not_exist.py")
# print(result)

# print('Test lorem ipsum')
# result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
# print(result)

# print('Test create new file')
# result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
# print(result)

# print('Test outside working dir')
# result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
# print(result)


print('Usage instructions')
result = run_python_file("calculator", "main.py")
print(result)

print('Calculate 3 + 5')
result = run_python_file("calculator", "main.py", ["3 + 5"])
print(result)

print('Error')
result = run_python_file("calculator", "../main.py")
print(result)

print('Error')
result = run_python_file("calculator", "nonexistent.py")
print(result)

print('Error')
result = run_python_file("calculator", "lorem.txt")
print(result)