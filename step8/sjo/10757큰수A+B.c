#include <stdio.h>
#include <string.h>

void reverse(char s[])
{
    int len = strlen(s);
    char tmp;
    
    for (int i = 0; i < len / 2; i++)
    {
        tmp = s[i];
        s[i] = s[len - 1 - i];
        s[len - 1 - i] = tmp;
    }
}

int main()
{
    char a[10001] = { 0 }, b[10001] = { 0 }, result[10002] = { 0 };
    int carry = 0;
    int a_num, b_num, sum;
    
    scanf("%s %s", a, b);
    int len = strlen(a) > strlen(b) ? strlen(a) : strlen(b);
    reverse(a);
    reverse(b);
    
    for (int i = 0; i < len; i++)
    {
        a_num = a[i] - '0';
        b_num = b[i] - '0';
        if (!a[i])
            sum = b_num + carry;
        else if (!b[i])
            sum = a_num + carry;
        else
            sum = a_num + b_num + carry;
        carry = sum > 9 ? 1 : 0;
        result[i] = sum % 10 + '0';
    }
    if (carry == 1)
        result[len] = '1';
    reverse(result);
    printf("%s", result);
}
