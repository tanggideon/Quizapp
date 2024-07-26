const begin = document.getElementById("begin");
const main = document.getElementById("quiz-container");
const quizForm = document.getElementById("quiz-form");
const quizInstruction = document.getElementById("quiz-instructions");
const toast = document.getElementById("liveToast");

begin.onclick = function () {
  prompt("Enter your student ID to begin quiz");
  quizInstruction.style.display = "none";
  quizForm.style.display = "block";
  let count = 0;
  function timer() {
    count++;
    if (count % 5 === 0) {
      const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toast);
      toastBootstrap.show();
    }
  }
  setInterval(timer, 1000);
};

