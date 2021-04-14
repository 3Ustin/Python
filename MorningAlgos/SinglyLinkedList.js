//THIS IS BASE EXAMPLE OF node constructor.
//
// class SLNode{
//     constructor(val){
//         this.val = val;
//         this.next = null;
//     }
// }

// class SLL{
//     constructor(){
//         this.head = null;
//     }
// }

class SingleLinkedNode{
    constructor(val){
        this.val = val;
        //pointer to next node.
        this.next = null;
    }
}

class SingleLinkedList{
    constructor(head = null){
        this.head = head;
    }
}


let node1 = new SingleLinkedNode(1);
let node2 = new SingleLinkedNode(2);
node1.next = node2;

let list = new SingleLinkedList(node1);

console.log(list.head.next.val);

node0 = new SingleLinkedNode(0);
node0.next = node1;
list.head = node0;

console.log(list.head.next.val);
console.log(list.head.val);

while(node0.next){
    node0.next = node0.next.next;
}

console.log(list.next);


//THIS IS EXAMPLE OF INSTANTIATING IN A LOOP!
//var runner = 0;
// var num = 2;
// for(var i = 0; i < num; i++){
//     node = new SingleLinkedNode(0);
//     list.push(node)
//     list[i].next = list[i-1];
// }

//THIS IS THE TEACHER EXAMPLE OF ITTERATING THROUGH A SERIES OF LINKED OBJECTS.
//
// class SingleLinkedList{
//     constructor(head = null){
//         this.head = head;
//     }

//     addBack(val){
//         var node = new SingleLinkedNode(val);

//         if(this.head == null){
//             this.head = node
//             return this;
//         }

//         var runner = this.head;
//         while(runner.next){
//             runner = runner.next;
//         }
//         runner.next = node;
//         return this;
//     }
//     printVals(){
//         var runner = this.head;
//         while(runner.next){
//             console.log(runner.val);
//             runner = runner.next
//         }
//     }
// }

// var list = new SingleLinkedList();

// list.addBack(4);
// list.addBack(18);
// list.printVals();

