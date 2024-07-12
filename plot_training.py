import math
import random
import numpy as np
import matplotlib.pyplot as plt


class Data:
    def __init__(self, number_of_points):
        self.values = []
        self.number_of_points = number_of_points

    def generate_data(self):
        for _ in range(self.number_of_points):
            self.values.append(random.randint(1, 100))

    # A Comprehensive Guide to Activation Functions in Deep Learning.
    # [link][https://medium.com/aimonks/a-comprehensive-guide-to-activation-functions-in-deep-learning-ff794f87c184]

    # 1. Sigmoid Activation Function
    def sigmoid(self):
        for i in range(len(self.values)):
            self.values[i] = 1 / (1 + math.exp(-self.values[i]))

    # 2. Tanh Activation Function
    def tanh(self):
        for i in range(len(self.values)):
            self.values[i] = np.tanh(self.values[i])

    # 3. Rectified Linear Unit (ReLU) Activation Function
    def relu(self):
        for i in range(len(self.values)):
            self.values[i] = max(0, self.values[i])

    # 4. Leaky ReLU Activation Function
    def leaky_relu(self, alpha=0.01):
        for i in range(len(self.values)):
            self.values[i] = max(alpha * self.values[i], self.values[i])

    # 5. Exponential Linear Unit (ELU) Activation Function
    def elu(self, alpha=1.0):
        for i in range(len(self.values)):
            self.values[i] = np.where(self.values[i] > 0, self.values[i], alpha * (np.exp(self.values[i]) - 1))

    # 6. Swish Activation Function
    def swish(self):
        for i in range(len(self.values)):
            self.values[i] = self.values[i] / (1 + math.exp(-self.values[i]))

    # 7. Parametric ReLU Activation Function
    def prelu(self, alpha=0.01):
        for i in range(len(self.values)):
            self.values[i] = max(alpha * self.values[i], self.values[i])

    # 8. Randomized Leaky ReLU (RReLU) Activation Function
    class RReLU:
        def __init__(self, lower=0.125, upper=0.333):
            self.lower = lower
            self.upper = upper

        def __call__(self, x):
            alpha = random.uniform(self.lower, self.upper)
            return np.maximum(alpha * x, x)

    # 9. Parametric Exponential Linear Unit (PELU) Activation Function
    class PELU:
        def __init__(self, alpha=1.0):
            self.alpha = alpha

        def __call__(self, x):
            return np.where(x > 0, x, self.alpha * (np.exp(x) - 1))

    # 10. Softmax Activation Function
    def softmax(self):
        return np.exp(self.values) / np.sum(np.exp(self.values), axis=0)

    # 11. Softplus Activation Function
    def softplus(self):
        return np.log(1 + np.exp(self.values))

    # 12. ArcTan Activation Function
    def arctan(self):
        return np.arctan(self.values)

    # 13. Gaussian Error Linear Unit (GELU) Activation Function
    def gelu(self):
        for i in range(len(self.values)):
            self.values[i] = 0.5 * self.values[i] * (
                    1 + math.tanh(
                            math.sqrt(2 / math.pi) * (
                                    self.values[i] + 0.044715 * math.pow(self.values[i], 3)
                            )
                    )
            )

    # 14. Swish-1 Activation Function
    def swish1(self):
        for i in range(len(self.values)):
            self.values[i] = self.values[i] / (1 + math.exp(-self.values[i]))

    # 15. Inverse Square Root Linear Unit (ISRLU) Activation Function
    def isrlu(self, alpha=1.0):
        for i in range(len(self.values)):
            self.values[i] = self.values[i] / math.sqrt(1 + alpha * math.pow(self.values[i], 2))

    # 16. Scaled Exponential Linear Unit (SELU) Activation Function
    def selu(self, alpha=1.67326, scale=1.0507):
        for i in range(len(self.values)):
            self.values[i] = scale * np.where(self.values[i] > 0, self.values[i], alpha * (np.exp(self.values[i]) - 1))

    # 17. SoftExponential Activation Function
    def soft_exponential(self, alpha=0.0):
        if alpha < 0:
            return [-np.log(1 - alpha * (self.values[i] + alpha)) / alpha for i in range(len(self.values))]
        elif alpha == 0:
            return self.values
        else:
            return [(np.exp(alpha * self.values[i]) - 1) / alpha for i in range(len(self.values))]

    # 18. Bipolar Sigmoid Activation Function
    def bipolar_sigmoid(self):
        for i in range(len(self.values)):
            self.values[i] = (1 - math.exp(-self.values[i])) / (1 + math.exp(-self.values[i]))

    # 19. Binary Step Activation Function
    def binary_step(self):
        for i in range(len(self.values)):
            self.values[i] = 0 if self.values[i] < 0 else 1


