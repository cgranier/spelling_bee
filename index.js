const findWordsButton = document.getElementById("findWordsButton");
const lettersInput = document.getElementById("letters");
const requiredLetterInput = document.getElementById("requiredLetter");
const solutionList = document.getElementById("solution");

findWordsButton.addEventListener("click", () => {
  const letters = lettersInput.value;
  const requiredLetter = requiredLetterInput.value;
  const words = findWords(letters, requiredLetter);
  const sortedWords = sortWords(words);
  updateSolutionList(sortedWords, solutionList);
});

function updateSolutionList(sortedWords, solutionList) {
  solutionList.innerHTML = "";
  sortedWords.forEach((word) => {
    const listItem = document.createElement("li");
    listItem.textContent = word;
    solutionList.appendChild(listItem);
  });
}
