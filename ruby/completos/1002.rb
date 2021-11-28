PI = 3.14159

def calc_area (raio)
    return (PI * (raio ** 2)).round(4) 
end

puts "A=%.4f" % calc_area(gets.chomp.to_f)