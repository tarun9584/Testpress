cont link="http://127.0.0.1:8000/"
const myJson;
const userAction = async () => {
   const response = await fetch(link+'Quizes');
   myJson = await response.json();
}
listQuiz()
{

 return(
     )
 }
function checkbox(){
var checkedValue = null;
var inputElements = document.getElementsByClassName('options');
for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].checked){
           checkedValue = inputElements[i].value;
           resut=resut+1;
           break;
      }
  }
  if(checkedValue==null){
     return(alert("you cant route another until you solve that question"));
  }
  else{

  }

}

function showCorrect(){
  document.write("correct");
}