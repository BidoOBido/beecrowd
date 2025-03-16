while true
  casos = gets.chomp.to_i
  if casos <= 0
    break
  end

  divisa_longitude, divisa_latitude = gets.chomp.split(" ").map(&:to_i)
  (1..casos).each do
    longitude, latitude = gets.chomp.split(" ").map(&:to_i)

    if longitude == divisa_longitude || latitude == divisa_latitude
      puts "divisa"
      next
    end

    coordenada = ""
    if latitude > divisa_latitude
      coordenada += "N"
    else
      coordenada += "S"
    end

    if longitude > divisa_longitude
      coordenada += "E"
    else
      coordenada += "O"
    end

    puts coordenada
  end
end
