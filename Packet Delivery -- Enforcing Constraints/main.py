'''
Create class "Package" that represents a package which has a length, width, height (cm) and weight (kg) parameter.

Furthermore, the following should always give the current volume of the package:

p = Package(0.2, 0.2, 0.2)
p.volume  # computes 0.2 * 0.2 * 0.2 and returns it
But lo and behold! The following constraints must be satisfied for all packages at all time:

0 < length <= 350
0 < width <= 300
0 < height <= 150
0 < weight <= 40
For example, the following should raise a custom (written-by-you) DimensionsOutOfBoundError:

p = Package(351, 0.2, 0.2, 0.2)
# raises DimensionsOutOfBoundError with  message:
#  "Package length==351 out of bounds, should be: 0 < length <= 350"
'''
class DimensionsOutOfBoundError(Exception):
    pass

class Package:    
  def __init__(self, length, width, height, weight):
    print("length={}, width={}, height={}, weight={}".format(length, width, height, weight))    
    self.length = length
    self.width = width
    self.height = height
    self.weight = weight
    self.volume = length * width * height    
  def __setattr__(self, key, value):
    self.__dict__[key] = value
    if (key is 'length' or key is 'width' or key is 'height'):
      if (hasattr(self, 'length') and hasattr(self, 'width') and hasattr(self, 'height')):
        self.volume = self.length * self.width * self.height
    if key is 'length':
      self.check_length()
    if key is 'width':
      self.check_width()
    if key is 'height':
      self.check_height()
    if key is 'weight':
      self.check_weight() 

  def check_length(self):
    if not(0 < self.length <= 350):
      raise DimensionsOutOfBoundError("Package length=={} out of bounds, should be: 0 < length <= 350".format(self.length))
  def check_width(self):  
    if not(0 < self.width <= 300):
      raise DimensionsOutOfBoundError("Package width=={} out of bounds, should be: 0 < width <= 300".format(self.width))
  def check_height(self):  
    if not(0 < self.height <= 150):
      raise DimensionsOutOfBoundError("Package height=={} out of bounds, should be: 0 < height <= 150".format(self.height))
  def check_weight(self):   
    if not(0 < self.weight <= 40):
      raise DimensionsOutOfBoundError("Package weight=={} out of bounds, should be: 0 < weight <= 40".format(self.weight))

  

    
def main():
  p = Package(350, 300, 150, 40)
  p.length = 400
main()