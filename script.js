let stack = [];

function renderStack() {
    let container = document.getElementById("stack-container");
    container.innerHTML = "";

    for (let i = stack.length - 1; i >= 0; i--) {
        let div = document.createElement("div");
        div.className = "box";
        div.innerText = stack[i];
        container.appendChild(div);
    }
}

function push() {
    let value = document.getElementById("value").value;

    if (value !== "") {
        stack.push(value);
        renderStack();
        document.getElementById("value").value = "";
    }
}

function pop() {
    stack.pop();
    renderStack();
}
