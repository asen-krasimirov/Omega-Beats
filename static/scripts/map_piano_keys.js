const keyTexts = [...document.querySelectorAll('.key-text')]

document.querySelector('.map-button').addEventListener('click', () => {
    for (const key of keyTexts) {
        key.classList.toggle('show');
    }
});
