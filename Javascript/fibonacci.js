function fib(n)
{
    if(n < 2)
    {
        return n;
    }
    else
    {
        return fib(n - 1) + fib(n - 2);
    }
}

function fib_(n)
{
    return n < 2 ? n : fib(n - 1) + fib(n - 2);
}
console.info(fib_(9));