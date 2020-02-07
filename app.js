let button=document.getElementById("button");
let h1=document.getElementById("head");
function sayhello(){
    console.log("1");
    axios.get('https://swapi.co/api/people/1/').then(function(response){
        console.log(response);
        h1.innerHTML=response.data.name;
    });
    console.log("2");
}
button.addEventListener('click',sayhello); 