function realFCount(n::Int)::Int
    if n == 0
        return 0
    end

    return n + sum(realFCount(i) for i in 0:n-1)
end

function calculatedFCount(n::Int)::Int
    return 2^n - 1
end

function test()::Nothing
    for n in 0:32
        println(n)
        if realFCount(n) != calculatedFCount(n)
            println("INEQUALITY")
            return
        end
    end
    println("all equal")
end

test()
    
