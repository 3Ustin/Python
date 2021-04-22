class SLNode{
    constructor(val){
        this.val = val;
        //this variable is called the pointer.
        this.next = null;
    }
}
class SLSTACK{
    constructor(){
        this.head = null;
        this.tail = null;
    }
    //adds to back of the list.
    push(val){
        var node = new SLNode(val);
        var runner = this.head;
        while(runner.next){
            runner = runner.next;
        }
        runner.next = node;
        this.tail = node;
        return node;
    }
    //return and remove last node of the list
    pop(){
        var runner = this.head;
        while(runner.next.next){
            runner = runner.next;
        }
        var deletedRunner = runner.next;
        runner.next = null;
        this.tail = runner;
        return deletedRunner
    }
    //top will return the value of the last node
    top(){
        var runner = this.head;
        while(runner.next){
            runner = runner.next;
        }
        return runner
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
    isPalendrome(){
        var stackList = new SLSTACK();
        stackList.head = this.head;
        var stackRunner = stackList.head
        var runner = this.head;
        var length = this.size();
        for(var i = 0; i < length; i++){
            var node = new SLNode(runner.val);
            stackList.push(node);
            console.log("stackRunner.val" + stackRunner.val + "==" + "runner.val" + runner.val);
            runner = runner.next;
        }
        runner = this.head;
        stackRunner = stackList.head
        for(var i = 0; i < length; i++){
            if(runner.val != stackRunner.val){
                return false;
            }1
            runner = runner.next;
        }
        return true;
    }
}


node0 = new SLNode(0);
node1 = new SLNode(1);
node2 = new SLNode(0);
node3 = new SLNode(0);
node4 = new SLNode(1);
node5 = new SLNode(0);
node0.next = node1;
node1.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node5;
var listQueue = new SLQUEUE();
listQueue.head = node0;
listQueue.tail = node5;

console.log(listQueue.isPalendrome());

