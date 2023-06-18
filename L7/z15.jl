function realFCount(n)
    if n == 0
        return 0
    end

    return n + sum(realFCount(i) for i in 0:n-1)
end

function calculatedFCount(n)
    return 2^n - 1
end

function test()
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
    
