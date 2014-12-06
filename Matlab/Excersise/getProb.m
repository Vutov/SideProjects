function P=getProb(mk, side)
%mk = 100;
br = 0;

for i=1:mk
    zar = randi([1,side]);
    if zar == 6
        br = br + 1;
    end
end

P = br/mk;