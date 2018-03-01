
#program to check the accuracy of the algorithm

def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

def conf_matrix_metric(expected, predicted, n_classes):
    m = [[0] * n_classes for i in range(n_classes)]
    for pred, exp in zip(predicted, expected):
        m[pred][exp] += 1
    t = sum(sum(l) for l in conf_matrix)
    acurracy= sum(conf_matrix[i][i] for i in range(len(conf_matrix)))/t
    return [m, acurracy]
