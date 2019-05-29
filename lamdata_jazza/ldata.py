import pandas as pd

class EasyLabel:
  
  """A configurable label encoder
  After running fit, labels will be set to frequency of
  occurrance by default. Run select_labels to set custom labels
  Run get_params to print current labels and fit info
  Run return_params to return current  labels and fit info"""
  
  def __init__(self, labels=None, categories=None):
    self = self
    self.frequency = []
    self.labels = labels
    self.categories = categories
    pass
  
  def fit(self, X):
    """This gets categories and frequency of occurrance,
    After running fit, labels will be set to frequency of
    occurrance by default. Run select_labels"""
    datas = pd.Series(X)
    vals = [0]*2
    vals[0] = datas.value_counts().index
    vals[1] = datas.value_counts().values
    self.categories = vals[0]
    self.labels = vals[1]
    self.frequency = vals[1]
    pass
    
  def get_params(self):
    print('You have {} categories'.format(len(self.categories)))
    print('Your categories are:     {}'.format(self.categories, list(self.categories)))
    print('Frequency of categories: {}'.format(dict(zip(self.categories, self.frequency))))
    print('Normalized frequency:    {}'.format(dict(zip(self.categories, self.frequency/len(self.frequency)))))
    print('Current category labels: {}'.format(dict(zip(self.categories, self.labels))))
    pass


  def return_params(self):
    return(self.categories, self.labels, self.frequency)
  
  def select_labels(self, lbl = [0]):
    """Label in the order categories are printed in get_params()
    Will label by frequency if no labels are selected"""
    if len(lbl) == 1:
      dictionary = dict(zip(self.categories, self.labels))
      return(dictionary)
    elif len(lbl) == len(self.categories):
      self.labels = pd.Series(lbl)
      dictionary = dict(zip(self.categories, self.labels))
      print(dictionary)
      return(dictionary)
    else:
      print('Error: wrong number of labels')
      pass

  def transform(self, X):
    """Returns pandas series of labels encoded according to labels parameter"""
    datas = pd.Series(X)
    datas = datas.replace(dict(zip(self.categories, self.labels)))
    return(datas)

