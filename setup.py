import os
import inspect

DIRECTORY_NAME = "inputs"
FILE_BASE= "input"
FILE_EXTENTION = "txt"

def get_input_file_path():
	frame = inspect.stack()[1]
	module = inspect.getmodule(frame[0])
	filename = os.path.basename(module.__file__)
	day_number = filename.strip("adpy")
	input_file_name = DIRECTORY_NAME + "/" + FILE_BASE + day_number + FILE_EXTENTION
	return input_file_name

# def run_all():
# 	dir_list = os.listdir(os.getcwd())
# 	dir_list.sort()
# 	for f in dir_list:
# 		if "day" in f:
# 			print(f)


# def main():
# 	run_all()

# if __name__ == "__main__":
#     main()