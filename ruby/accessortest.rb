class Person
  attr_accessor :name
#  attr_reader :name
#  attr_writer :name
#  def name
#      @name # simply returning an instance variable @name
#  end
#  def name=(str)
#      @name = str
#    end
end

person = Person.new
puts person.name # => no method error
person.name = "Dennis" # => no method error