#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

long long convertToDecimal(char *str) {
    // Check if the number is negative
    int negative = 0;
    if (str[0] == '-') {
        negative = 1;
        str++; // Move past the '-' character
    }

    long long result = 0;

    // Determine the base of the number
    int base = 10;
    if (str[0] == '0') {
        if (tolower(str[1]) == 'x') {
            base = 16; // Hexadecimal
            str += 2; // Move past "0x"
        } else {
            base = 8; // Octal
            str++; // Move past '0'
        }
    }

    // Convert the string to decimal
    while (*str) {
        char c = *str++;
        int digit;
        if (isdigit(c)) {
            digit = c - '0';
        } else if (base == 16 && isxdigit(c)) {
            digit = tolower(c) - 'a' + 10;
        } else {
            printf("Invalid input!\n");
            exit(EXIT_FAILURE);
        }
        result = result * base + digit;
    }

    return (negative ? -result : result);
}

int main() {
    char str[100];
    printf("Enter an integer constant as a string: ");
    scanf("%s", str);

    long long decimalNumber = convertToDecimal(str);
    printf("Decimal representation: %lld\n", decimalNumber);

    return 0;
}
