#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers;
    std::vector<int> squaresOfEvens;
    std::vector<int> sublist;
    int num, startIndex, endIndex, listSize;

    // Input the list of integers
    std::cout << "Enter the number of integers in the list: ";
    std::cin >> listSize;
    
    std::cout << "Enter the integers: ";
    for (int i = 0; i < listSize; ++i) {
        std::cin >> num;
        numbers.push_back(num);
    }

    // Create a new list of squares of even numbers
    for (int n : numbers) {
        if (n % 2 == 0) {
            squaresOfEvens.push_back(n * n);
        }
    }

    // Output the list of squares of even numbers
    std::cout << "List of squares of even numbers: {";
    for (size_t i = 0; i < squaresOfEvens.size(); ++i) {
        std::cout << squaresOfEvens[i];
        if (i != squaresOfEvens.size() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "}\n";

    // Input the start and end index for sublist
    std::cout << "Enter the start index: ";
    std::cin >> startIndex;
    std::cout << "Enter the end index: ";
    std::cin >> endIndex;

    // Extract sublist from start index to end index
    if (startIndex >= 0 && endIndex < listSize && startIndex <= endIndex) {
        for (int i = startIndex; i <= endIndex; ++i) {
            sublist.push_back(numbers[i]);
        }
    } else {
        std::cout << "Invalid indices.\n";
        return 1;
    }

    // Output the sublist
    std::cout << "Sublist: {";
    for (size_t i = 0; i < sublist.size(); ++i) {
        std::cout << sublist[i];
        if (i != sublist.size() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "}\n";

    return 0;
}
