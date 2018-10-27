import csv
import time
import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import Adam
from torch.utils.data import Dataset, DataLoader

FILEPATH = 'data/distance_data.csv'
LR = 0.001
BATCH_SIZE = 32
EPOCH = 500

def readData(filepath):
	f = open(filepath, 'r')
	row = csv.reader(f, delimiter=',')

	x, y = [], []
	for r in row:
		y.append(r[0])
		x.append(r[1:])

	return np.array(x).astype(np.float32), np.array(y).astype(np.int64)

class SE(nn.Module) :
	def __init__(self):
		super(SE, self).__init__()
		self.l1 = nn.Linear(8, 8)
		self.l2 = nn.Linear(8, 4)
		self.out = nn.Linear(4, 2)

	def forward(self, x):
		x = F.relu(self.l1(x))
		x = F.relu(self.l2(x))
		out = self.out(x)
		return out

class Data(Dataset):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __getitem__(self, index):
		return self.x[index], self.y[index]

	def __len__(self):
		return self.x.shape[0]

def fit(model, dataset, optim, loss_function, batch, epochs):
	history = []
	dataLoader = DataLoader(dataset, batch_size=batch, shuffle=True)

	for epoch in range(epochs):
		t1 = time.time()
		for i, (x, y) in enumerate(dataLoader):
			optim.zero_grad()
			output = model(x)
			loss = loss_function(output, y)
			loss.backward()
			optim.step()

		t2 = time.time()
		print('Epoch:', epoch + 1, '| loss:%.4f | time:%.2f' %(loss.data[0], t2 - t1))
		history.append(loss.data[0])

	return history

def loadModel():
	return SE().load_state_dict(torch.load('data/params_SE.pkl'))

def mergeData(x1, x2):
	x = np.concatenate((x1, x2), axis=0)
	x = torch.from_numpy(x)
	return x

def result(out):
	if out.data.numpy()[0] >= 0.5:
		return False
	return True

if __name__ == '__main__':
	x, y = readData(FILEPATH)
	data_train = Data(x, y)

	model = SE()
	optim = Adam(model.parameters(), lr=LR, weight_decay=0.001)
	loss_function = nn.CrossEntropyLoss()

	fit(model, data_train, optim, loss_function, BATCH_SIZE, EPOCH)

	torch.save(model.state_dict(), 'data/params_SE.pkl')
