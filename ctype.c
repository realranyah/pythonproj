#include <stdio.h>

int main()
{
    int num[5],a,x;
    double ave,sum;
    printf("This program determines the sum and the average of positive integers,then,output the sum and average.\n");
    a=0;
    do
        {
        printf("\nNumber%3.d integer is ",a+1);
        scanf("%d",&num[a]);
        if (num[a] <= 0)
            {
            printf("\nInteger has terminated! \n\n");
            break;
            }	
        a++;	
        }
    while (a < 5);
    x = a;
    a=0;
    do
        {
        sum=sum+num[a];
        a++;
        }
    while (a < x);
    ave=sum/x;
    printf("\n\nThe sum of all obtain values is %.2f. \nThen, the average is %.2f", sum,ave);
	
}
