import torch.optim as optim
import torch.nn as nn
import torch


class QTrainer:

    def __init__(self, model, learning_rate, gamma):
        self.lr = learning_rate     # learning rate
        self.model = model  # the actual model
        self.gamma = gamma  # gamma
        self.optimizer = optim.Adam(model.parameters(), lr=self.lr)     # optimizer
        self.criterion = nn.MSELoss()

    def train_step(self, state, action, reward, next_state, done):
        """Training function"""
        state = torch.tensor(state, dtype=torch.float)
        next_state = torch.tensor(next_state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.long)
        reward = torch.tensor(reward, dtype=torch.float)
        # (n, x)

        if len(state.shape) == 1:   # we only have one number
            # we want this dimension (1, x)
            state = torch.unsqueeze(state, 0)
            next_state = torch.unsqueeze(next_state, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            done = (done, )  # define as tuple with one value

        # predict values with current state
        pred = self.model(state)

        target = pred.clone()
        for index in range(len(done)):
            Q_new = reward[index]
            if not done[index]:
                Q_new = reward[index] + self.gamma * torch.max(self.model(next_state[index]))

            target[index][torch.argmax(action).item()] = Q_new

        # apply Q_new = r + gamma * max(next prediction Q value) -> only if not done
        # pred.clone()
        # preds[argmax(action) = Q_new

        self.optimizer.zero_grad()  # empty the gradient
        loss = self.criterion(target, pred)  # calculate the loss
        loss.backward()     # backward propagation

        self.optimizer.step()
