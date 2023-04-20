t=[0:0.01:2*pi];

x=sin(t);
dx_a=cos(t);

l=length(t)

dt=diff(t);
dx=diff(x);
dx_n=dx./dt;

figure
hold on
plot(t,x,"b")
plot(t,dx_a,"r")
plot(t(:,2:l),dx_n,"g")
xlabel("t")
ylabel("x")
legend("sin(x)","cos(x)","dx/dt")
