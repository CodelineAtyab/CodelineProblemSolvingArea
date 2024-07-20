#include <iostream>
#include <regex>
#include <string>

bool validateUsername(const std::string& username) {
    return !username.empty() && username.size() <= 50;
}

bool validatePassword(const std::string& password) {
    if (password.size() < 8) return false;

    bool hasSpecial = false, hasDigit = false, hasUpper = false, hasLower = false;
    for (char ch : password) {
        if (std::ispunct(ch)) hasSpecial = true;
        if (std::isdigit(ch)) hasDigit = true;
        if (std::isupper(ch)) hasUpper = true;
        if (std::islower(ch)) hasLower = true;
    }

    return hasSpecial && hasDigit && hasUpper && hasLower;
}

bool validateEmail(const std::string& email) {
    const std::regex emailPattern(R"(^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)");
    return std::regex_match(email, emailPattern);
}

int main() {
    std::string username, password, email;

    std::cout << "Enter username: ";
    std::getline(std::cin, username);

    std::cout << "Enter password: ";
    std::getline(std::cin, password);

    std::cout << "Enter email: ";
    std::getline(std::cin, email);

    // Validate and display results
    if (validateUsername(username)) {
        std::cout << "Username is valid.\n";
    } else {
        std::cout << "Username is invalid.\n";//It must not be empty and must not exceed 50 characters.
    }

    if (validatePassword(password)) {
        std::cout << "Password is valid.\n";
    } else {
        std::cout << "Password is invalid.\n";
    }

    if (validateEmail(email)) {
        std::cout << "Email is valid.\n";
    } else {
        std::cout << "Email is invalid.\n";
    }

    return 0;
}
