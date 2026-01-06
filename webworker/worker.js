onmessage = (e) => {
    let result = 0;
    for (let i = 0; i < 1000000000; i++) {
        result += i;
    }

    postMessage(result);
};

console.log(self);
// console.log(document); // not accessible .. because of scope
// console.log(window); // not accessible .. because of scope
// console.log(btn1); // not accessible .. because of scope
