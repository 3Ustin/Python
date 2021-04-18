class SingleLinkedNode{
    constructor(val){
        this.val = val;
        this.next = null;
    }
}

class SingleLinkedList{
    constructor(head = null){
        this.head = head;
    }

    apendValue(val,after){
        //This head doesn't exist.
        if(this.head == null){
            var node = new SingleLinkedNode(val);
            this.head = node;
        }
        var node = new SingleLinkedNode(val);
        var runner = this.head;
        var doesValExist = false;
        while(runner){
            if(runner.val == after){
                doesValExist = true;
                node.next = runner.next;
                runner.next = node;
            }
            runner = runner.next;
        }

        //If the val is not in the list
        if(!doesValExist){
            this.addBack(val);
            }
        }

    addBack(val){
        var node = new SingleLinkedNode(val);

        if(this.head == null){
            this.head = node
            return this;
        }

        var runner = this.head;
        while(runner.next){
            runner = runner.next;
        }
        runner.next = node;
        return this;
    }
}


// var node0 = new SingleLinkedNode(0);
// var runner = node0;
// for(var i = 1; i< 8; i++){
//     let node = new SingleLinkedNode(i);
//     runner.next = node;
//     let node1 = new SingleLinkedNode(i+1);
//     node.next = node1;
//     runner = node1;
// }
// let listicus = new SingleLinkedList();
// listicus.head = node0;
// console.log(listicus);




let node1 = new SingleLinkedNode(0);
let node2 = new SingleLinkedNode(4);
let node3 = new SingleLinkedNode(6);
let node4 = new SingleLinkedNode(2);
let node5 = new SingleLinkedNode(26);
let node6 = new SingleLinkedNode(24);
node1.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node5;
node5.next = node6;


let list = new SingleLinkedList(node1);

list.apendValue(3,2);

console.log(list.head.next.next);
