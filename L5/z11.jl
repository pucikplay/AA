function nodeAction(i, s, graph)
    if s[i] == 0 && all(j -> s[j] == 0, graph[i])
        s[i] = 1
    end
    if s[i] == 1 && 1 in graph[i]
        s[i] = 0
    end
end

function maxIndSet(graph)
    n = length(graph)
    state_prev = zeros(Bool, n)
    state_curr = zeros(Bool, n)
    state_prev[1] = 1
    
    while state_prev != state_curr
        state_prev = state_curr
        for i in 1:n
            nodeAction(i, state_curr, graph)
        end
    end
    println(state_curr)
end

graph = [[2 4],
         [1 3 5],
         [2 6],
         [1 5],
         [4 2 6],
         [5 3]]

maxIndSet(graph)