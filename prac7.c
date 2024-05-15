#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX_STACK_SIZE 100

// Stack structure
struct Stack {
    int top;
    int items[MAX_STACK_SIZE];
};

// Function to initialize the stack
void initialize(struct Stack *s) {
    s->top = -1;
}

// Function to check if the stack is full
int isFull(struct Stack *s) {
    return s->top == MAX_STACK_SIZE - 1;
}

// Function to check if the stack is empty
int isEmpty(struct Stack *s) {
    return s->top == -1;
}

// Function to push an element onto the stack
void push(struct Stack *s, int value) {
    if (!isFull(s)) {
        s->items[++(s->top)] = value;
    } else {
        printf("Stack Overflow\n");
        exit(EXIT_FAILURE);
    }
}

// Function to pop an element from the stack
int pop(struct Stack *s) {
    if (!isEmpty(s)) {
        return s->items[(s->top)--];
    } else {
        printf("Stack Underflow\n");
        exit(EXIT_FAILURE);
    }
}

// Function to evaluate a postfix expression
int evaluatePostfix(char *expr) {
    struct Stack stack;
    initialize(&stack);

    int i, operand1, operand2;
    for (i = 0; expr[i] != '\0'; ++i) {
        if (isdigit(expr[i])) {
            push(&stack, expr[i] - '0'); // Convert character to integer
        } else {
            operand2 = pop(&stack);
            operand1 = pop(&stack);
            switch (expr[i]) {
                case '+':
                    push(&stack, operand1 + operand2);
                    break;
                case '-':
                    push(&stack, operand1 - operand2);
                    break;
                case '*':
                    push(&stack, operand1 * operand2);
                    break;
                case '/':
                    push(&stack, operand1 / operand2);
                    break;
                default:
                    printf("Invalid operator\n");
                    exit(EXIT_FAILURE);
            }
        }
    }
    return pop(&stack);
}

int main() {
    char postfixExpression[100];
    printf("Enter a postfix expression: ");
    scanf("%s", postfixExpression);

    int result = evaluatePostfix(postfixExpression);
    printf("Result: %d\n", result);

    return 0;
}
