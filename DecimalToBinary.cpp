#include <iostream>
#include <stack>
#include <string>

std::string decimalToBinary(int num) {
    if (num == 0) return "0";

    std::stack<int> remainders;
    while (num > 0) {
        remainders.push(num % 2);
        num /= 2;
    }

    std::string binary = "";
    while (!remainders.empty()) {
        binary += std::to_string(remainders.top());
        remainders.pop();
    }

    return binary;
}

int main() {
    int num;
    std::cout << "Enter a positive decimal number: ";
    std::cin >> num;

    if (num < 0) {
        std::cout << "Please enter a positive number.\n";
    } else {
        std::string binary = decimalToBinary(num);
        std::cout << "The binary equivalent of " << num << " is " << binary << ".\n";
    }

    return 0;
}
