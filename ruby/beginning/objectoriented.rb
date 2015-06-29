#define a class
class Box
  #initialzie class variables
  @@count = 0
  #constructor method
  def initialize(w,h)
    @width, @height = w,h
    @@count += 1
  end
  #accessor method
  def getWidth
    @width
  end
  def getHeight
    @height
  end
  
  private :getWidth, :getHeight
  
  #setter method
  def setWidth=(value)
    @width = value
  end
  
  def setHeight=(value)
    @height = value
  end
  
  def getArea
    getWidth * getHeight
  end
  
 def self.printCount
   puts "Box count is : #@@count"
 end
 
 def to_s
   "(w:#@width, h:#@height)" #string formatting of the object
 end
 
 def printArea
   @area = getWidth * getHeight
   puts "Big box area is: #@area"
 end
 #make it protected
 protected :printArea
end

#create an object
box = Box.new(10,20)
box2 = Box.new(10,20)
box3 = Box.new(10,20)


box.setHeight = 30
box.setWidth = 50

#x = box.getWidth()
#y = box.printHeight()
a = box.getArea()
#
#puts "Width of the box is : #{x}"
#puts "Height of the box is: #{y}"

puts "Area of the box is : #{a}"

Box.printCount()

puts "String representation of box is : #{box}"

#box.printArea()