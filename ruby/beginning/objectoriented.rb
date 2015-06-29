#define a class
class Box
  #constructor method
  def initialize(w,h)
    @width, @height = w,h
  end
  #accessor method
  def printWidth
    @width
  end
  def printHeight
    @height
  end
  
  #setter method
  def setWidth=(value)
    @width = value
  end
  
  def setHeight=(value)
    @height = value
  end
end

#create an object
box = Box.new(10,20)

box.setHeight = 30
box.setWidth = 50

x = box.printWidth()
y = box.printHeight()

puts "Width of the box is : #{x}"
puts "Height of the box is: #{y}"