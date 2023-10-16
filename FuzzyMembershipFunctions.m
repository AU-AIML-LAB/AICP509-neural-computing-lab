x = (0.0:1.0:10.0);
subplot(311);
y1 = trimf(x, [1, 3, 5]);
plot(x,y1);

subplot(312);
y2 =  trapmf(x, [1, 3, 5, 7]);
plot(x,y2);
x2 = (0.0:0.2:10.0);
y3 = gbellmf(x2, [1,2,5]);
subplot(313);

plot(x2,[y3]);