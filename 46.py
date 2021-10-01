#Ваша задача - написать функцию, которая преобразовывает текст из формата, принятого в Python (my_function_name) в CamelCase, где первая буква каждого слова - большая/заглавная.

def to_camel_case(name: str) -> str:
	res = ''
	name = name.split('_')

	for word in name:
		res += word.capitalize()

	return res

if __name__ == '__main__':
    print("Example:")
    print(to_camel_case("my_function_name"))# == "MyFunctionName"
    print(to_camel_case("i_phone"))# == "IPhone"
    print(to_camel_case("this_function_is_empty"))# == "ThisFunctionIsEmpty"
    print(to_camel_case("name"))# == "Name"