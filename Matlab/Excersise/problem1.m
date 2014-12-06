t=-10:0.01:10;

for i=1:length(t)
    if t(i) < -pi
        y(i)= 2 * sin(t(i) - 0.25);
    elseif t(i) >  -pi & t(i) < pi
        y(i) = 3 * t(i) / pi;
    else
        y(i) = cos(t(i));
    end
end
plot(t,y,'.');