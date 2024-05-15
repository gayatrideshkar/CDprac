#include <stdio.h>
#include <ctype.h>

int isIdentifier(char *str) {
    // Check if the first character is a letter or underscore
    if (!isalpha(str[0]) && str[0] != '_')
        return 0;

    // Check if all characters are either letters, digits, or underscore
    for (int i = 1; str[i]; i++) {
        if (!isalnum(str[i]) && str[i] != '_')
            return 0;
    }

    return 1;
}

int isIntegerConstant(char *str) {
    // Check if the string starts with a valid digit or '-'
    if (!isdigit(str[0]) && str[0] != '-')
        return 0;

    // Check if the rest of the string contains only digits
    for (int i = 1; str[i]; i++) {
        if (!isdigit(str[i]))
            return 0;
    }

    return 1;
}

int isRealConstant(char *str) {
    // Check if the string starts with a valid digit or '-'
    if (!isdigit(str[0]) && str[0] != '-')
        return 0;

    int hasDot = 0;

    // Check if the rest of the string contains only digits or a single dot
    for (int i = 1; str[i]; i++) {
        if (str[i] == '.') {
            if (hasDot)
                return 0; // More than one dot found
            hasDot = 1;
        } else if (!isdigit(str[i])) {
            return 0;
        }
    }

    return 1;
}

int main() {
    char token[100];
    printf("Enter a token: ");
    scanf("%s", token);

    if (isIdentifier(token)) {
        printf("Identifier\n");
    } else if (isIntegerConstant(token)) {
        printf("Integer Constant\n");
    } else if (isRealConstant(token)) {
        printf("Real Constant\n");
    } else {
        printf("Unknown token\n");
    }

    return 0;
}
