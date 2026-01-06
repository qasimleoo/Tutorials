let count = 0;

let btn1 = document.getElementById("btn1");
btn1.addEventListener("click", () => {
    let worker = new Worker("./worker.js");
    worker.postMessage("Starting");
    worker.onmessage = (e) => {
        document.getElementById("id1").innerHTML = e.data + " " + count++;
    };
});

document.getElementById("btn2").addEventListener("click", () => {
    document.getElementById("id2").innerHTML = "Hello World " + count++;
});
