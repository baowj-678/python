var a = 1;
var b = a + "";
//console.info(!!"");
//
// if(true)
// {
//     a = 2;
// }

// false || (a = 2);

function score(s)
{
    //"||"可以用于赋初值
    return s || 5;
}

console.info(score(1));
console.info(score());
console.info(a);