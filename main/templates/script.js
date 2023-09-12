const foodButton = document.getElementById("foodButton");
const drinkButton = document.getElementById("drinkButton");
const foodAudio = document.getElementById("foodAudio");
const drinkAudio = document.getElementById("drinkAudio");

foodButton.addEventListener("click", playButtonClickSound.bind(null, foodAudio));
drinkButton.addEventListener("click", playButtonClickSound.bind(null, drinkAudio));

function playButtonClickSound(audioElement) {
    if (audioElement.paused) {
        audioElement.play();
    } else {
        audioElement.currentTime = 0;
    }
}

