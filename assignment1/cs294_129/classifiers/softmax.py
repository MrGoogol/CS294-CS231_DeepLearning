import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  for i in xrange(X.shape[0]):
      scores = np.dot(X[i],W)
      loss -= np.log( np.exp(scores)[y[i]]/sum(np.exp(scores)) )
      dW[:,y[i]] -= X[i]
      for j in xrange(W.shape[1]):
        dW[:,j] += X[i]*np.exp(scores)[j]/sum(np.exp(scores))

  loss /= X.shape[0]
  dW /= X.shape[0]    
  loss += 0.5 * reg * np.sum(W * W)
  dW += reg*W        
  
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  scores = np.dot(X,W)
  scores -= np.max(scores,axis=1).reshape(X.shape[0],1)
  P = np.exp(scores)/np.reshape(np.sum(np.exp(scores),axis=1),(X.shape[0],1))
  loss = -np.sum(np.log(P[(range(X.shape[0]),y)]))
  loss /= X.shape[0]
  loss += 0.5 * reg * np.sum(W * W)
  P[(range(X.shape[0]),y)] = P[(range(X.shape[0]),y)] - 1
  dW = np.dot(X.T,P) / X.shape[0]
  dW += reg * W

  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


