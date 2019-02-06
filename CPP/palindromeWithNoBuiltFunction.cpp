#include <iostream> 
int calculateLength(char *input){
    int i = 0;
    while (input[i]){
        i++;
    }
    return i;
}
// Program starts from here
int main(){
    char input[100]; //Getting Input from User upto 100 chars
    std::cout << "Please input the string/number [Note: Max 100 characters allowed]:";
    std::cin >> input;
    int length = calculateLength(input);
    int lastIndex = length - 1;
    bool isPalindrome = true;
    for (int i = lastIndex; i >= length / 2; i--){
        if (input[i] != input[lastIndex - i]){
            isPalindrome = false;
            break;
        }
    }
    if (isPalindrome){
        std::cout << ":) Its a Palindrome" << std::endl;
    }else{
        std::cout << ":( Its Not palindrome" << std::endl;
    }
    return 0;
}