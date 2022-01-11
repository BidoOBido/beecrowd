def calc_media(nota_a, nota_b)
    return ((nota_a * 3.5) + (nota_b * 7.5)) / 11
end

puts "MEDIA = %.5f" % calc_media(gets.chomp.to_f, gets.chomp.to_f).round(5)