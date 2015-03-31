clear;
t = -10:0.1:10;
Y = zeros(1, length(t));

for i = 1:5
    y = sin(2 * pi * t * i);
    Y = Y + y;
end

plot(t,Y);