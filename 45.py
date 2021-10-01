#Ваша задача - написать функцию, которая преобразовывает текст из формата CamelCase, принятый в Python (my_function_name), где все буквы - маленькие, а слова соединены знаком нижнего подчеркивания "_".
import string

def from_camel_case(name: str) -> str:
	res = ''

	for char in name:
		if char in string.ascii_uppercase:
			res += '_' + char
		else:
			res += char

	return res.lower()[1:]

if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("MyFunctionName"))# == "my_function_name"
    print(from_camel_case("IPhone"))# == "i_phone"
    print(from_camel_case("ThisFunctionIsEmpty"))# == "this_function_is_empty"
    print(from_camel_case("Name"))# == "name"