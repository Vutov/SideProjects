clear;
t1=-10:0.01:-pi;
t2=-pi + 0.01:0.01:pi;
t3=pi + 0.01:0.01:10;
t = [t1 t2 t3];

y1 = 2 * sin(t1);
y2 = 3 * t2 / pi;
y3 = cos(t3);

y=[y1 y2 y3]

plot(t,y,'.');