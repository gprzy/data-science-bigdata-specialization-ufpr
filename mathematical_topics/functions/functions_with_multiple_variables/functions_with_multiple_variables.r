fx1x2 <- function(x) {
    y <- sqrt(25 - x[1]^2 - x[2]^2)
    return(y)
}


# function on x = (0,0)
print(paste("y on x = (0,0) = ", fx1x2(c(0, 0))))

# function on x = (3,0)
print(paste("y on x = (3,0) = ", fx1x2(c(3, 0))))

input_1 <- c(0, 0)
input_2 <- c(3, 0)

input <- matrix(
    c(input_1, input_2),
    ncol = 2, nrow = 2,
    byrow = TRUE
)

cat("\ninput")
print(input)

output <- c()
for (i in 1:2) {
    output[i] <- fx1x2(input[i, ])
}

output
