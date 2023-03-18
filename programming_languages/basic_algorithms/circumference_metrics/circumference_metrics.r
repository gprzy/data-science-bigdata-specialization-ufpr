circumference_metrics <- function(radius){
    perimeter <- 2*pi*radius
    area <- pi*radius^2
    return(c(perimeter, area))
}

print(circumference_metrics(8))
