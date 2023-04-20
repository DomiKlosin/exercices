clear all
clear clc
t=[0:0.0001:pi];
f=@(t)sin(t);
c=integral(f,0,pi);

tp=0;
tk=pi;
n=length(t);
h=(tk-tp)/n;
ts=tp:h:tk;

x=sin(ts);
P=h*(sum(x(2:n))+(x(1)+x(n+1))/2);

disp("wartość c=")
disp(c);
disp("wartość P4=")
disp(P);

