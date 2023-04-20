clear all
close all
clear clc

disp("Podaj wartości współczynników przy niewiadomych układu równań")
x1=input("x1 = ");
x2=input("x2 = ");
x3=input("x3 = ");
y1=input("y1 = ");
y2=input("y2 = ");
y3=input("y3 = ");
z1=input("z1 = ");
z2=input("z2 = ");
z3=input("z3 = ");

disp("Podaj wartości wyrazów wolnych układu ")
b1=input("b1 = ");
b2=input("b2 = ");
b3=input("b3 = ");

A=[x1 y1 z1;x2 y2 z2;x3 y3 z3]; %macierz współczynników
b=[b1;b2;b3];                   %macierz wyrazów wolnych

W=det(A);

if W==0
    disp("Błąd! Wyznacznik macierzy A jest równy zero!")
else
    disp("Rozwiązanie układu z użyciem macierzy odwrotnej")
    X=A\b               %zapis równoznaczny z A^-1.*b

    disp("Rozwiązanie układu wzrorami Cramera")
    Ax=A;
    Ax(:,1)=b;          %macierz Ax
    Wx=det(Ax);
    Ay=A;
    Ay(:,2)=b;          %macierz Ay
    Wy=det(Ay);
    Az=A;
    Az(:,3)=b;          %macierz Az
    Wz=det(Az);

    x=Wx/W
    y=Wy/W
    z=Wz/W
end
