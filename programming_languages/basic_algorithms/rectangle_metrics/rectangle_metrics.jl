function rectangle_metrics(a, b)
    area = a*b
    diagonal = sqrt(a^2 + b^2)
    return area, diagonal
end

println(rectangle_metrics(10, 20))
