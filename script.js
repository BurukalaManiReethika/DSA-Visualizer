let stack = [];
let queue = [];
let linked = [];

function push() {

const value =
document.getElementById("value").value;

if(value){

stack.push(value);

renderStack();

document.getElementById("value").value="";
}
}

function popItem(){

stack.pop();

renderStack();
}

function renderStack(){

const container =
document.getElementById("stack-container");

container.innerHTML="";

for(let i=stack.length-1;i>=0;i--){

container.innerHTML +=
`<div class="box">${stack[i]}</div>`;
}
}

function enqueue(){

const value =
document.getElementById("value").value;

if(value){

queue.push(value);

renderQueue();

document.getElementById("value").value="";
}
}

function dequeue(){

queue.shift();

renderQueue();
}

function renderQueue(){

const container =
document.getElementById("queue-container");

container.innerHTML="";

queue.forEach(item=>{

container.innerHTML +=
`<div class="box queue-box">${item}</div>`;
});
}

function insertNode(){

const value =
document.getElementById("value").value;

if(value){

linked.push(value);

renderLinked();

document.getElementById("value").value="";
}
}

function deleteNode(){

linked.pop();

renderLinked();
}

function renderLinked(){

const container =
document.getElementById("linked-container");

container.innerHTML="";

linked.forEach((item,index)=>{

container.innerHTML +=
`<span class="linked-node">${item}</span>`;

if(index !== linked.length-1){

container.innerHTML += " ➜ ";
}
});

if(linked.length){

container.innerHTML += " ➜ NULL";
}
}

function toggleTheme(){

document.body.classList.toggle("light");
}
