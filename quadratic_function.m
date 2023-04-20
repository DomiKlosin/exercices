clear all
clear clc
close all

a=input("Podaj wartość a: ")
b=input("Podaj wartość b: ")
c=input("Podaj wartość c: ")

d=b^2-4*a*c;

if d<0
    disp("Brak miejsc zerowych")
elseif d==0
    x0=-b/2*a;
    disp("Równanie ma jedno rozwiązanie")
    disp(x0)
elseif d>0
    d2=sqrt(d);
    x1=(-b-d2)/2*a;
    x2=(-b+d2)/2*a;
    disp("Równanie ma dwa rozwiązania")
    disp(x1)
    disp(x2)
end

