import hashlib
import numpy as np
import math

def pseudo_random(seed=0xDEADBEEF):
    """Generate an infinite stream of pseudo-random numbers"""
    state = (0xffffffff & seed)/0xffffffff
    while True:
        h = hashlib.sha256()
        h.update(bytes(str(state), encoding='utf8'))
        bits = int.from_bytes(h.digest()[-8:], 'big')
        state = bits >> 32
        r = (0xffffffff & bits)/0xffffffff
        yield r


class weighted_bootstrap:
    def __init__(self, dataset, weights, sample_size):
        self.dataset = dataset
        self.weights = weights
        self.sample_size = sample_size
        self.r = pseudo_random()
        
    def __iter__(self):
        return self
    
    def __next__(self):
        sample = []
        running_sum = list(np.cumsum(self.weights))
        for _ in range(self.sample_size):
            value = next(self.r) * running_sum[-1]
            i = next(i for i, x in enumerate(running_sum) if x >= value)
            sample.append(self.dataset[i])
        return np.array(sample)


def adaboost(learner, dataset, n_models):
    models = []
    weights = [1/len(dataset) for i in range(len(dataset))]
    bootstrap = weighted_bootstrap(dataset, weights, len(dataset))
    for i in range(n_models):
        model = learner(next(bootstrap))
        error = sum(weights[i] for i, example in enumerate(dataset) 
                    if model(example[:-1]) != example[-1])
        models.append((model, error))
        if error == 0 or error >= 0.5:
            break
        for i, example in enumerate(dataset):
            if model(example[:-1]) == example[-1]:
                weights[i] *= error / (1-error)
        weights = [weights[i]/sum(weights) for i in range(len(dataset))]
        bootstrap.weights = weights
    def classifier(x):
        weights = {}
        for model, error in models:
            c = model(x)
            if error == 0:
                weight = float('inf')
            else:
                weight = -math.log(error) / (1-error)
            weights[c] = weights.get(c, 0) + weight
        return min(weights.items(), key=lambda x: (-x[1], x[0]))[0]
    return classifier


def main():
    import sklearn.datasets
    import sklearn.utils
    import sklearn.linear_model
    import sklearn.tree
    
    digits = sklearn.datasets.load_digits()
    data, target = sklearn.utils.shuffle(digits.data, digits.target, random_state=3)
    train_data, train_target = data[:-5, :], target[:-5]
    test_data, test_target = data[-5:, :], target[-5:]
    dataset = np.hstack((train_data, train_target.reshape((-1, 1))))
    
    def linear_learner(dataset):
        features, target = dataset[:, :-1], dataset[:, -1]
        model = sklearn.linear_model.SGDClassifier(random_state=1, max_iter=1000, tol=0.001).fit(features, target)
        return lambda v: model.predict(np.array([v]))[0]
    
    boosted = adaboost(linear_learner, dataset, 10)
    for (v, c) in zip(test_data, test_target):
        print(int(boosted(v)), c)
        
    wine = sklearn.datasets.load_wine()
    data, target = sklearn.utils.shuffle(wine.data, wine.target, random_state=3)
    train_data, train_target = data[:-5, :], target[:-5]
    test_data, test_target = data[-5:, :], target[-5:]
    dataset = np.hstack((train_data, train_target.reshape((-1, 1))))
    
    def tree_learner(dataset):
        features, target = dataset[:, :-1], dataset[:, -1]
        model = sklearn.tree.DecisionTreeClassifier(random_state=1).fit(features, target)
        return lambda v: model.predict(np.array([v]))[0]
    
    boosted = adaboost(tree_learner, dataset, 10)
    for (v, c) in zip(test_data, test_target):
        print(int(boosted(v)), c)


if __name__ == '__main__':
    main()