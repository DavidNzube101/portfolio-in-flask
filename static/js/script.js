// Smooth scrolling to section when a link is clicked
document.addEventListener("DOMContentLoaded", function () {
    const links = document.querySelectorAll('a[href^="#"]');
    for (const link of links) {
        link.addEventListener("click", function (e) {
            e.preventDefault();
            const targetId = this.getAttribute("href").substring(1);
            const targetSection = document.getElementById(targetId);
            window.scrollTo({
                top: targetSection.offsetTop - 50, // Adjust for header height
                behavior: "smooth",
            });
        });
    }
});

const letters = "ABCDEDFGHIJKLMNOPQRSTUVWXYZ"
text = document.getElementById('logo')
container = document.querySelector(".logo")

text2 = document.getElementById('hero-text')
container2 = document.querySelector("#hero-text__container")

text.onmouseover = event => {
    let iterations = 0;

    const interval = setInterval(() => {
        event.target.innerText = event.target.innerText.split("").map((letter, index) => {

        if (index < iterations) {
            return event.target.dataset.value[index]
        }

        return letters[Math.floor(Math.random() * 26)]

        }).join("")

        if (iterations >= event.target.dataset.value.length) {
            clearInterval(interval)
        }

        iterations += 1 / 3
    }, 100)
}

text2.onmouseover = event => {
    let iterations = 0;

    const interval = setInterval(() => {
        event.target.innerText = event.target.innerText.split("").map((letter, index) => {

        if (index < iterations) {
            return event.target.dataset.value[index]
        }

        return letters[Math.floor(Math.random() * 26)]

        }).join("")

        if (iterations >= event.target.dataset.value.length) {
            clearInterval(interval)
        }

        iterations += 1 / 2
    }, 100)
}