class Plot:
    def __init__(self, number_of_points=100):
        self.data = Data(number_of_points)
        self.data.generate_data()
        self.plot = plt

    def plot_data(self, color="blue", line_style="-", line_width=1, marker=""):
        if marker:
            self.plot.plot(self.data.values, color=color, linestyle=line_style, linewidth=line_width, marker=marker)
        else:
            self.plot.plot(self.data.values, color=color, linestyle=line_style, linewidth=line_width)

    def labellise(self, x_label="X-axis", y_label="Y-axis", title="Random data"):
        self.plot.xlabel(x_label)
        self.plot.ylabel(y_label)
        self.plot.title(title)

    def sigmoid(self):
        self.data.sigmoid()
        self.plot_data("red")

    def tanh(self):
        self.data.tanh()
        self.plot_data("green")

    def relu(self):
        self.data.relu()
        self.plot_data("black")

    def leaky_relu(self):
        self.data.leaky_relu()
        self.plot_data("orange")

    def elu(self):
        self.data.elu()
        self.plot_data("purple")

    def swish(self):
        self.data.swish()
        self.plot_data("brown")

    def prelu(self):
        self.data.prelu()
        self.plot_data("pink")

    def rrelu(self):
        self.data.RReLU()
        self.plot_data("gray")

    def pelu(self):
        self.data.PELU()
        self.plot_data("cyan")

    def softmax(self):
        self.data.softmax()
        self.plot_data("magenta")

    def softplus(self):
        self.data.softplus()
        self.plot_data("yellow")

    def arctan(self):
        self.data.arctan()
        self.plot_data("lime")

    def gelu(self):
        self.data.gelu()
        self.plot_data("olive")

    def swish1(self):
        self.data.swish1()
        self.plot_data("maroon")

    def isrlu(self):
        self.data.isrlu()
        self.plot_data("navy")

    def selu(self):
        self.data.selu()
        self.plot_data("teal")

    def soft_exponential(self):
        self.data.soft_exponential()
        self.plot_data("silver")

    def bipolar_sigmoid(self):
        self.data.bipolar_sigmoid()
        self.plot_data("gold")

    def binary_step(self):
        self.data.binary_step()
        self.plot_data("indigo")

    def show(self):
        self.plot.show()


def run_activation_functions(choices):
    # Dictionary of all available functions
    activation_functions = {
        1: plot.sigmoid,
        2: plot.tanh,
        3: plot.relu,
        4: plot.leaky_relu,
        5: plot.elu,
        6: plot.swish,
        7: plot.prelu,
        8: plot.rrelu,
        9: plot.pelu,
        10: plot.softmax,
        11: plot.softplus,
        12: plot.arctan,
        13: plot.gelu,
        14: plot.swish1,
        15: plot.isrlu,
        16: plot.selu,
        17: plot.soft_exponential,
        18: plot.bipolar_sigmoid,
        19: plot.binary_step
    }

    if 'all' in choices:
        for func in activation_functions.values():
            func()
    else:
        for choice in choices:
            if choice in activation_functions:
                activation_functions[choice]()

def main():
    global plot
    plot = Plot(100)

    # Example user input processing
    user_input = input("Enter activation function numbers separated by comma or 'all': ")

    if user_input.strip().lower() == 'all':
        choices = ['all']
    else:
        # Convert input string numbers to a list of integers
        try:
            choices = list(map(int, user_input.split(',')))
        except ValueError:
            print("Invalid input. Please enter only numbers separated by commas or 'all'.")
            return

    run_activation_functions(choices)
    plot.show()


if __name__ == "__main__":
    main()
