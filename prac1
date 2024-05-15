#include <stdio.h>
#include <string.h>

int isValidString(char *str) {
    int len = strlen(str);
    if (len < 3) // The minimum length required for a valid string is 3
        return 0;

    // Check if the string ends with "abb"
    if (str[len - 1] != 'b' || str[len - 2] != 'b' || str[len - 3] != 'a')
        return 0;

    // Check if all characters are either 'a' or 'b'
    for (int i = 0; i < len - 3; i++) {
        if (str[i] != 'a' && str[i] != 'b')
            return 0;
    }

    return 1;
}

int main() {
    char str[100];
    printf("Enter a string: ");
    scanf("%s", str);

    if (isValidString(str)) {
        printf("Valid string according to (a|b)*abb\n");
    } else {
        printf("Invalid string\n");
    }

    return 0;
}
