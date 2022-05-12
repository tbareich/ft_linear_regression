using CSV, DataFrames

θ0 = 0.0
θ1 = 0.0
learning_rate = 0.1
f(X)::Vector{Float64} = θ0 .+ θ1 * X
epoch = 0
data = CSV.File("data.csv") |> DataFrame
X = data[1:end, 1]
Y = data[1:end, 2]
m = length(X)
maxX = max(X...)
maxY = max(Y...)

X = X ./ maxX
Y = Y ./ maxY
while epoch <= 1000
    tmp_θ0 = (1 / m) * sum(f(X) - Y)
    tmp_θ1 = (1 / m) * sum(X .* (f(X) - Y))
    global θ0 -= learning_rate * tmp_θ0
    global θ1 -= learning_rate * tmp_θ1
    global epoch += 1
end
@show θ0
@show θ1