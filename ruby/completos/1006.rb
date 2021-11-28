def calc_media(nota_a, nota_b, nota_c)
    return (((nota_a * 2) + (nota_b * 3) + (nota_c * 5)) / 10).round(1)
end

puts "MEDIA = %.1f" % calc_media(gets.chomp.to_f, gets.chomp.to_f, gets.chomp.to_f)