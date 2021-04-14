class SLNode{
    constructor(val){
        this.val = val;
        //this variable is called the pointer.
        this.next = null;
    }
}

class SLL{
    constructor(){
        this.head = null;
    }

    addFront(val){
        var node = new SLNode(val);
        if(this.head == null){
            node = this.head;
        }
        else{
            node.next = this.head;
            this.head = node;
                
        }
    }

    search(val){
        var runner = this.head;
        while(runner){
            if(runner.val == val){
                return true;
            }
            runner = runner.next;
        }
        return false;
    }

    addBack(val){
        var node = new SLNode(val);
        var runner = this.head;
        while(runner.next){
            runner = runner.next;
        }
        runner.next = node;
        return node;
    }

    removeHead(){
        var runner = this.head.next;
        this.head.next = null;
        this.head = runner;
    }

    //THIS IS EXAMPLE CODE OF REMOVING THE LIST
    //
    // removeFromList(numOnList){
    //     if(this.head == null){
    //         break;
    //     }
    //     var runner = this.head;
    //     var i = 0;
    //     while(runner.next){

    //         runner = runner.next;
    //         i++;
    //     }
    // }
}


node0 = new SLNode(0);
node1 = new SLNode(1);
node0.next = node1; 

var nodeList = new SLL();
nodeList.head = node0;

nodeList.addFront(2);

console.log(nodeList.head);
console.log(nodeList.search(1));
nodeList.addBack(5);
console.log(nodeList.head.next.next.next);

nodeList.removeHead();
console.log(nodeList.head);


//is there a head?
//yes?
//point the current node to the head,
//then make current node head.
//no?
//this.node = list.head;



//itterating::
//create variable runner = head
//while(runner)
//
// node0 = new SLNode(2);
// console.log(node0.val);