async function incrementCounter(increment = 1){
    result = await fetch("/increment?increment=" + increment);
    result = await result.text()
    elem = document.getElementById("counter");
    elem.innerHTML = result;
}