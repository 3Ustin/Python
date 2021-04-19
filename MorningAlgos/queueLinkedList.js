class SLNode{
    constructor(val){
        this.val = val;
        //this variable is called the pointer.
        this.next = null;
    }
}
class SLQUEUE{
    constructor(){
        this.head = null;
        this.tail = null;
    }
    enqueue(val){
        var node = new SLNode(val);
        var runner = this.head;
        while(runner.next){
            runner = runner.next;
        }
        runner.next = node;
        this.tail = node;
        return node;
    }
    dequeue(){
        var runner = this.head.next;
        this.head = null;
        this.head = runner;
        return runner
    }
    front(){
        return this.head
    }
    contains(val){
        var runner = this.head;
        while(runner){
            if(runner.val == val){
                return true;
            }
            runner = runner.next;
        }
        return false;
    }
    isEmpty(){
        if(this.head == null){
            return true;
        }
        else{
            return false;
        }
    }
    size(){
        var i = 0;
        var runner = this.head;
        while(runner){
            i++;
            runner = runner.next;
        }
        return i;
    }
}


node0 = new SLNode(0);
node1 = new SLNode(1);
node2 = new SLNode(2);
node3 = new SLNode(3);
node4 = new SLNode(4);
node5 = new SLNode(5);
node0.next = node1;
node1.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node5;
var list = new SLQUEUE();
list.head = node0;
list.tail = node5;


console.log(list.enqueue(6));
console.log(list.dequeue(0));
console.log(list.front());
console.log(list.contains(3));
console.log(list.isEmpty());
console.log(list.size());