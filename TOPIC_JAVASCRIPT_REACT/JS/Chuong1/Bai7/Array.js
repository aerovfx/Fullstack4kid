// function show(){
//     const myArray = ["Python","Javascript", "R", "C", "C++", "C#"];
//     const newArrayLen = myArray.length;
//     //loop for
//     let arrValue = "<ul>";
//     for (let i = 0; i < newArrayLen; i++ ){
//         arrValue += "<li>" + myArray[i] + "</li>";

//     }
//     arrValue += "</ul>"



//     document.getElementById("show").innerHTML = arrValue;
// }
// for Each
// function show(){
//     const myArray = ["Python","Javascript", "R", "C", "C++", "C#"];
//     //loop for
//     let arrValue = "<ul>";
//     myArray.forEach(myFunction);
//     arrValue += "</ul>"
    
//     function myFunction(value) {
//         arrValue += "<li>" + value + "</li>"
//     }



//     document.getElementById("show").innerHTML = arrValue;
// }

// .Map()
// function show(){
//     const myArray = ["Python","Javascript", "R", "C", "C++", "C#"];
//     const myList = myArray.map((item) => `<li>${item}</li>`);
//     document.getElementById("show").innerHTML = myList;
// }

// function show(){
//     const myArray = [1,2,3,4,5,6];
//     const myList = myArray.map((item) => item *2 );
//     // const item = myArray[[i] * 2];
//     newArray = [];
//     newArray.push(myList);
//     // console.log(myArray, newArray)
//     // document.getElementById("show").innerHTML = (myArray, newArray);
//     document.write(myArray, newArray);
// }

//.Filter()
function show(){
    const myArray = ["Python","Javascript", "R", "C", "C++", "C#"];
    const result = myArray.filter(checkLevel);

    function checkLevel(checkLevel){
        return checkLevel != "Python"
    }
    document.getElementById("show").innerHTML = result;
}