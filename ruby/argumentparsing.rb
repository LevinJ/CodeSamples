require 'optparse'

options = {}
OptionParser.new do |opts|
  opts.banner = "Usage: example.rb [options]"

  opts.on("-c", "--command COMMAND",
               "Require the COMMAND before executing your script") do |lib|
         options[] = lib
  end
end.parse!

p options
p ARGV