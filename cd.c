#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function prototypes
int isIdentifier(char* token);
int isConstant(char* token);
int isKeyword(char* token);

// Enumeration of token types
typedef enum {
    TOKEN_UNKNOWN,
    TOKEN_IDENTIFIER,
    TOKEN_CONSTANT,
    TOKEN_KEYWORD
} TokenType;

// Structure to hold the token type and the actual token
typedef struct {
    TokenType type;
    char* value;
} Token;

// Function to determine token type and value
Token getToken(char* token) {
    Token result;
    result.value = token;

    if (isIdentifier(token)) {
        result.type = TOKEN_IDENTIFIER;
    } else if (isConstant(token)) {
        result.type = TOKEN_CONSTANT;
    } else if (isKeyword(token)) {
        result.type = TOKEN_KEYWORD;
    } else {
        result.type = TOKEN_UNKNOWN;
    }

    return result;
}

// Main function
int main() {
    char input[100];
    printf("Enter a token: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = 0; // Remove newline character

    Token token = getToken(input);

    // Print the result
    switch (token.type) {
        case TOKEN_IDENTIFIER:
            printf("<identifier, %s>\n", token.value);
            break;
        case TOKEN_CONSTANT:
            printf("<constant, %s>\n", token.value);
            break;
        case TOKEN_KEYWORD:
            printf("<keyword, %s>\n", token.value);
            break;
        default:
            printf("<unknown, %s>\n", token.value);
            break;
    }

    return 0;
}

// Implementations of isIdentifier, isConstant, isKeyword from the provided code
// ...
