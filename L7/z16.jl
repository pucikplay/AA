using Random

function realLCount(n)
    if n == 0 || n == 1
        return 1
    end
    return 2 + sum(realLCount(i) for i in 1:n-1)
end

function randLCount(n)
    if n == 0 || n == 1
        return 1
    end
    count = 1
    for i in 1:n
        if rand([true,false])
            count += randLCount(i)
        end
    end
    return count
end

function avgRandLCount(n,t)
    total = 0
    for _ in 1:t
        total += randLCount(n)
    end
    return total/t
end

function calculatedLCount(n)
    if n == 0 || n == 1
        return 1
    end
    return 3 * 2^(n-2)
end

function test()
    t = 1000
    for n in 1:22
        real = realLCount(n)
        calc = calculatedLCount(n)
        rand = avgRandLCount(n,t)
        error = abs(rand - real)/real
        println("n: $n, Real: $real, Calc: $calc, Rand: $rand, error: $error")
    end
end

test()