def my_method
  puts "foo"
end

def my_method2
  puts "bar"
end

cmd_hash = Hash.new()
cmd_hash[0] = method(:my_method)
cmd_hash[1] = method(:my_method2)
cmd_hash[0].call()