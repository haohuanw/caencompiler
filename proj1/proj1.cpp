#include <iostream>
#include "io.h"

double calcBalance(double beginning, double monthPay, double intRate);

int main(int argc, char *argv[])
{
    double monthPay = 0.0;
    double interestRate = 0.0;
    double year = 0.0;
    //double remainder = 0.0;
    double balance=0.0;
    monthPay = 5;
    interestRate = 0.1;
    int done = 0;
    while(done == 0){
        year = 10;
        if(year == (int)year){
            done = 1;
        }
    }
    PrintHeader();
    double month = year*12;
    double principal = calcBalance(0,monthPay,interestRate);
    balance+=principal;
    double tmp = balance;
    while(month>0){
        PrintMonthlyData(month,principal,100-principal,balance);
        --month;
        balance = calcBalance(balance,monthPay,interestRate);
        principal = balance-tmp;
        tmp = balance;
    }
    return 0;
}

double calcBalance(double beginning, double monthPay, double intRate)
{
    return (beginning+monthPay)/(1+intRate/12);
}
