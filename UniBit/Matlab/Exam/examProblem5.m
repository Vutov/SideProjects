clear;
%%Задача за 6
N = 16;
T = 850;
e = 0.01;
I = 1000;
s = 1:1000:10000000;

Pd = zeros(1, length(s));
for i=0:N
    longPartOne = power((1 + (((1 + I) * T) ./ (1 + I + s))), i) .* power((1 + (T ./ (1 + I + s) ) ) ,(N - i)); 
    longPartTwo = power((1 + (((1 + I) * T) ./ (1 + s))), i) .* power((1 + (T ./ (1 + s) ) ) ,(N - i)); 
    current = nchoosek(N,i) * power(e,i) * power((1-e),(N - i)) * ((e ./ longPartOne) + ((1-e) ./ longPartTwo) )
    Pd = Pd + current;
end

plot(s, Pd)