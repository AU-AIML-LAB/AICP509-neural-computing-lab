a = input('Enter the input for a: ');
b = input('Enter the input for b: ');
c = a + b;
d = a.* b;
as = c -d ;
e  = 1 - b;
ad = a + e;
f = a- b;
bs = min(1, c);
bd = max(0, f);
g = c - 1;
bp = max(0, g);
disp('The Algebraic Sum');
disp(as);
disp('The Algebraic Difference');
disp(ad);
disp('The bounded Sum');
disp(bs)
disp('The bounded Difference');
disp(bd)
disp('The bounded Product');
disp(bp);
