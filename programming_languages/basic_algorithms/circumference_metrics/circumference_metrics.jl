function circumference_metrics(radius)
    perimeter = 2*pi*radius
    area = pi*radius^2
    return perimeter, area
end

println(circumference_metrics(8))
