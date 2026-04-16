from data_package import remove_duplicates
from data_package import strip_whitespaces
from data_package import calculate_mean
from data_package import find_maximum
from data_package import find_minimum


user_input = input("Enter a comma-separated list of numbers: ")

string_list = user_input.split(",")

cleaned_strings = strip_whitespaces(string_list)

number_list = []
for item in cleaned_strings:
    number_list.append(float(item))

unique_numbers = remove_duplicates(number_list)

mean_value = calculate_mean(unique_numbers)
max_value = find_maximum(unique_numbers)
min_value = find_minimum(unique_numbers)

print("Cleaned and unique data:", unique_numbers)
print("_________________")
print("Mean:", mean_value)
print("Maximum:", max_value)
print("Minimum:", min_value)