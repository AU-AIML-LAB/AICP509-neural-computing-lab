import numpy as np

class Perceptron:
    def __init__(self) -> None:
        self.weight = np.zeros((2, 1))
        self.bias = 0
        self.learning_rate = 0.1

    def predict(self, x: np.array) -> np.array:
        return np.where(np.dot(self.weight.T, x.T) + self.bias > 0, 1, 0)
    
    def fit(self, x: np.array, y: np.array, epoch:int = 100) -> None:
        for _ in range(epoch):
            for x_i, y_i in zip(x, y):
                y_hat = self.predict(x_i).squeeze()
                self.weight += self.learning_rate * (y_i - y_hat) * x_i.reshape(-1, 1)
                self.bias += self.learning_rate * (y_i - y_hat)

    def score(self, x: np.array, y: np.array) -> float:
        y_hat = self.predict(x)
        return np.mean(y_hat == y)
    

if __name__ == '__main__':
    X = np.array([
        [0, 0], 
        [0, 1], 
        [1, 0], 
        [1, 1]])
    
    y = np.array([0, 1, 1, 1])

    perceptron = Perceptron()
    perceptron.fit(X, y, epoch=3)

    print(perceptron.score(X, y))