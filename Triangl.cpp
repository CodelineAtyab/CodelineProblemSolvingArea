#include <iostream>

// Function to display a right-angle triangle of ones
void displayRightAngleTriangle(int lines) {
    for (int i = 1; i <= lines; ++i) {
        for (int j = 0; j < i; ++j) {
            std::cout << "1";
        }
        std::cout << "\n";
    }
}

// Function to display a palindromic triangle
void displayPalindromicTriangle(int lines) {
    for (int i = 1; i <= lines; ++i) {
        // Print leading spaces for alignment
        for (int j = i; j < lines; ++j) {
            std::cout << " ";
        }
        // Print increasing numbers
        for (int j = 1; j <= i; ++j) {
            std::cout << j;
        }
        // Print decreasing numbers
        for (int j = i - 1; j >= 1; --j) {
            std::cout << j;
        }
        std::cout << "\n";
    }
}

// Function to display help information
void displayHelp() {
    std::cout << "A palindromic triangle is a triangle array of numbers where each row forms a palindrome.\n";
    std::cout << "The first few lines are:\n";
    std::cout << "1\n";
    std::cout << "11\n";
    std::cout << "121\n";
    std::cout << "12321\n";
    std::cout << "1234321\n";
    std::cout << "You can use this pattern to draw a palindromic triangle of any number of lines.\n";
}

int main() {
    int choice;
    int lines;

    while (true) {
        // Display menu
        std::cout << "Menu\n";
        std::cout << "1. Enter a right angle triangle of ones\n";
        std::cout << "2. Display a palindromic triangle\n";
        std::cout << "3. Help\n";
        std::cout << "4. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                std::cout << "Enter number of lines: ";
                std::cin >> lines;
                displayRightAngleTriangle(lines);
                break;

            case 2:
                std::cout << "Enter number of lines: ";
                std::cin >> lines;
                displayPalindromicTriangle(lines);
                break;

            case 3:
                displayHelp();
                break;

            case 4:
                std::cout << "Exiting the program.\n";
                return 0;

            default:
                std::cout << "Invalid choice. Please try again.\n";
                break;
        }
    }
}
