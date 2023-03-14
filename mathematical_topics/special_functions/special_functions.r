sigmoid_function <- function(x){
    e <- 2.71
    y <- 1 / (1 + e^(-x))
    return(y)
}