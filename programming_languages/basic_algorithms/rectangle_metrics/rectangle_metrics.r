rectangle_metrics <- function(a, b){
    area <- a*b
    diagonal <- sqrt(a^2 + b^2)
    return(c(area, diagonal))
}

print(rectangle_metrics(10, 20))
