#include <iostream>
#include <string>

int main() {
	std::string word;
	int word_length = 0;
	int middle_letter = 0;

	std::cout << "enter a word: ";
	std::cin >> word;
	std::cout << word << std::endl;

	word_length = word.length();
	middle_letter = (int)(word_length / 2);

	if (word_length % 2 == 1)
		std::cout << word.at(middle_letter) << std::endl;
	else
		std::cout << word.at(middle_letter - 1) << word.at(middle_letter) << std::endl;
	return 0;
}