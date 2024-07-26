const tableRows = document.querySelectorAll("tr")
const begin = document.getElementById("begin")
const main = document.getElementById("quiz-container")
const quizForm = document.getElementById("quiz-form")
const quizInstruction = document.getElementById("quiz-instructions")
const toast = document.getElementById('liveToast')

tableRows.forEach (row => {
    row.onclick = function() {
        if(confirm("Are you sure you want to take quiz?")) {
            console.log(row);
            window.open("{% url 'quiz' %}")
        }           
        
    }
})
begin.onclick = function() {
    prompt("Enter your student ID to begin quiz")
    quizInstruction.style.display = "none"
    quizForm.style.display = "block"
    let count = 0
    function timer (){
        count ++
        if (count % 5 === 0){
            const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toast)
            toastBootstrap.show()
        }
    }
    setInterval(timer, 1000)
}



// if (toastTrigger) {
//   const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toast)
//   toastTrigger.addEventListener('click', () => {
//     toastBootstrap.show()
//   })
// }