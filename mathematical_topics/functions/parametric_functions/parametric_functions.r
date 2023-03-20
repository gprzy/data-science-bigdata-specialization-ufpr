linear_parametric_function <- function(x, theta) {
    y <- (x - theta)^2
    return(y)
}

two_parameter_function <- function(x, theta_1, theta_2) {
    y <- (x - theta_1)^2 / (theta_2)
    return(y)
}

print(
    paste(
        "linear_parametric_function on x = 2, and theta 1 = 3 =",
        linear_parametric_function(
            x = 2, theta = 3
        )
    )
)

print(
    paste(
        "two_parameter_function on x = 2, and theta 1, 2 = (2, 3) =",
        two_parameter_function(
            x = 2, theta_1 = 2, theta_2 = 3
        )
    )
)
