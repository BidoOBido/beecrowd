PI = 3.14159

def calc_volume(raio)
    return (4.0/3) * PI * (raio ** 3)
end

puts "VOLUME = %.3f" % calc_volume(gets.chomp.to_i)