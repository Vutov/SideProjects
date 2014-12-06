clear;
%Задача за 5
t = -10:0.1:10;
Y = zeros(1, length(t));

for i = 1:5
    y1 = sin(2 * pi * t * i);
    Y = Y + y1;
end
for j = 1:8
    z = power(2, j) * power(t, 2);
    y2 = sqrt(z);
    Y = Y + y2;
end

plot(t,Y);