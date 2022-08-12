args = sys.argv

first_value = int(args[1])
second_value = int(args[2])
third_value = int(args[3])
fourth_value = int(args[4])
result = first_value + second_value + third_value + fourth_value
# further code of the script "add_four_numbers.py"
if len(args) == 5:
    print(result)
