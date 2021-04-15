class SLNode{
    constructor(val){
        this.val = val;
        //pointer to next node.
        this.next = null;
    }
}

class SLL{
    constructor(head = null){
        this.head = head;
    }

    prependValue(val,before){
        var node = new SLNode(val);
        var runner = this.head;
        while(runner){
            if(runner.next.val == before){
                node.next = runner.next;
                runner.next = node;
                return this;
            }
            runner = runner.next;
        }
    }
}

var list = new SLL();
var node0 = new SLNode(0);
var node1 = new SLNode(1);
var node2 = new SLNode(2);

node0.next = node1;
node1.next = node2;
list.head = node0;
var pepper = list.prependValue(9,2);
console.log(list.head);


// if(this.head == null){
//     this.head = node;
//     return this;
// }
        