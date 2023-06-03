function P_matrix(graph, n)
    p_matrix = Array{Float64,2}(undef, n, n)
    for i in 1:n
        row_sum = sum(graph[i])
        if row_sum == 0
            for j in 1:n
                p_matrix[i,j] = 1/n
            end
        else
            for j in 1:n
                p_matrix[i,j] = graph[i,j]/row_sum
            end
        end
    end
    return p_matrix
end

function M_matrix(graph, a)
    n = length(graph[1,:])
    p_matrix = P_matrix(graph, n)
    j_matrix = ones(Float64, n, n)

    return (1-a) * p_matrix + a * (1/n) * j_matrix
end

function Stationary_dist(graph, a)
    n = length(graph[1,:])
    m_matrix = M_matrix(graph, a)

    return transpose(ones(Float64, n) / n) * (m_matrix ^ (2 ^ 12))
end

alphas = [0, 0.15, 0.5, 1]

graph = [1 0 0 0 0 0;
         0 0 1 0 1 0;
         1 0 0 0 0 0;
         0 1 0 0 1 0;
         0 0 0 1 0 0;
         0 0 1 0 0 0]

graph_altered = [1 0 0 0 0 0;
                 0 0 0 0 1 0;
                 1 0 0 0 0 0;
                 0 1 0 0 1 0;
                 0 0 0 1 0 0;
                 0 0 1 0 0 0]

println("Normal graph")
for a in alphas
    println("alpha = $a")
    println(Stationary_dist(graph, a))
end

println("\nAltered graph")
for a in alphas
    println("alpha = $a")
    println(Stationary_dist(graph_altered, a))
end
