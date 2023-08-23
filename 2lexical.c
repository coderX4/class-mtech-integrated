#include<stdio.h>
#include<ctype.h>
#include<string.h>
#include <stdbool.h>
int main()
{
    FILE *input;
    int l=1,t=0,j=0,i,flag;
    char ch,str[20];
    input = fopen("input.txt","r");
    printf("Line no. \t Token no. \t Token \t Lexeme\n\n");
    while(!feof(input))
    {
        i=0;
        flag=0;
        ch=fgetc(input);
        if( ch=='+' || ch== '-' || ch=='*' || ch=='/' )
        {
            printf("%7d\t\t %7d\t\t Operator\t %7c\n",l,t,ch);
            t++;
        }
        else if( ch==';' || ch=='{' || ch=='}' || ch=='(' || ch==')' || ch=='?' ||
                ch=='@' || ch=='!' ||ch=='%')
            {
                printf("%7d\t\t %7d\t\t Special symbol\t %7c\n",l,t,ch);
                t++;
            }
        else if(isdigit(ch))
        {
            printf("%7d\t\t %7d\t\t Digit\t\t %7c\n",l,t,ch);
            t++;
        }
        else if(isalpha(ch))
        {   
            str[i]=ch;
            i++;
            ch=fgetc(input);
            while(isalnum(ch) && ch!=' ')
            {
                str[i]=ch;
                i++;
                ch=fgetc(input);
            }
            str[i]='\0';
            for(j=0;j<=300;j++)
            {
                if(!strcmp(str, "if") || !strcmp(str, "else") ||
        !strcmp(str, "while") || !strcmp(str, "do") ||
        !strcmp(str, "break") ||
         !strcmp(str, "continue") || !strcmp(str, "int")
        || !strcmp(str, "double") || !strcmp(str, "float")
        || !strcmp(str, "return") || !strcmp(str, "char")
        || !strcmp(str, "case") || !strcmp(str, "char")
        || !strcmp(str, "sizeof") || !strcmp(str, "long")
        || !strcmp(str, "short") || !strcmp(str, "typedef")
        || !strcmp(str, "switch") || !strcmp(str, "unsigned")
        || !strcmp(str, "void") || !strcmp(str, "static")
        || !strcmp(str, "struct") || !strcmp(str, "goto"))
                {
                    flag=1;
                    break;
                }
            }
            if(flag==1)
            {
                printf("%7d\t\t %7d\t\t Keyword\t %7s\n",l,t,str);
                t++;
            }
            else
            {
                printf("%7d\t\t %7d\t\t Identifier\t %7s\n",l,t,str);
                t++;
            } 
        }
        else if(ch=='\n')
        {
            l++;
        }
    }
    fclose(input);
    return 0;
} 

