function output(){
    log = imbeddedOutput();
    console.log("made it here");
    return log;
}
function imbeddedOutput(){
    return "imbeddedOutput";
}
here = output();
console.log(here);